---
tags: [system, publishing]
---
%% EN %%
# Publishing Guide: GitHub Pages, automatic builds & PDFs

> [!mindset]
> Publishing should be boring: you edit lessons in Obsidian, push, and a few minutes later the website and the PDFs are up to date. A robot does the building, the same way every time.

## 1. What gets published, and what becomes public

| Part | Where it ends up | Who can see it |
|---|---|---|
| Lessons with `status: done`, glossary, disclaimer, drills, calculator | the website (`site/`) | everyone with the link |
| One printable PDF per phase, English and Thai | `site/pdf/`, linked from each phase page | everyone with the link |
| The whole vault (notes, `_System`, `_tools`, `CLAUDE.md`) | the GitHub **repository** | depends on the repository: see below |

> [!caution] Public repository on the free plan
> GitHub Pages works with **public** repositories on GitHub Free. Private repositories need a paid plan (GitHub Pro, Team or Enterprise), as of October 2026 *(GitHub Docs, "GitHub Pages limits" / "GitHub's plans")*. In a public repository **every file in the vault is visible**, including `_System` notes, `CLAUDE.md` (which names the owner) and your own journal notes if you keep them in the vault. Before the first push: keep private notes outside this folder or add them to `.gitignore`, and read through `_System` once.

## 2. One-time setup (about 15 minutes)

1. Make a free account at github.com. Install **GitHub Desktop** (easiest) or the `git` command-line tool.
2. Create a new repository, e.g. `traders-path` (public, see the caution above). Don't add a README; the vault already has files.
3. Put the vault in it. With the command line, in Terminal:
   ```bash
   cd "/Users/kyedev/Documents/ME/Own-project/Investing"
   git init -b main
   git add .
   git commit -m "Trader's Path vault"
   git remote add origin https://github.com/<your-user>/traders-path.git
   git push -u origin main
   ```
   With GitHub Desktop: *File → Add local repository →* choose the vault folder → *Publish repository*.
4. On github.com open the repository → **Settings → Pages → Build and deployment → Source: GitHub Actions**.
5. Open the **Actions** tab. The workflow **Publish site** starts on every push; the first run takes about 3–5 minutes. When it's green, the site is at `https://<your-user>.github.io/traders-path/`.

The `site/` folder is in `.gitignore` on purpose: GitHub builds it fresh every time, so pages from renamed lessons never linger (a known gotcha of `build.py`, which never deletes old files).

## 3. Every day

