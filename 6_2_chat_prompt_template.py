from dotenv import load_dotenv
import os
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

chat = ChatOpenAI(model_name=os.getenv('BASIC_GPT_MODEL'))

template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI bot."),
    ("placeholder", "{conversation}"), # placeholder를 이용하여 에시 전체를 집어 넣을 수 있음
])

chain = template | chat | StrOutputParser()

prompt_value = chain.invoke(
    {
        "conversation": [
            ("human", "안녕!"),
            ("ai", "오늘 무엇을 도와드릴까요?"),
            ("human", "아이스크림 순대 만들어 주실 수 있나요?"),
        ]
    }
)

print(prompt_value)
