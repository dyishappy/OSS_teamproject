from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# 모델과 토크나이저 로드
tokenizer = AutoTokenizer.from_pretrained("lmsys/vicuna-7b-v1.5")
model = AutoModelForCausalLM.from_pretrained("lmsys/vicuna-7b-v1.5")

# 모델을 GPU로 이동
device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

def generate_recipe(ingredients, cuisine_type, chef_level):
    # 재료가 없을 경우 대체 텍스트 설정
    if not ingredients or '없음' in ingredients:
        ingredients_text = "재료에 상관없이"
    else:
        ingredients_text = f"{', '.join(ingredients)}로"

    # 시스템 프롬프트 동적 생성
    system_prompt = (
        f"{ingredients_text} {chef_level} 수준의 {cuisine_type} 요리 레시피를 추천해드릴게요~\n"
        "1. 재료\n"
        "\n"
        "2. 조리 방법\n"
        "\n"
        "3. 영양정보\n"
        "    a. 알러지 정보\n"
        "    b. 영양분\n"
        "    c. 칼로리\n"
        "\n"
        "4. 조리시간\n"
    )
    
    # 사용자 입력 처리
    if not ingredients or '없음' in ingredients:
        user_input = (
            f"재료에 상관없이 {chef_level} 수준의 {cuisine_type} 요리 레시피를 추천해줘."
        )
    else:
        user_input = (
            f"내가 냉장고에 {', '.join(ingredients)}이 있는데 "
            f"{chef_level} 수준의 {cuisine_type} 요리 레시피 알려줘."
        )
    
    # 최종 프롬프트 생성
    prompt = f"{system_prompt}\nUser: {user_input}\nAssistant:"
    
    # 입력 텍스트 토크나이즈
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    
    # 모델로부터 응답 생성
    outputs = model.generate(
        inputs["input_ids"],
        max_length=1024,  # 생성될 응답의 최대 길이
        do_sample=True,  # 샘플링 활성화
        top_k=50,        # top-k 샘플링
        temperature=0.7  # 생성 다양성을 조절하는 온도 값
    )
    
    # 생성된 텍스트 디코딩
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # 불필요한 텍스트 제거 및 형식 유지
    response = response.replace(system_prompt.strip(), "").strip()
    return response

if __name__ == "__main__":

    # 입력 예시임. 본 코드에선 입력값 받아서 사용
    ingredients = ["양송이 버섯", "된장", "고추장", "마늘", "새우"]
    cuisine_type = "양식"
    chef_level = "초보자"

    # 레시피 생성
    recipe = generate_recipe(ingredients, cuisine_type, chef_level)

    # 응답 전처리: 'Assistant:' 이후 텍스트만 남기기
    if "Assistant:" in recipe:
        recipe = recipe.split("Assistant:", 1)[1].strip()

    print(recipe) # 확인용임. 본 코드에선 recipe 반완 값 받아서 사용
