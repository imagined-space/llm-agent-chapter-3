# 传统RAG的简单实现
def basic_rag(query, documents):
    # 1. 简单文本分割
    chunks = simple_text_split(documents)
    
    # 2. 向量化
    embeddings = embed_texts(chunks)
    
    # 3. 相似度检索
    relevant_chunks = similarity_search(query, embeddings, top_k=5)
    
    # 4. 简单问答
    context = "\n".join(relevant_chunks)
    response = llm.complete(f"Context: {context}\nQuestion: {query}")
    
    return response