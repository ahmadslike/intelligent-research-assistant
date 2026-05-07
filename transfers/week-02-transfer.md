# 🔄 Transfer Document — نهاية الأسبوع الثاني (يوم 14)

**التاريخ:** 7 مايو 2026  
**الطالب:** أحمد سليق  
**المدرّب:** Claude Sonnet 4.6

---

## 📋 معلومات ثابتة

- **النظام:** Linux Fedora (لابتوب جديد)
- **مجلد المشروع:** `/home/ahmadmvp/سطح المكتب/intelligent-research-assistant`
- **GitHub:** `https://github.com/ahmadslike/intelligent-research-assistant`
- **Stack:** Python 3.14 + FastAPI + ChromaDB + sentence-transformers + Next.js 16
- **LLM:** OpenRouter (`openrouter/free`)
- **Claude Pro:** نشط

---

## ✅ ما أنجزناه في الأسبوع الثاني (يوم 8-14)

### يوم 8: Custom Slash Commands
- أنشأنا `.claude/commands/`
- 3 commands: `/test-rag`, `/deploy-check`, `/ingest-pdf`
- `/deploy-check` اكتشف وصلّح UTF-16 تلقائياً

### يوم 9: Researcher Agent
- أول Sub-Agent في المشروع
- `ResearcherAgent` يجيب 3 مصادر (Wikipedia, Britannica, arXiv)
- فهم: Class, async/await, Pydantic models

### يوم 10: Reader + Analyst + Writer Agents
- `ReaderAgent` → يستخرج 3 نقاط من كل مصدر
- `AnalystAgent` → يحلل ويلاقي التناقضات
- `WriterAgent` → يكتب تقرير 300-500 كلمة
- Pipeline كامل شغّال في Python

### يوم 11: Skills
- `.claude/skills/academic-writer.md`
- Claude يستخدمها تلقائياً لما يكتب تقارير أكاديمية
- فهم الفرق بين Skill وSlash Command

### يوم 12: Hooks
- `.claude/hooks/safety-check.sh` → يحجب أوامر الحذف
- `.claude/hooks/auto-format.sh` → يفورمات Python تلقائياً
- `.claude/hooks/notify-done.sh` → يطبع ✅ لما يخلص
- درس: jq مش موجود على Windows/Linux → استبدلناه بـPython

### يوم 13: Pipeline متكامل
- `POST /research/full` endpoint
- 4 agents يشتغلوا مع بعض
- try/except لكل agent
- نتيجة: تقرير كامل مع مصادر

### يوم 14: Next.js Frontend
- واجهة عربية كاملة على `http://localhost:3000`
- حل مشكلة CORS
- `'use client'` لـuseState وfetch
- Full-Stack شغّال: Frontend ↔ Backend ↔ Agents ↔ RAG

---

## 📁 هيكل المشروع الحالي

```
intelligent-research-assistant/
├── backend/
│   ├── agents/
│   │   ├── researcher.py  ✅
│   │   ├── reader.py      ✅
│   │   ├── analyst.py     ✅
│   │   └── writer.py      ✅
│   ├── api/
│   │   └── research.py    ✅ (POST /research/full)
│   ├── rag/
│   │   ├── rag_engine.py  ✅
│   │   └── rag_api.py     ✅
│   └── main.py            ✅ (CORS + routers)
├── frontend/
│   └── app/
│       └── page.tsx       ✅ (واجهة عربية)
├── .claude/
│   ├── commands/          ✅ (3 commands)
│   ├── hooks/             ✅ (3 hooks)
│   └── skills/            ✅ (academic-writer)
├── docs/daily/            ✅ (14 ملف توثيق)
└── transfers/             ✅
```

---

## 🔑 أوامر مهمة على Linux/Fedora

```bash
# تفعيل venv
source venv/bin/activate.fish

# تشغيل Backend
cd backend && uvicorn main:app --reload

# تشغيل Frontend
cd frontend && npm run dev

# Git workflow
git add .
git commit -m "message"
git push

# Claude Code
claude
Shift+Tab  # Plan Mode
/mcp       # عرض MCPs
```

---

## ⚠️ تحذيرات مهمة

1. **Fish Shell** على Linux: استخدم `source venv/bin/activate.fish`
2. **CORS**: Frontend على 3000، Backend على 8000 — لازم `CORSMiddleware`
3. **openrouter/free**: النموذج الافتراضي — يختار مجاني تلقائياً
4. **لا تستخدم المفكرة** لملفات Python — UTF-16 مشكلة
5. **git push** نهاية كل يوم دائماً

---

## 📅 خطة الأسبوع الثالث (يوم 15-20)

- **يوم 15:** تحسين RAG — Chunking أذكى
- **يوم 16:** End-to-End Workflow كامل
- **يوم 17:** Error Handling + Testing
- **يوم 18:** Deployment — Railway + Vercel
- **يوم 19:** Portfolio Polish
- **يوم 20:** مراجعة شاملة + خطة المستقبل

---

**نهاية Transfer Document — الأسبوع الثاني** ✅
