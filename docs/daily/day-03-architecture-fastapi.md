# 📘 ملف تعلّم Claude Code — اليوم الثالث

**الطالب:** أحمد سليق  
**المدرّب:** Claude Sonnet 4.6  
**اليوم:** اليوم الثالث — Architecture + هيكل المشروع + FastAPI  
**التاريخ:** 16 أبريل 2026  
**المدة الفعلية:** ~3 ساعات  
**المشروع:** Intelligent Research Assistant (RAG + Multi-Agent System)

---

## 🎯 ما الذي تعلمناه اليوم؟

اليوم انتقلنا من "أدوات" إلى "بناء" — بنينا الهيكل الكامل للمشروع وشغّلنا أول API حقيقي. مثل ما المهندس يرسم مخطط البناء قبل ما يبني، اليوم رسمنا وبنينا معاً.

---

### 1. شو هو Architecture المشروع؟

قبل ما تكتب أي كود، المهندس الجيد يرسم "خريطة" للمشروع — كيف تتصل الأجزاء ببعض.

مشروعنا:
```
المستخدم
    ↓
Next.js Frontend (الواجهة)
    ↓
FastAPI Backend (المحرك)
    ↓
Multi-Agent System
    ├── Researcher Agent → يبحث على الويب
    ├── Reader Agent    → يقرأ المصادر
    ├── Analyst Agent   → يحلل ويقارن
    └── Writer Agent    → يكتب التقرير
    ↓
ChromaDB (يحفظ ويسترجع المعلومات)
    ↓
OpenRouter API (الذكاء الاصطناعي)
```

---

### 2. شو هو Python venv؟

تخيّل عندك مطبخين — مطبخ للحلويات ومطبخ للأكل المالح. كل مطبخ عنده أدواته ومكوّناته الخاصة — ما تختلط.

venv = بيئة Python معزولة لكل مشروع. لو مشروع A يحتاج مكتبة بنسخة 1.0 ومشروع B يحتاجها بنسخة 2.0 — ما يتعارضوا.

**الأوامر:**
```powershell
python -m venv venv        # إنشاء البيئة
venv\Scripts\activate      # تفعيلها
# بتشوف (venv) في بداية السطر = أنت داخل البيئة
deactivate                 # للخروج منها
```

---

### 3. شو هو requirements.txt؟

قائمة المكتبات اللي يحتاجها مشروعك — مثل وصفة الطبخ. أي شخص ثاني يشغّل مشروعك يكتب:
```
pip install -r requirements.txt
```
وكل شي يتثبّت تلقائياً.

**الفرق بين venv و requirements.txt:**
- `venv` = المطبخ المعزول نفسه
- `requirements.txt` = قائمة المكونات (الوصفة)

---

### 4. شو هو FastAPI؟

إطار عمل Python لبناء APIs بسرعة. مميزاته:
- سريع جداً
- يولّد توثيق تلقائي (`/docs`)
- سهل الكتابة

**مثال بسيط:**
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}
```

---

### 5. شو هو Swagger UI (/docs)؟

FastAPI يولّد صفحة توثيق تلقائية على `/docs` — تقدر تشوف كل الـendpoints وتجرّبها من المتصفح بدون أي كود إضافي!

---

### 6. شو هو __init__.py؟

ملف فارغ يخبر Python إن هاد المجلد "حزمة" (package) يقدر يستوردها. بدونه Python ما يقدر يستورد الكود من داخل المجلد.

---

### 7. شو هو uvicorn؟

Server يشغّل تطبيق FastAPI. مثل "المحرك" اللي يشغّل السيارة.

```powershell
uvicorn main:app --reload
# main = اسم الملف (main.py)
# app = اسم المتغير في الكود
# --reload = أعد التشغيل تلقائياً لما تغيّر الكود
```

---

## 🛠️ كل الأوامر التي استخدمناها اليوم

---

**الأمر:**
```powershell
python --version
pip --version
```
**وظيفته:** التحقق من تثبيت Python وpip  
**الناتج:** `Python 3.12.9` و `pip 24.3.1`

---

**الأمر:**
```powershell
python -m venv venv
```
**شو يعني؟** "أنشئ بيئة Python معزولة اسمها venv"  
**وظيفته:** ينشئ مجلد `venv` فيه Python منفصل للمشروع  
**متى نستخدمه؟** مرة وحدة في بداية كل مشروع

---

**الأمر:**
```powershell
venv\Scripts\activate
```
**شو يعني؟** "فعّل البيئة المعزولة"  
**الناتج:** `(venv)` يظهر في بداية السطر  
**ملاحظة:** لازم تفعّله كل مرة تفتح PowerShell جديد

---

**الأمر:**
```powershell
mkdir backend, backend\agents, backend\api, backend\core, backend\rag, frontend, tests
```
**وظيفته:** ينشئ كل مجلدات المشروع دفعة وحدة

---

**الأمر:**
```powershell
pip install fastapi uvicorn python-dotenv pydantic httpx
```
**وظيفته:** يثبّت المكتبات الأساسية  
**داخل venv:** يثبّتها في البيئة المعزولة فقط

---

**الأمر:**
```powershell
uvicorn main:app --reload
```
**وظيفته:** يشغّل الـserver على `http://127.0.0.1:8000`  
**ملاحظة:** `--reload` يعيد التشغيل تلقائياً عند تغيير الكود

