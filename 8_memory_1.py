# memory (ConversationBufferMemory)
from dotenv import load_dotenv
import os
load_dotenv() 

from langchain_openai import ChatOpenAI
# ConversationChain: 대화 체인을 관리하는 데 사용
# https://python.langchain.com/docs/modules/chains/popular/conversation
from langchain.chains import ConversationChain
# ConversationBufferMemory : 대화 중 생성된 메모리를 관리
from langchain.memory import ConversationBufferMemory

chat = ChatOpenAI(model_name=os.getenv('BASIC_GPT_MODEL'))

print("=== 직접 LLM 호출 (메모리 없음) ===")
print(chat.invoke("전 세계의 인구가 많은 상위 3개 국가는?").content)
print(chat.invoke("그 다음 3개 국가는?").content)

print("\n" + "="*100)

# 대화 체인 설정
conversation = ConversationChain(llm=chat, memory=ConversationBufferMemory())

print("[first question]")
print(conversation.invoke("전 세계의 인구가 많은 상위 3개 국가는?")['response'])

print("\n[second question]")
print(conversation.invoke("그 다음 3개 국가는?")['response'])

print("\n[third question]")
print(conversation.invoke("이전 답변을 깔끔하게 요약해줘")['response'])

print("\n[memory]")
print(conversation.memory.load_memory_variables({}))