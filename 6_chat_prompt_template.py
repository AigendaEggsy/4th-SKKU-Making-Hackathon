# 6. ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv() 

from langchain_openai import ChatOpenAI
# 참고 : https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html
from langchain_core.prompts import ChatPromptTemplate # 챗 프롬프트 생성하는 클래스
from langchain_core.output_parsers import StrOutputParser

chat = ChatOpenAI(model_name="gpt-3.5-turbo-0125")

# template이라는 변수에 ChatPromptTemplate 인스턴스를 집어넣고 from_messages라는 메서드를 통해 채팅용 프롬프트를 작성
template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a geography expert. And you only reply in {language}."), # 모델에게 사람이 지시하는 메시지
        ("ai", "Hi my name is {name}!"), # AI의 출력 메시지
        ("human", "What is the distance between {country_a} and {country_b}. Also, what is your name?"), # 사람이 입력하는 메시지
    ]
)

# template.format_messages : 사용자의 입력을 프롬프트에 동적으로 삽입하여, 최종적으로 대화형 상황을 반영한 메시지 리스트를 생성
prompt = template.format_messages(
    language = "Korean",
    name = "Hyoin",
    country_a = "Korea",
    country_b = "USA"
)

print(f"\n[template]\n{template}\n")
print(f"[prompt]\n{prompt}\n\n")
print(chat.invoke(prompt).content)

# Quiz : LCEL Chaining을 사용해서 결과 작성하기


