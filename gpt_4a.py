import openai

# OpenAI API 키 설정
openai.api_key = "your_api_key_here"  # 여기에 자신의 OpenAI API 키를 입력하세요.

def get_recipe(ingredients, chef_level, cuisine_type):
    # 입력 검증
    if not chef_level:
        return "요리 수준을 입력해주세요!"
    if not cuisine_type:
        return "요리 분야를 입력해주세요!"
    
    # 시스템 프롬프트 설정
    system_prompt = (
        "너는 요리 전문가야. "
        "다음과 같은 형식으로 1번부터 4번까지 응답 출력해줘:\n"
        "1. 재료\n"
        "2. 조리 방법\n"
        "3. 영양정보\n"
        "    a. 알러지 정보\n"
        "    b. 영양분\n"
        "    c. 칼로리\n"
        "4. 조리시간\n"
        "재료와 조리 방법이 너무 길지 않게 간단하게 설명해줘."
    )
    
    # 유저 프롬프트 생성
    user_prompt = (
        f"내가 냉장고에 {', '.join(ingredients)}이 있는데 "
        f"이걸로 {chef_level} 수준의 {cuisine_type} 레시피 추천해줘."
    )
    
    # API 요청
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=300,  # 응답의 최대 길이
        temperature=0.7,  # 다양성을 조절하는 온도 값
        top_p=1.0,       # 생성의 확률 분포를 조정
    )
    
    # 응답 추출
    return response['choices'][0]['message']['content']

# 입력 예시
ingredients = ["양파", "달걀", "간장", "고춧가루"]
chef_level = "초급자"
cuisine_type = "한식"

# 레시피 생성
recipe = get_recipe(ingredients, chef_level, cuisine_type)
print(recipe)
