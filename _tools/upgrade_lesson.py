#!/usr/bin/env python3
"""Insert v2 'deep explanation' blocks into an existing lesson WITHOUT rewriting it.

    from upgrade_lesson import Lesson
    L = Lesson("08 Options & Dealer Positioning/8.1 Options Basics- Calls & Puts.md")
    L.after_callout("en", "mindset", EN_ELI5)     # right after the > [!mindset] block
    L.before_heading("en", "2.", EN_BLOCK)        # before the line "## 2. ..."
    L.before_callout("en", "example", EN_BLOCK)   # before the first > [!example]
    L.at_end("en", EN_BLOCK)                      # end of the EN (or TH) section
    L.set_meta("level", "v2")
    L.save()

Every insert is idempotent: if the block's first line is already in that language section, it is skipped,
so the script can be re-run safely.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class Lesson:
    def __init__(self, rel):
        self.path = ROOT / rel
        text = self.path.read_text(encoding="utf-8")
        m = re.search(r"%%\s*EN\s*%%", text)
        n = re.search(r"%%\s*TH\s*%%", text)
        self.head = text[:m.end()]
        self.sec = {"en": text[m.end():n.start()].split("\n"), "th": text[n.end():].split("\n")}
        self.th_marker = text[n.start():n.end()]
        self.added = 0

    # -- helpers
    def _has(self, lang, block):
        lines = [l.strip() for l in block.strip().split("\n") if l.strip()]
        sig = next((l for l in lines if len(l) > 30), lines[0])  # a distinctive line, not just "> [!analogy]"
        return sig in [x.strip() for x in self.sec[lang]]

    def _insert(self, lang, idx, block):
        if self._has(lang, block):
            return
        lines = self.sec[lang]
        new = [""] + block.strip("\n").split("\n") + [""]
        lines[idx:idx] = new
        # collapse >2 blank lines
        out = []
        for l in lines:
            if l.strip() == "" and len(out) >= 2 and out[-1].strip() == "" and out[-2].strip() == "":
                continue
            out.append(l)
        self.sec[lang] = out
        self.added += 1

    def _find(self, lang, pred, start=0):
        for i, l in enumerate(self.sec[lang][start:], start):
            if pred(l):
                return i
        raise ValueError(f"anchor not found in {self.path.name} [{lang}]")

    # -- public API
    def after_callout(self, lang, kind, block):
        i = self._find(lang, lambda l: l.startswith(f"> [!{kind}]"))
        while i < len(self.sec[lang]) and self.sec[lang][i].startswith(">"):
            i += 1
        self._insert(lang, i, block)

    def before_callout(self, lang, kind, block):
        self._insert(lang, self._find(lang, lambda l: l.startswith(f"> [!{kind}]")), block)

    def before_heading(self, lang, prefix, block):
        self._insert(lang, self._find(lang, lambda l: l.startswith(f"## {prefix}")), block)

    def at_end(self, lang, block):
        lines = self.sec[lang]
        while lines and lines[-1].strip() == "":
            lines.pop()
        self._insert(lang, len(lines), block)

    def set_meta(self, key, value):
        if re.search(rf"^{key}:", self.head, re.M):
            self.head = re.sub(rf"^{key}:.*$", f"{key}: {value}", self.head, flags=re.M)
        else:
            self.head = re.sub(r"^(status:.*)$", rf"\1\n{key}: {value}", self.head, count=1, flags=re.M)

    def save(self):
        text = self.head + "\n".join(self.sec["en"]) + self.th_marker + "\n".join(self.sec["th"])
        text = text.rstrip() + "\n"
        self.path.write_text(text, encoding="utf-8")
        print(f"{self.path.name}: +{self.added} blocks")
