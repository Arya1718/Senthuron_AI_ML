# Senthuron AI Text Summarizer & Keyword Extractor

This project provides a simple and efficient pipeline to:
- Summarize any given text into exactly **3 bullet points**
- Extract the **top N keywords** using deep learning

Built using powerful libraries like:
- [Transformers](https://huggingface.co/transformers/) by HuggingFace for summarization
- [KeyBERT](https://github.com/MaartenGr/KeyBERT) for keyword extraction

---

## 🚀 Features

- ✅ Clean and preprocess input text
- ✅ Summarize long paragraphs into **3 concise bullet points**
- ✅ Extract **top keywords** using BERT embeddings
- ✅ Handles short input gracefully with friendly warnings

---

## 📦 Requirements

Install dependencies using pip:

```bash
pip install transformers keybert sentence-transformers --quiet
