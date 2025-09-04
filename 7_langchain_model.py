# LLM vs Chat Model
from dotenv import load_dotenv
load_dotenv() 

from langchain_openai import OpenAI, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# LLM : 주로 단일 요청에 대한 복잡한 출력을 생성하는 데 적합
# 기능 : LLM 클래스는 텍스트 문자열을 입력으로 받아 처리한 후, 텍스트 문자열을 반환합니다.
llm = OpenAI() # OpenAI는 LLM과 Chat Model 위한 별도의 API 엔드포인트를 제공합니다.

# Chat Model : 사용자와의 상호작용을 통한 연속적인 대화 관리에 더 적합
# 기능 : Chat Model 클래스는 메시지의 리스트를 입력으로 받고, 하나의 메시지를 반환합니다.
chat = ChatOpenAI(model_name="gpt-3.5-turbo-0125")
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "이 시스템은 여행 전문가 입니다."),
    ("user", "{user_input}"),
])
chain = chat_prompt | chat | StrOutputParser()

question = "한국의 대표적인 관광지 3군데를 추천해주세요."
print(f"[LLM]\n{llm.invoke(question)}\n")
print(f"[Chat prompt]\n{chain.invoke(question)}")
