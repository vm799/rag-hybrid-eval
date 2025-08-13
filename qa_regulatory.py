# qa_regulatory.py
import os
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

OUT_DIR = "chroma_regulatory"
EMB_MODEL = os.getenv("EMB_MODEL", "all-MiniLM-L6-v2")
USE_OPENAI = os.getenv("USE_OPENAI", "true").lower() == "true"

def get_llm():
    if USE_OPENAI:
        # requires OPENAI_API_KEY in env
        model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        return ChatOpenAI(temperature=0, model_name=model_name)
    else:
        # Placeholder: implement local-model client (e.g., Ollama wrapper) if needed
        raise RuntimeError("Non-OpenAI local model path not implemented. Set USE_OPENAI=true and OPENAI_API_KEY.")

def main():
    if not os.path.isdir(OUT_DIR):
        print(f"Vector DB directory {OUT_DIR} not found. Run ingest first.")
        return

    embeddings = SentenceTransformerEmbeddings(model_name=EMB_MODEL)
    vectordb = Chroma(persist_directory=OUT_DIR, embedding_function=embeddings)
    retriever = vectordb.as_retriever(search_kwargs={"k": 6})

    llm = get_llm()
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

    print("Regulatory QA ready. Type a question (ctrl-c to exit).")
    while True:
        q = input("\n> ")
        if not q.strip():
            continue
        ans = qa.run(q)
        print("\n---\n", ans, "\n---\n")

if __name__ == "__main__":
    main()
