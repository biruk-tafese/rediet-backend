# 🌿 REDIET — Daily Support & Motivation Platform
**Telegram Bot + Telegram Mini App (MVP)** powered by **Django**.

Rediet is a Telegram-based daily motivation system for Ethiopian youth and anyone who needs encouragement—delivering short daily messages in **Amharic + English**, optional **Bible verses**, **audio devotionals**, and a simple way to submit **prayer requests**.

> “One small message every day can change someone’s direction.”

---

## ✨ Features (MVP)

### 🤖 Telegram Bot
- `/start` onboarding + language selection (**🇪🇹 Amharic / 🇬🇧 English**)
- **Today’s message** (formatted, emotional, shareable)
- Optional **Bible verse**
- **Audio devotional** (30–90 sec voice/MP3)
- **Archive navigation** (last 7 days: Previous/Next)
- **Prayer request** submission (stored in DB)
- **Language switch** anytime
- **Share button** (Telegram-forward optimized)

### 📱 Telegram Mini App
- **Home**: clean reading UI for today’s message (large Amharic-friendly typography)
- **Audio player**
- **Share button**
- **Archive**: scroll/filter by date
- **Prayer page**: simple form → submit

### 🧠 Django Backend
- Content management (messages + audio)
- Telegram user tracking (language preference)
- Prayer request storage
- REST API for bot + mini app

---

## 🧩 System Architecture

**Flow**
```
User → Telegram Bot → Django API → Database → Response → Bot / Mini App
```

**Components**
- **Telegram Bot**: main interaction point (commands, buttons, message flow)
- **Telegram Mini App**: modern UI for reading + archive + prayer form
- **Django API**: data storage + endpoints for content and user activity

---

## 📦 Data Models (Concept)

### Message
- `title_am`, `title_en`
- `content_am`, `content_en`
- `verse` (optional)
- `audio` (optional)
- `created_at`

### TelegramUser
- `telegram_id` (unique)
- `language` (`am` default)
- `created_at`

### PrayerRequest
- `telegram_id`
- `message`
- `created_at`

---

## 🌐 API Endpoints (MVP)

Base URL example:
- Local: `http://127.0.0.1:8000`
- Production: `https://your-domain.com`

### ✅ Get Today’s Message
`GET /api/today/`

### ✅ Get Messages (Archive)
`GET /api/messages/`

Recommended query params (optional):
- `?limit=7`
- `?date=YYYY-MM-DD`

### ✅ Submit Prayer
`POST /api/prayer/`

**Body**
```json
{
  "telegram_id": "123456789",
  "message": "Please pray for my exams..."
}
```

### ✅ Update User (Language, etc.)
`POST /api/user/`

**Body**
```json
{
  "telegram_id": "123456789",
  "language": "am"
}
```

---

## 🚀 Quick Start (Backend — Django)

### 1) Requirements
- Python 3.10+ recommended
- pip
- (Optional) Git

### 2) Setup virtual environment
**Windows (PowerShell)**
```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
```

**macOS/Linux**
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### 3) Install dependencies
```bash
pip install django djangorestframework
```

> If you already have a `requirements.txt`, use:
```bash
pip install -r requirements.txt
```

### 4) Configure environment variables
Create a `.env` file (example):

```env
DJANGO_SECRET_KEY=change-me
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

# Optional (future) - for bot integration
TELEGRAM_BOT_TOKEN=123456:ABCDEF_your_token
API_BASE_URL=http://127.0.0.1:8000
```

### 5) Run migrations + start server
```bash
python manage.py migrate
python manage.py runserver
```

Open: http://127.0.0.1:8000/

### 6) Create admin user (optional)
```bash
python manage.py createsuperuser
```

Admin: http://127.0.0.1:8000/admin/

---

## 🤖 Telegram Bot (Recommended Structure)

You can implement the bot in a separate folder, for example:

```
bot/
  main.py
  requirements.txt
```

**Bot responsibilities**
- Handle `/start` → save user + ask language
- Show menu buttons: Today / Audio / Archive / Prayer / Language / Share
- Fetch content from Django via API:
  - `/api/today/`
  - `/api/messages/`
- Post prayer requests via `/api/prayer/`

> Next step: if you want, I can generate a clean bot skeleton (Python) that already integrates with these endpoints.

---

## 📱 Telegram Mini App (Recommended Structure)

Typical folder structure:
```
miniapp/
  (Next.js / React project)
```

**Mini App responsibilities**
- Display today’s message (clean UI)
- Audio player
- Archive list & filter
- Prayer submission form → POST `/api/prayer/`

> Next step: I can also generate a Next.js Telegram WebApp starter template and connect it to your API.

---

## 🧪 Suggested MVP Testing Checklist
- [ ] Add a few Message entries in Django admin (Amharic + English)
- [ ] `GET /api/today/` returns the correct message for the current date
- [ ] Bot displays message in correct language
- [ ] Archive navigation loads last 7 messages
- [ ] Prayer request saves to database
- [ ] Audio file uploads and is served correctly
- [ ] Mini app shows today’s message and can submit a prayer request

---

## 🗓️ 3-Day Implementation Plan (MVP)
**Day 1**
- Django setup
- Models + Admin
- Bot skeleton (start/menu)

**Day 2**
- Bot logic (today/archive/prayer)
- API integration
- Content workflow

**Day 3**
- Mini app UI (Next.js)
- Audio feature
- Deploy backend + bot webhook

---

## 📤 Share Format (Growth Engine)
Each message supports a share-friendly template:

```
🌿 Rediet - Daily Support

[message]

📖 [verse]

👉 Join: @rediet_bot
```

---

## 🔒 Notes & Best Practices
- Keep messages short, emotional, and readable (mobile-first)
- Avoid complex logins (Telegram identity is enough for MVP)
- Do not commit secrets or `.venv/`
- Use `.gitignore` for Python + environment files

Example `.gitignore`:
```gitignore
.venv/
__pycache__/
*.pyc
db.sqlite3
.env
media/
```

---

## 🤝 Contributing
Contributions, ideas, and feedback are welcome.  
Open an issue or submit a PR.

---

## 📄 License
Add a license if you plan to make the repo public (MIT is common). For now:
- **All rights reserved** (default) unless you add a LICENSE file.

---

## 📬 Contact
Project owner: **@biruk-tafese**  
If you want help building the next step (bot starter code, mini app template, or deployment), open an issue with what you want to tackle next.
