# Multi Chain
from dotenv import load_dotenv
load_dotenv() 

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.callbacks import StreamingStdOutCallbackHandler # 스트리밍 하는 메서드

chat1 = ChatOpenAI(
    model_name="gpt-3.5-turbo-0125",
    temperature = 0.1,
)

prompt1 = ChatPromptTemplate.from_template("translates {korean_word} to English.")

chain1 = prompt1 | chat1 | StrOutputParser()

chat2 = ChatOpenAI(
    model_name="gpt-4-turbo",
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