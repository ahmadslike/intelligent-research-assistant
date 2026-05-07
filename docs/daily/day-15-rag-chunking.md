# 📘 ملف تعلّم Claude Code — اليوم الخامس عشر

**الطالب:** أحمد سليق  
**المدرّب:** Claude Sonnet 4.6  
**اليوم:** اليوم الخامس عشر — تحسين RAG بـChunking  
**التاريخ:** 7 مايو 2026  
**المدة الفعلية:** ~2 ساعة  
**تقييم اليوم:** 9/10

---

## 🎯 شو تعلمنا اليوم؟

تعلمنا كيف نحسّن نظام RAG بتقسيم النصوص الطويلة لأجزاء صغيرة قبل التخزين.

---

## 📚 المفاهيم بالتفصيل

### 1. شو هو Chunking وليش مهم؟

**المشكلة:**
لو رفعت مستند 500 صفحة وحفظته كـembedding وحد — البحث يقارن سؤالك بمعنى 500 صفحة كلها. النتيجة؟ ضبابية وغير دقيقة.

**الحل (Chunking):**
تقسيم المستند لأجزاء ~200 كلمة وكل جزء يتحفظ كـembedding مستقل.

```
مستند 500 صفحة
        ↓
chunk 1: الصفحات 1-2   → embedding 1
chunk 2: الصفحات 2-3   → embedding 2  (مع overlap)
chunk 3: الصفحات 3-4   → embedding 3
...
        ↓
البحث يرجع الـchunk الأدق مش المستند كله
```

---

### 2. شو هو Overlap وليش 20 كلمة؟

Overlap = تداخل بين الـchunks — آخر 20 كلمة من chunk يكونوا أول 20 كلمة في الـchunk التالي.

**ليش مهم؟**
لو جملة مهمة وقعت على الحدود بين chunk وثاني:

```
...هذا هو المفهوم الأساسي | في علم الذكاء الاصطناعي...
                          ↑
                      حد الـchunk
```

بدون overlap → الجملة تتقسم وتضيع معناها
مع overlap → الجملة موجودة كاملة في كلا الـchunks

---

### 3. شو أضفنا بالضبط؟

**3 دوال جديدة في `rag_engine.py`:**

```python
# الدالة 1: تقسيم النص
def chunk_text(text, chunk_size=200, overlap=20):
    words = text.split()
    if not words: return []
    if len(words) <= chunk_size: return [text]
    step = chunk_size - overlap  # 180 كلمة خطوة
    chunks = []
    for i in range(0, len(words), step):
        chunk = ' '.join(words[i: i + chunk_size])
        chunks.append(chunk)
        if i + chunk_size >= len(words): break
    return chunks

# الدالة 2: تخزين مع chunking
def add_document_chunked(doc_id, text, metadata=None):
    metadata = metadata or {}
    chunks = chunk_text(text)
    # بناء كل البيانات دفعة وحدة (batch)
    ids = [f"{doc_id}_chunk_{i}" for i in range(len(chunks))]
    # كل chunk عنده metadata خاص فيه
    # chunk_index: رقم الـchunk
    # total_chunks: العدد الكلي
    # parent_doc_id: المستند الأصلي
    collection.add(ids=ids, embeddings=embeddings, 
                   documents=chunks, metadatas=metadatas)
    return {"status": "added", "total_chunks": len(chunks)}

# الدالة 3: بحث محسّن
def search_chunked_documents(query, n_results=3):
    qe = model.encode(query).tolist()
    raw = collection.query(query_embeddings=[qe], n_results=n_results)
    # يرجع list مرتّبة بدل nested lists
    return [
        {"text": doc, "metadata": meta, "distance": dist}
        for doc, meta, dist in zip(raw["documents"][0], 
                                    raw["metadatas"][0], 
                                    raw["distances"][0])
    ]
```

---

### 4. ليش أضفنا دوال جديدة بدل تعديل القديمة؟

**مبدأ مهم: "Open/Closed Principle"**

```
الكود القديم: add_document + search_documents
    ↓ يستخدمها: /rag/add, /rag/search, /rag/count endpoints
    ↓ لو عدّلناها → ممكن نكسر هاي الـendpoints

الكود الجديد: add_document_chunked + search_chunked_documents
    ↓ مستقلة تماماً
    ↓ ما تؤثر على القديم
```

**القاعدة:** أضف، لا تعدّل — أأمن وأضمن.

---

### 5. نتيجة الاختبار

```
Syntax OK ✅
chunk_text tests passed ✅
500-word text → 3 chunks ✅
overlap مضمون بين الـchunks ✅
```

---

## 🧠 أسئلة الاختبار + الأجوبة

**س1:** شو هو Chunking وليش مهم؟  
**ج:** تقسيم نص طويل لأجزاء صغيرة — البحث يرجع الجزء الأدق مش المستند كله ✅

**س2:** شو يعني 20 كلمة overlap؟  
**ج:** تداخل يضمن إن الجمل على الحدود موجودة في كلا الـchunks ✅

**س3:** ليش أضفنا دوال جديدة؟  
**ج:** عشان ما نكسر الـendpoints الموجودة — أضف ولا تعدّل ✅

---

## 📅 التحضير ليوم 16

**موضوع يوم 16:** End-to-End Workflow كامل + تحسينات

---

**نهاية توثيق اليوم الخامس عشر** ✅  
📌 *"أضف ولا تعدّل — القاعدة الذهبية للكود الآمن"*
