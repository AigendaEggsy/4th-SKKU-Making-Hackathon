# tempeature 확인
from openai import OpenAI
import os
from dotenv import load_dotenv
import time

load_dotenv()

client = OpenAI(
    api_key = os.getenv('OPENAI_API_KEY')
)

# 참고 : https://platform.openai.com/docs/api-reference/audio/createTranslation
def completion(qustion, temp):
    start_time = time.time()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role":"user", "content":qustion},
        ],
        # temperature : 생성된 텍스트의 무작위성을 조절하는 데 사용되며, 낮은 값은 보다 결정적이고 일관된 결과를, 높은 값은 더 창의적이고 예측 불가능한 결과를 낳습니다
        temperature = temp # 0 ~ 1
    )
    elapsed_time = time.time() - start_time
    print(f"경과 시간: {elapsed_time}초\n")
    return response.choices[0].message.content


# 응답을 출력합니다
question_1 = "법률 관련된 문제에 대해 가장 정확하고 상세한 설명을 해주세요. 특히 계약서 작성 시 주의해야 할 점에 대해 설명해주세요."
temp_1 = 0
print(completion(question_1, temp_1))


# Quiz 2 : 각의 질문마다 적절한 temperature를 생각해보세요

# question_2 = "최근 기술 발전에 따른 영화 산업의 변화에 대해 설명해주세요. 특히 AI 기술이 영화 제작에 어떤 영향을 미치고 있는지 구체적으로 알고 싶습니다."
# temp_2 = ?
# print(completion(question_2, temp_2))

# question_3 = "만약 달에 문명을 건설한다면, 어떤 문제들을 마주하게 될까요? 창의적이고 상상력 넘치는 시나리오를 만들어주세요."
# temp_3 = ?
# print(completion(question_3, temp_3))