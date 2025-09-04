from dotenv import load_dotenv
load_dotenv() 

# https://python.langchain.com/docs/modules/memory/types/summary_buffer/
from langchain.memory import ConversationSummaryBufferMemory
from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

chat = ChatOpenAI(model_name="gpt-3.5-turbo-0125",)

memory = ConversationSummaryBufferMemory(
    llm = chat, # LLM 설정
    max_token_limit=160, # 데이저 저장 Max 값 설정
    return_messages = True, # 결과값을 출력할지 설정, 기본 false 
)

prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpful AI talking to a human."),
    MessagesPlaceholder(variable_name="history"), # 변수가 이미 메시지 목록이라고 가정하는 프롬프트 템플릿
    ("human","{question}")
])

# invoke시 값이 자동으로 전달되므로 input을 반드시 선언해야 함
def load_memory(*_):
    return memory.load_memory_variables({})["history"]

# RunnablePassthrough : 입력된 데이터를 그대로 반환, 데이터를 변경하지 않고 파이프라인의 다음 단계로 전달하는 데 사용
# assign과 함께 호출된 RunnablePassthrough(RunnablePassthrough.assign(...))는 입력을 받아 assign 함수에 전달된 추가 인자
# 참고 : https://velog.io/@udonehn/LangChain%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC-%EC%B1%97%EB%B4%87-%EB%B0%98%EB%93%A4%EA%B8%B0#%EC%B2%B4%EC%9D%B8%EC%9D%98-%ED%9D%90%EB%A6%84
chain = RunnablePassthrough.assign(history=load_memory) | prompt | chat | StrOutputParser()
def invoke_chain(question):
    result = chain.invoke({"question": question})
    # 메모리에 저장, Max token이 넘을 시 요약해서 저장
    memory.save_context(
        {"input": question}, # 입력 질문 저장
        {"output": result} # 출력 내용 저장
    )
    # 메모리에 저장된 내용 출력
    # print(memory.load_memory_variables({})["history"])
    return result

print(invoke_chain("너는 누구야?"))
print(invoke_chain("내연기관 자동차를 만드는 방법에 대해서 설명해"))
print(invoke_chain("전기차하고 다른점은 뭐야?"))
print(invoke_chain("조금전에 이야기 한 것들을 한줄로 요약해"))