# https://github.com/streamlit/docs/blob/main/python/api-examples-source/chat.llm.py
# streamlit run 12_chatbot_memory.py
import streamlit as st

from dotenv import load_dotenv
import os
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.callbacks import BaseCallbackHandler
from langchain.memory import ConversationSummaryBufferMemory

st.set_page_config(
    page_title="SKKU 메이킹 해커톤 챗봇(메모리 포함)",
    page_icon="❤️",
)

# 스트리밍 설정을 위한 callback class 설정
class ChatCallbackHandler(BaseCallbackHandler):
    message=""

    # llm이 생성되면 메서드 동작
    def on_llm_start(self, *args, **kwargs):
        self.message_box = st.empty()
    
    # llm이 끝나면 메서드 동작
    def on_llm_end(self, *args, **kwargs):
        save_message(self.message, "ai")

    # llm token이 생성될 때 메서드 동작
    def on_llm_new_token(self, token, *args, **kwargs):
        self.message += token
        self.message_box.markdown(self.message)

##################################################################
# Langchain 설정 구간
##################################################################

chat = ChatOpenAI(
    model_name=os.getenv('BASIC_GPT_MODEL'),
    temperature = 0.1,
    streaming=True, # 스트리밍 활성화
    callbacks = [ChatCallbackHandler(),] # 콜백 클래스 등록
)

# streamlit cache에 대화 memory 저장
@st.cache_resource
def init_memory(_chat):
    return ConversationSummaryBufferMemory(
        llm=_chat, max_token_limit=160, return_messages=True,
    )

memory = init_memory(chat)

# 프롬프트 입력
prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpful AI talking to a human."),
    MessagesPlaceholder(variable_name="history"),
    ("human","{question}")
])

def load_memory(*_):
    return memory.load_memory_variables({})["history"]

# LCEL
chain = (
    {
        "question": RunnablePassthrough(),
        "history": load_memory,
    }
    | prompt
    | chat
    | StrOutputParser()
)

##################################################################
# Streamlit System 구현
##################################################################

st.title("킹고스마트싱스 챗봇(메모리 포함)")

# streamlit은 새로 업데이트 될때마다 코드가 재실행됨
# 그러므로 따로 메모리를 저장해야하고 session_state에 저장
# 대화 내용을 messages라는 session_state에 저장
if "messages" not in st.session_state:
    st.session_state.messages = []

# 대화 내용을 저장하는 함수
def save_message(message, role):
    st.session_state["messages"].append({"message": message, "role": role})

# 단일 대화 내용을 출력하는 함수
def send_message(message, role, save=True):
    with st.chat_message(role):
        st.markdown(message)
    # save=True일 때, 동시에 대화 내용 저장
    if save:
        save_message(message, role)

# 대화 내용을 출력하는 함수
def paint_history():
    # messages라는 session_state에 있는 대화내용 모두 출력하는 함수
    for message in st.session_state["messages"]:
        send_message(message["message"], message["role"], save=False,)

##################################################################
# Streamlit UI 구현
##################################################################

# 지금까지 대화 내용 출력
paint_history()

# 질문이 입력되면 동작
if question := st.chat_input("질문을 입력하세요..."):
    # user(사용자가 등록한 내용)라는 role로 대화 내용 출력 및 저장
    send_message(question, "user", save=True)
    
    # ai(llm 출력)라는 role로 대화 내용 출력(실시간 스트리밍) 및 저장
    with st.chat_message("ai"):
        result = chain.invoke(question)
        memory.save_context(
            {"input": question},
            {"output": result}
        )