---

## 🐛 الأخطاء التي واجهتنا وكيف حللناها

**الخطأ:** `python --version` ما يطلع شي  
**السبب:** Python 3.14 مثبّت بس PATH ناقص  
**الحل:** حذفنا النسخة القديمة وثبّتنا Python 3.12.9 مع تفعيل "Add to PATH" ✅  
**الدرس:** دائماً فعّل "Add Python to PATH" عند التثبيت

---

## 🧠 أسئلة الاختبار + الأجوبة

**س1:** شو هو الـvenv وليش نستخدمه؟  
**ج:** بيئة Python معزولة لكل مشروع حتى لا تتخلط المكتبات ✅

**س2:** شو هو `/docs`؟  
**ج:** Swagger UI — توثيق تلقائي لكل الـAPI يولّده FastAPI ✅

**س3:** شو يعني `__init__.py`؟  
**ج:** يخبر Python إن المجلد حزمة يقدر يستوردها ✅

**بونص:** شو الفرق بين `requirements.txt` و `venv`؟  
**ج:** venv = البيئة المعزولة، requirements.txt = قائمة المكتبات ✅

---

## 📊 ملخص سريع

### أهم الأوامر:

| الأمر | شو يعمل |
|-------|---------|
| `python -m venv venv` | إنشاء بيئة معزولة |
| `venv\Scripts\activate` | تفعيل البيئة |
| `pip install -r requirements.txt` | تثبيت كل المكتبات |
| `uvicorn main:app --reload` | تشغيل الـserver |

### هيكل المشروع الحالي:
```
intelligent-research-assistant/
├── backend/
│   ├── agents/
│   ├── api/
│   ├── core/
│   ├── rag/
│   ├── main.py
│   └── __init__.py
├── frontend/
├── tests/
├── docs/
├── venv/
├── requirements.txt
├── .env.example
├── .gitignore
├── CLAUDE.md
├── PROGRESS.md
└── README.md
```

### ✅ ما أتقنته اليوم:
- إنشاء وتفعيل venv
- بناء هيكل المشروع كامل
- كتابة أول FastAPI app
- تشغيل server حقيقي
- فهم Swagger UI
- حل مشكلة Python PATH

### ⚠️ للمراجعة قبل يوم 4:
- تذكّر تفعّل `venv\Scripts\activate` كل مرة تفتح PowerShell
- الـserver يوقف لما تغلق PowerShell — طبيعي

### 🎯 التحدي الأكبر:
مشكلة Python PATH — أخذت وقتاً لكن القرار بتثبيت نسخة جديدة كان صح.

### 💡 أهم درس:
لما تثبّت Python دائماً فعّل "Add to PATH" — يوفّر عليك مشاكل كثيرة.

---

## 📅 التحضير ليوم 4

**موضوع يوم 4:** Python refresh (typing, async) + Git workflow + أول endpoint حقيقي

**ما أحتاج أحضّره:**
- تأكد إن `(venv)` يظهر لما تفتح PowerShell وتفعّل البيئة

---

**نهاية توثيق اليوم الثالث** ✅  
📌 *"الكود الجيد يبدأ بهيكل جيد"*
