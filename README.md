# 簡易RAG LLM模型

## 簡介

此專案為簡易的RAG應用。使用者可將pdf檔案放置於pdfs資料夾中，透過RAG(Retrieval-Augmented Generation)技術，讓LLM模型能根據檔案之內容，回答出更準確之答案。該範例使用之embedding模型為`bge-large-zh`；LLM模型為`mistral`。透過Streamlit製作的GUI介面，讓使用者能夠實際與模型進行對話。

# 使用步驟

1. 下載所需Python套件:

```bash
pip install ollama chromadb langchain streamlit transformers torch
```

2. 從ollama中下載LLM模型：

```bash
ollama pull mistral
```
3. 克隆此專案

```bash
git clone 
```