1. Edit lessons in Obsidian as usual.
2. If you changed figure code, run `python3 _tools/make_figures.py <phase>` (figures are committed as files; the robot doesn't redraw them). If you changed drills, run `python3 _tools/drills/make_drills.py`.
3. Commit and push (GitHub Desktop: write a short summary → *Commit to main* → *Push origin*).
4. Watch the Actions tab. Green = live. Red = open the failed step; the message says what's wrong.

What the robot runs, in order (`.github/workflows/publish-site.yml`):
1. installs Python and `markdown` (`requirements.txt`) and Thai fonts;
2. `python _tools/make_pdfs.py`: one A4 PDF per phase and language;
3. `python _tools/build.py`: the website, including links to the PDFs;
4. a safety check that fails if any page still contains raw Obsidian embeds (`![[…]]`) or render tokens;
5. uploads `site/` and publishes it.

## 4. Preview on your own computer

```bash
python3 _tools/make_pdfs.py      # optional, ~40 s; needs Google Chrome
python3 _tools/build.py
open site/index.html
```

## 5. Before a big publish: quality checklist

- [ ] `python3 _tools/qa/figure_check.py` → **0 issues**
- [ ] `python3 _tools/qa/fact_register.py` → no ⚠ rows you haven't re-checked ([[Fact Register]])
- [ ] `python3 _tools/qa/thai_check.py` → Part A empty; Part B read ([[Thai Review List]])
- [ ] [[Disclaimer]] read and approved
- [ ] `last_reviewed` updated on the lessons you re-checked

## 6. If something goes wrong

| Symptom | Likely cause | Fix |
|---|---|---|
| Actions tab shows nothing after a push | Workflow file missing or branch isn't `main` | Check `.github/workflows/publish-site.yml` is committed; push to `main` |
| Deploy step: "Pages not enabled" / 404 site | Pages source not set | Settings → Pages → Source: **GitHub Actions** |
| "Check that no raw Obsidian syntax…" fails | A lesson embeds a figure that doesn't exist, or a broken block | The log lists the page; fix the lesson, push again |
| PDF has boxes instead of Thai letters | Fonts missing (only on your own machine) | Install *Noto Sans Thai*; the robot installs Thai fonts itself |
| Old page still online after renaming a lesson | (only with a committed `site/`) | Keep `site/` out of git; the robot builds fresh |

A custom domain (e.g. `traderspath.com`) is optional: Settings → Pages → Custom domain, then add the DNS records GitHub shows you.

%% TH %%
---
# คู่มือการเผยแพร่: GitHub Pages, การ Build อัตโนมัติ และ PDF

> [!mindset]
> การเผยแพร่ควรเป็นเรื่องน่าเบื่อ: คุณแก้บทเรียนใน Obsidian กด Push แล้วไม่กี่นาทีต่อมาเว็บไซต์และ PDF ก็อัปเดต หุ่นยนต์เป็นคน Build ให้ ด้วยวิธีเดิมทุกครั้ง

## 1. อะไรถูกเผยแพร่ และอะไรจะกลายเป็นสาธารณะ

| ส่วน | ไปอยู่ที่ไหน | ใครเห็นได้ |
|---|---|---|
| บทเรียนที่ `status: done` อภิธานศัพท์ ข้อจำกัดความรับผิดชอบ แบบฝึก เครื่องคำนวณ | เว็บไซต์ (`site/`) | ทุกคนที่มีลิงก์ |
| PDF สำหรับพิมพ์เฟสละหนึ่งไฟล์ ภาษาอังกฤษและภาษาไทย | `site/pdf/` มีลิงก์จากหน้าของแต่ละเฟส | ทุกคนที่มีลิงก์ |
| ทั้ง Vault (โน้ต `_System` `_tools` `CLAUDE.md`) | **Repository** บน GitHub | ขึ้นกับ Repository: ดูด้านล่าง |

> [!caution] Repository สาธารณะในแพ็กเกจฟรี
> GitHub Pages ใช้ได้กับ Repository **สาธารณะ (Public)** ใน GitHub Free ส่วน Repository ส่วนตัว (Private) ต้องใช้แพ็กเกจเสียเงิน (GitHub Pro, Team หรือ Enterprise) ณ ตุลาคม 2026 *(GitHub Docs, "GitHub Pages limits" / "GitHub's plans")* ใน Repository สาธารณะ **ทุกไฟล์ใน Vault มองเห็นได้** รวมถึงโน้ตใน `_System` และ `CLAUDE.md` (ซึ่งระบุชื่อเจ้าของ) และบันทึกเทรดของคุณถ้าเก็บไว้ใน Vault ก่อน Push ครั้งแรก: เก็บโน้ตส่วนตัวไว้นอกโฟลเดอร์นี้หรือใส่ใน `.gitignore` และอ่านทบทวน `_System` หนึ่งรอบ

## 2. ตั้งค่าครั้งเดียว (ประมาณ 15 นาที)

1. สมัครบัญชีฟรีที่ github.com ติดตั้ง **GitHub Desktop** (ง่ายที่สุด) หรือเครื่องมือบรรทัดคำสั่ง `git`
2. สร้าง Repository ใหม่ เช่น `traders-path` (สาธารณะ ดูคำเตือนด้านบน) ไม่ต้องเพิ่ม README เพราะ Vault มีไฟล์อยู่แล้ว
3. ใส่ Vault ลงไป ถ้าใช้บรรทัดคำสั่ง ใน Terminal:
   ```bash
   cd "/Users/kyedev/Documents/ME/Own-project/Investing"
   git init -b main
   git add .
   git commit -m "Trader's Path vault"
   git remote add origin https://github.com/<your-user>/traders-path.git
   git push -u origin main
   ```
   ถ้าใช้ GitHub Desktop: *File → Add local repository →* เลือกโฟลเดอร์ Vault → *Publish repository*
4. บน github.com เปิด Repository → **Settings → Pages → Build and deployment → Source: GitHub Actions**
5. เปิดแท็บ **Actions** เวิร์กโฟลว์ **Publish site** จะเริ่มทุกครั้งที่ Push รอบแรกใช้เวลาประมาณ 3–5 นาที เมื่อขึ้นสีเขียว เว็บไซต์จะอยู่ที่ `https://<your-user>.github.io/traders-path/`

โฟลเดอร์ `site/` อยู่ใน `.gitignore` โดยตั้งใจ: GitHub Build ใหม่ทุกครั้ง หน้าของบทเรียนที่เปลี่ยนชื่อจึงไม่ค้างอยู่ (ปัญหาที่รู้กันของ `build.py` ซึ่งไม่เคยลบไฟล์เก่า)

## 3. ใช้งานประจำวัน

1. แก้บทเรียนใน Obsidian ตามปกติ
2. ถ้าแก้โค้ดภาพประกอบ ให้รัน `python3 _tools/make_figures.py <phase>` (ภาพถูก Commit เป็นไฟล์ หุ่นยนต์ไม่วาดใหม่) ถ้าแก้แบบฝึก ให้รัน `python3 _tools/drills/make_drills.py`
3. Commit และ Push (GitHub Desktop: เขียนสรุปสั้น ๆ → *Commit to main* → *Push origin*)
4. ดูแท็บ Actions สีเขียว = ขึ้นเว็บแล้ว สีแดง = เปิดขั้นตอนที่ล้มเหลว ข้อความจะบอกว่าผิดตรงไหน

สิ่งที่หุ่นยนต์ทำตามลำดับ (`.github/workflows/publish-site.yml`):
1. ติดตั้ง Python และ `markdown` (`requirements.txt`) และฟอนต์ภาษาไทย
2. `python _tools/make_pdfs.py`: PDF ขนาด A4 เฟสละหนึ่งไฟล์ต่อภาษา
3. `python _tools/build.py`: เว็บไซต์ รวมลิงก์ไปยัง PDF
4. การตรวจความปลอดภัยที่จะล้มเหลวถ้าหน้าใดยังมีโค้ดฝังภาพของ Obsidian (`![[…]]`) หรือโทเคนที่ยังไม่ถูกแปลง
5. อัปโหลด `site/` และเผยแพร่

## 4. ดูตัวอย่างบนเครื่องของคุณ

```bash
python3 _tools/make_pdfs.py      # ไม่บังคับ ~40 วินาที ต้องมี Google Chrome
python3 _tools/build.py
open site/index.html
```

## 5. ก่อนเผยแพร่ครั้งใหญ่: เช็กลิสต์คุณภาพ

- [ ] `python3 _tools/qa/figure_check.py` → **0 ปัญหา**
- [ ] `python3 _tools/qa/fact_register.py` → ไม่มีแถว ⚠ ที่ยังไม่ได้ตรวจซ้ำ ([[Fact Register]])
- [ ] `python3 _tools/qa/thai_check.py` → Part A ว่าง และอ่าน Part B แล้ว ([[Thai Review List]])
- [ ] อ่านและอนุมัติ [[Disclaimer]] แล้ว
- [ ] อัปเดต `last_reviewed` ในบทเรียนที่ตรวจซ้ำแล้ว

## 6. ถ้ามีอะไรผิดพลาด

| อาการ | สาเหตุที่เป็นไปได้ | วิธีแก้ |
|---|---|---|
| แท็บ Actions ไม่มีอะไรหลัง Push | ไม่มีไฟล์เวิร์กโฟลว์ หรือ Branch ไม่ใช่ `main` | ตรวจว่า Commit `.github/workflows/publish-site.yml` แล้ว และ Push ไปที่ `main` |
| ขั้น Deploy: "Pages not enabled" / เว็บขึ้น 404 | ยังไม่ได้ตั้ง Source ของ Pages | Settings → Pages → Source: **GitHub Actions** |
| ขั้น "Check that no raw Obsidian syntax…" ล้มเหลว | บทเรียนฝังภาพที่ไม่มีอยู่ หรือบล็อกเสีย | Log จะบอกหน้า แก้บทเรียนแล้ว Push ใหม่ |
| PDF แสดงกล่องแทนตัวอักษรไทย | ไม่มีฟอนต์ (เฉพาะบนเครื่องของคุณ) | ติดตั้ง *Noto Sans Thai* หุ่นยนต์ติดตั้งฟอนต์ไทยเองอยู่แล้ว |
| หน้าเก่ายังออนไลน์หลังเปลี่ยนชื่อบทเรียน | (เฉพาะเมื่อ Commit `site/`) | อย่าใส่ `site/` ใน git ให้หุ่นยนต์ Build ใหม่ |

โดเมนของตัวเอง (เช่น `traderspath.com`) เป็นทางเลือก: Settings → Pages → Custom domain แล้วเพิ่มระเบียน DNS ตามที่ GitHub แสดง
