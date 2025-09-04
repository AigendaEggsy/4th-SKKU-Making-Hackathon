# memory (ConversationBufferWindowMemory)
from dotenv import load_dotenv
load_dotenv() 

from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory

chat = ChatOpenAI(model_name="gpt-3.5-turbo-0125")

# 참고 : https://python.langchain.com/docs/modules/memory/types/buffer_window/
conversation = ConversationChain(llm=chat, memory=ConversationBufferWindowMemory(k=3,))
print("[first question]")
print(conversation.invoke("뉴진스 맴버 1명 말해봐")['response'])

print("\n[second question]")
print(conversation.invoke("다른 1명 더 말해봐")['response'])

print("\n[third question]")
print(conversation.invoke("다른 1명 더 말해봐")['response'])

print("\n[fourth question]")
print(conversation.invoke("지금까지 말한 맴버 이름 말해봐")['response'])

print("\n[memory]")
print(conversation.memory.load_memory_variables({}))


