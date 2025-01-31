# 簡易RAG LLM模型

## 簡介
此專案為簡易的RAG應用。使用者可將pdf檔案放置於pdfs資料夾中，透過RAG(Retrieval-Augmented Generation)技術，讓LLM模型能根據檔案之內容，回答出更準確之答案。該範例使用之embedding模型為`bge-large-zh`；LLM模型為`mistral`。透過Streamlit製作的GUI介面，讓使用者能夠實際與模型進行對話。

## 使用步驟
1. 克隆此專案
```bash
git clone https://github.com/Dodobird0218/RAG-practice.git
```
2. 下載所需Python套件:
```bash
pip install ollama chromadb langchain streamlit transformers torch
```
3. 從ollama中下載LLM模型：
```bash
ollama pull mistral
```
4. 移動至此專案資料夾
```bash
cd RAG-practice
```
5. 執行rag.py
```bash
python rag.py
```
6. 使用streamlit執行app.py
```bash
streamlit run app.py
```

## 實際demo示範

###
<img width="722" alt="demo01" src="https://github.com/user-attachments/assets/07335b05-d285-4674-a837-6837a79533ff" />

###
<img width="722" alt="demo02" src="https://github.com/user-attachments/assets/ba345e4e-c03a-4333-b518-e33aec8f268b" />
