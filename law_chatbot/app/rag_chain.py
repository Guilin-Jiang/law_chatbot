import ollama
import faiss
import numpy as np
import requests
import os
from transformers import AutoTokenizer, AutoModel
from . import load_documents

# 加载 HuggingFace 嵌入模型
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def encode_text(texts):
    inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
    embeddings = model(**inputs).last_hidden_state.mean(dim=1)
    return embeddings.detach().numpy()

# 使用 Ollama 运行 Llama 模型
def get_answer(query):
    host = os.getenv("OLLAMA_HOST", "http://host.docker.internal:11434")
    model_mistral = os.getenv("OLLAMA_MODEL", "mistral")

    url = f"{host}/api/chat"

    payload = {
        "model": model_mistral,
        "messages": [
            {"role": "user", "content": query}
        ],
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("Ollama response:")
        print(response.text)

        data = response.json()  # ⚠️ 出错点
        return data["message"]["content"]
    
    except requests.exceptions.RequestException as e:
        print("Ollama 请求失败:", e)
        return "抱歉，无法连接 Ollama下的mistral 模型。"

# 构建 RAG chain
def retrieve_and_generate(query):
    # 从数据库加载文件并进行嵌入
    documents = load_documents.load_pdf_documents("data/legal_documents.pdf")
    document_chunks = [doc['text'] for doc in documents]
    document_embeddings = encode_text(document_chunks)

    # 使用 FAISS 索引进行检索
    index = faiss.IndexFlatL2(document_embeddings.shape[1])
    index.add(document_embeddings)

    query_embedding = encode_text([query])
    _, I = index.search(query_embedding, k=1)

    # 返回最相似的段落
    similar_paragraph = document_chunks[I[0][0]]

    # 通过 Llama 模型生成回答
    answer = get_answer(f"请根据以下段落来回答问题: {similar_paragraph[:500]} 问题: {query}")
    return answer
