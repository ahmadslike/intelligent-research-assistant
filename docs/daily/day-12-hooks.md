# 📘 ملف تعلّم Claude Code — اليوم الثاني عشر

**الطالب:** أحمد سليق  
**المدرّب:** Claude Sonnet 4.6  
**اليوم:** اليوم الثاني عشر — Hooks  
**التاريخ:** 4 مايو 2026  
**المدة الفعلية:** ~2 ساعة  
**تقييم اليوم:** 9/10

---

## 🎯 شو تعلمنا اليوم؟

تعلمنا Hooks — أكواد تشتغل تلقائياً قبل أو بعد كل عملية في Claude Code.

---

## 📚 المفاهيم بالتفصيل

### 1. شو هو Hook؟

Hook = "خطّاف" — كود يشتغل تلقائياً في لحظة معينة.

مثال من الحياة:
- قبل ما تخرج من البيت → تتحقق من المفاتيح (PreToolUse)
- بعد ما تطبخ → تغسل الأواني (PostToolUse)
- لما تنام → تطفئ الأضواء (Stop)

### 2. أنواع الـHooks

```
PreToolUse  → يشتغل قبل ما Claude ينفّذ أمر
              يقدر يوقف الأمر (exit 2 = block)
              
PostToolUse → يشتغل بعد ما Claude ينفّذ أمر
              يعدّل النتيجة (مثل format الكود)
              
Stop        → يشتغل لما Claude يخلص كل شي
              مفيد للإشعارات
```

### 3. كيف تشتغل الـHooks؟

```
Claude يريد ينفّذ أمر
        ↓
PreToolUse Hook يشتغل
        ↓
لو exit 0 → Claude ينفّذ الأمر
لو exit 2 → Claude يوقف ويطلع خطأ
        ↓
الأمر ينفّذ
        ↓
PostToolUse Hook يشتغل
```

---

## 🛠️ الـHooks اللي بنيناها

### 1. safety-check.sh (PreToolUse)

**مهمته:** يحجب أوامر الحذف

```bash
# يقرأ الأمر من الـJSON
COMMAND=$(... python ...)

# لو الأمر يحتوي على rm أو del أو Remove-Item
if BLOCK; then
  # يرجع رسالة خطأ ويوقف
  exit 2
fi
```

**درس مهم:** في البداية حجب الـcommit لأن رسالته احتوت على "Remove-Item"!
Claude حسّن الـhook ليفرق بين **أمر حقيقي** ونص عادي — هاد مثال على Bug حقيقي وحله.

### 2. auto-format.sh (PostToolUse)

**مهمته:** يفورمات ملفات Python تلقائياً بعد كل كتابة

```bash
# يقرأ اسم الملف
FILE=$(... python ...)

# لو الملف .py
if [[ "$FILE" == *.py ]]; then
  python -m black "$FILE"  # فورمات تلقائي
fi
```

**شو يعمل black؟**
```python
# قبل
def greet(name,age):
    print(   "Hello "+name   )
x={"key":"value"}

# بعد (تلقائياً)
def greet(name, age):
    print("Hello " + name)

x = {"key": "value"}
```

### 3. notify-done.sh (Stop)

**مهمته:** يطبع رسالة لما Claude يخلص

```bash
echo "✅ Task complete!" >&2
```

بسيط بس مفيد — تعرف لما Claude خلص مهمة طويلة.

---

## 📁 هيكل الـHooks

```
.claude/
├── hooks/
│   ├── safety-check.sh   ← PreToolUse
│   ├── auto-format.sh    ← PostToolUse
│   └── notify-done.sh    ← Stop
└── settings.json         ← يربط كل شي
```

**settings.json** هو اللي يخبر Claude Code متى يشغّل أي hook:

```json
{
  "hooks": {
    "PreToolUse": [{"matcher": "Bash", "hooks": [...]}],
    "PostToolUse": [{"matcher": "Write|Edit", "hooks": [...]}],
    "Stop": [{"matcher": "*", "hooks": [...]}]
  }
}
```

---

## 🐛 المشاكل اللي واجهناها

**المشكلة 1:** `jq: command not found`  
**السبب:** `jq` أداة Linux مش موجودة على Windows  
**الحل:** استبدلناها بـPython (موجود عندنا دائماً)

**المشكلة 2:** safety-check حجب الـcommit  
**السبب:** رسالة الـcommit احتوت على "Remove-Item" فالـhook اعتقد إنه أمر حذف  
**الحل:** Claude حسّن الـhook ليفرق بين أمر حقيقي ونص عادي  
**الدرس:** الـHooks قوية — لازم تكون ذكية مش بس تبحث عن كلمات

---

## 🧠 أسئلة الاختبار + الأجوبة

**س1:** شو الفرق بين PreToolUse وPostToolUse؟  
**ج:** Pre = قبل التنفيذ (يقدر يوقف)، Post = بعد التنفيذ (يعدّل) ✅

**س2:** ليش حجب الـhook الـcommit في البداية؟  
**ج:** رسالة الـcommit احتوت على "Remove-Item" فظنّه أمر حذف ✅

**س3:** شو يعمل auto-format؟  
**ج:** يزبط شكل الكود والمسافات تلقائياً بعد كل كتابة ✅

---

## 📊 ملخص سريع

| Hook | متى يشتغل | شو يعمل |
|------|----------|---------|
| safety-check | قبل Bash | يحجب الحذف |
| auto-format | بعد Write/Edit | يفورمات Python |
| notify-done | لما يخلص | يطبع ✅ |

---

## 📅 التحضير ليوم 13

**موضوع يوم 13:** ربط كل شي في pipeline متكامل

---

**نهاية توثيق اليوم الثاني عشر** ✅  
📌 *"Hooks = الحارس الذكي الذي لا ينام"*
