# gpt api 사용하기
from openai import OpenAI
import os
from dotenv import load_dotenv
import time

load_dotenv() # .env 파일 정보 불러오기

# 클라이언트 인스턴스를 생성하고 API 키를 환경변수에서 가져옵니다
client = OpenAI(
    api_key = os.getenv('OPENAI_API_KEY')
)

# 대화 생성 요청을 보내고 응답을 받습니다
# 참고 : https://platform.openai.com/docs/api-reference/making-requests
def completion():
    start_time = time.time()
    response = client.chat.completions.create(
        # 참고 : https://platform.openai.com/docs/models/overview
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role":"system", "content":"너는 슈퍼마리오브라더스에 나오는 마리오야. 항상 마리오처럼 대답해. 그리고 모든 답변은 한국어로 해"},
            {"role":"user", "content":"너의 삶의 목표는 뭐야?"}
        ],
    )
    elapsed_time = time.time() - start_time
    print(f"경과 시간: {elapsed_time}초\n")
    return response

# 응답을 출력합니다
print(completion().choices[0].message.content)

# Quiz 1 : 응답(content)만을 출력하게 하세요
# print("정답을 적으시오")