from langchain_openai import ChatOpenAI

def main():
    # 初始化模型并提供秘钥
    llm = ChatOpenAI(openai_api_key="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")

    llm.invoke("how can langsmith help with testing?")

if __name__ == "__main__":
  main()

# nihao
