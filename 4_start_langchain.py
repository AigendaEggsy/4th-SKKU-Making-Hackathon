# Langchain 시작하기
# 참고 : https://python.langchain.com/docs/get_started/quickstart/
from dotenv import load_dotenv
load_dotenv() 

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate # 프롬프트 생성하는 클래스
from langchain_core.output_parsers import StrOutputParser # 모델의 출력을 문자열로 표시

quesion = "지구는 태양 주변을 왜 공전해?"

# llm 설정
chat = ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature = 0.1)

# llm 호출
print(chat.invoke(quesion).content)

print("="*100)

# 프롬프트를 정의
prompt = ChatPromptTemplate.from_template("당신은 천문학 전문가입니다. 질문에 과학적 원리를 근거하여 자세하게 설명해줘 <Question>: {input}")

# chain 연결 (LCEL)
# LCEL Chaining 기본 형태: Prompt + Model + Output Parser
# 참고 : https://python.langchain.com/docs/expression_language/
chain = prompt | chat | StrOutputParser()

# chain 호출
print(chain.invoke({"input": quesion}))


