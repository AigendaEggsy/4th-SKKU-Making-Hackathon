# Multi Chain
from dotenv import load_dotenv
import os
load_dotenv() 

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.callbacks import StreamingStdOutCallbackHandler  # 최신 경로

# 첫 번째 체인: 한국어 → 영어 번역
chat1 = ChatOpenAI(
    model_name=os.getenv('BASIC_GPT_MODEL'),
    temperature = 0.1,
)

prompt1 = ChatPromptTemplate.from_template("translates {korean_word} to English.")

chain1 = prompt1 | chat1 | StrOutputParser()

# 두 번째 체인: 영어 단어 → 옥스퍼드 사전 설명
chat2 = ChatOpenAI(
    model_name=os.getenv('BASIC_GPT_MODEL'),
    temperature = 0.1,
    # 스트리밍 활성화
    streaming=True,
    callbacks = [StreamingStdOutCallbackHandler()]
)

prompt2 = ChatPromptTemplate.from_template(
    "explain {english_word} using oxford dictionary to me in Korean."
)

chain2 = (
    {"english_word": chain1}
    | prompt2
    | chat2
    | StrOutputParser()
)

print(chain2.invoke({"korean_word":"미래"}))