import streamlit as st
from rag import RAG

# 初始化 RAG
rag = RAG()

# 頁面標題
st.title("📚 RAG Demo")
st.markdown("上傳 PDF 並透過 LLM 進行智能問答")

# 使用者輸入問題
user_input = st.text_input("輸入你的問題", "")

# 按鈕觸發查詢
if st.button("查詢"):
    if user_input:
        with st.spinner("正在檢索並生成回應..."):
            try:
                answer = rag.generate_response(user_input)
                st.subheader("回答：")
                st.write(answer)
            except Exception as e:
                st.error(f"發生錯誤: {e}")
    else:
        st.warning("請輸入問題後再進行查詢！")
