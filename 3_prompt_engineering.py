# Prompt Engineering 작성하는 법
# https://platform.openai.com/docs/guides/prompt-engineering/prompt-engineering

'''
더 나은 결과를 얻기 위한 6가지 전략

1. 명확한 지침 작성 (Write clear instructions)
2. 참조 텍스트 제공 (Provide reference text)
3. 복잡한 작업을 더 간단한 하위 작업으로 나누기 (Split complex tasks into simpler subtasks)
4. 모델에게 '생각할 시간' 주기 (Give the model time to "think")
5. 외부 도구 사용 (Use external tools)
6. 체계적으로 변경 사항 테스트 (Test changes systematically)
'''

from openai import OpenAI
import os
from dotenv import load_dotenv
import time

load_dotenv()

client = OpenAI(
    api_key = os.getenv('OPENAI_API_KEY')
)

def completion(temp):
    start_time = time.time()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            # sample 1
            # {"role": "system", "content": "영어로 된 문장이 제공되며, 이를 한국어로 번역하는 것이 과제입니다."},

            # sample 2
            # {"role": "system", "content": "8세인 제시와 소통하며, 동화책을 번역해."},

            # sample 3
            {"role": "system", "content": "Interact with 8-year-old Younghee and translate a storybook as shown in the example."},
            {"role": "user", "content": "It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him."},
            {"role": "assistant", "content": "4월의 화창하고 추운날 12시였어. 스미스씨는 엄청 세게 부는 바람을 피하고 싶어서 턱을 쭉~ 내리고 빅토리 맨션으로 재빨리 들어갔지. 그런데도 어찌나 바람이 빠르게 부는지 스미스씨가 아무리 빨리 집에 들어갔어도 추위를 막지는 못했어. 으.. 엄청 추웠겠지?"},

            {"role": "user", "content": "Winston kept his back turned to the telescreen. It was safer, though, as he well knew, even a back can be revealing. A kilometre away the Ministry of Truth, his place of work, towered vast and white above the grimy landscape. This, he thought with a sort of vague distaste -- this was London, chief city of Airstrip One, itself the third most populous of the provinces of Oceania. He tried to squeeze out some childhood memory that should tell him whether London had always been quite like this. Were there always these vistas of rotting nineteenth-century houses, their sides shored up with baulks of timber, their windows patched with cardboard and their roofs with corrugated iron, their crazy garden walls sagging in all directions? And the bombed sites where the plaster dust swirled in the air and the willow-herb straggled over the heaps of rubble; and the places where the bombs had cleared a larger patch and there had sprung up sordid colonies of wooden dwellings like chicken-houses? But it was no use, he could not remember: nothing remained of his childhood except a series of bright-lit tableaux occurring against no background and mostly unintelligible."}
        ],
        temperature=0.7,
    )
    elapsed_time = time.time() - start_time
    print(f"경과 시간: {elapsed_time}초\n")
    return response.choices[0].message.content


# 응답을 출력합니다
print(completion(0))
