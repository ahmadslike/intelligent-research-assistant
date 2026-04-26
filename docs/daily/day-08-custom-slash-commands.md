# 📘 ملف تعلّم Claude Code — اليوم الثامن

**الطالب:** أحمد سليق  
**المدرّب:** Claude Sonnet 4.6  
**اليوم:** اليوم الثامن — Custom Slash Commands  
**التاريخ:** 26 أبريل 2026  
**المدة الفعلية:** ~2 ساعة  
**المشروع:** Intelligent Research Assistant (RAG + Multi-Agent System)

---

## 🎯 ما الذي تعلمناه اليوم؟

Custom Slash Commands = أوامر تصنعها أنت لمشروعك. بدل ما تكتب نفس الطلب الطويل كل مرة، تكتب أمر وحد.

---

### شو هي Custom Slash Commands؟

أوامر مخصصة تحفظها في `.claude/commands/` كملفات Markdown. كل ملف = أمر واحد.

**الفرق عن الأوامر المدمجة:**
- `/init`, `/compact`, `/cost` → مدمجة في Claude Code من Anthropic
- `/test-rag`, `/deploy-check`, `/ingest-pdf` → أنت صنعتها لمشروعك

---

## 🛠️ الـCommands التي بنيناها اليوم

### 1. /test-rag
يختبر RAG system كامل:
- يضيف 3 مستندات
- يبحث ويعرض النتائج
- يعدّ المستندات
- يعمل جدول واضح للنتائج

### 2. /deploy-check
يفحص جاهزية المشروع للـdeploy:
- يتحقق من الملفات المهمة
- يفحص syntax كل ملفات Python
- يصلح مشاكل تلقائياً (مثل UTF-16)
- يعمل تقرير كامل

### 3. /ingest-pdf
يضيف PDF للـRAG system:
- يقرأ الملف
- يقسّمه chunks
- يحفظ كل chunk في ChromaDB

---

## 📁 مكان الحفظ

```
.claude/
└── commands/
    ├── test-rag.md      ← /test-rag
    ├── deploy-check.md  ← /deploy-check
    └── ingest-pdf.md    ← /ingest-pdf
```

---

## 🧪 نتائج مذهلة

### /test-rag
```
✅ Add Documents — PASSED (3 docs)
✅ Search — PASSED (نتائج مرتّبة بالـdistance)
✅ Count — PASSED (count: 3)
```

### /deploy-check
```
✅ requirements.txt
✅ .env.example  
✅ CLAUDE.md
✅ venv + packages
✅ Server running
✅ Syntax — PASS (fixed UTF-16 automatically!)
✅ .gitignore
```

**أهم شي:** Claude اكتشف مشكلة UTF-16 في `__init__.py` files وصلّحها تلقائياً بدون ما تطلب منه! 🤖

---

## 🧠 أسئلة الاختبار + الأجوبة

**س1:** شو هي Custom Slash Commands وين تتحفظ؟  
**ج:** أوامر مخصصة نصنعها بملفات Markdown في `.claude/commands/` ✅

**س2:** شو الفرق بين `/test-rag` و `/init`؟  
**ج:** `/test-rag` نحن صنعناه لمشروعنا، `/init` مدمج في Claude Code من Anthropic ✅

**س3:** شو عمل `/deploy-check` لما لاقى مشكلة؟  
**ج:** اكتشف المشكلة وصلّحها تلقائياً ✅

---

## 📅 التحضير ليوم 9

**موضوع يوم 9:** Sub-Agents — بناء Researcher Agent

---

**نهاية توثيق اليوم الثامن** ✅  
📌 *"Command وحد يساوي 10 خطوات — هاد هو الأتمتة الحقيقية"*
