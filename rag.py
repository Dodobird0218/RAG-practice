import os
import ollama
import chromadb
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

class RAG:
    def __init__(self, pdf_folder="pdfs", db_folder="db"):
        self.pdf_folder = pdf_folder
        self.db_folder = db_folder

        # 使用中文嵌入模型，這裡以 `bge-large-zh` 為例
        self.embedding_model = HuggingFaceEmbeddings(model_name="BAAI/bge-large-zh")

        # 初始化 ChromaDB 向量資料庫
        self.vectorstore = Chroma(persist_directory=self.db_folder, embedding_function=self.embedding_model)

        # 初始化 Ollama Mistral 模型
        self.llm_model = "mistral"  # Ollama 的 Mistral 模型

    def load_pdfs(self):
        """載入並處理 PDF 檔案，存入向量資料庫"""
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        
        for file in os.listdir(self.pdf_folder):
            if file.endswith(".pdf"):
                loader = PyPDFLoader(os.path.join(self.pdf_folder, file))
                docs = loader.load()
                texts = text_splitter.split_documents(docs)

                # 儲存文本並計算嵌入
                documents = [text.page_content for text in texts]
                self.vectorstore.add_texts(texts=documents, metadatas=[{"source": file} for _ in texts])

        print("✅ PDF 資料載入完成！")

    def retrieve(self, query):
        """根據問題檢索最相關的內容"""
        results = self.vectorstore.similarity_search(query, k=3)
        return [f"{doc.metadata['source']}: {doc.page_content}" for doc in results]

    def generate_response(self, query):
        """使用 Ollama Mistral 模型生成回應"""
        context = "\n".join(self.retrieve(query))
        prompt = f"根據以下資訊回答問題：\n{context}\n\n問題：{query}\n回答："

        # 使用 Ollama LLM 生成回應
        response = ollama.chat(model=self.llm_model, messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]

if __name__ == "__main__":
    rag = RAG()
    rag.load_pdfs()  # 初始化時載入 PDF
