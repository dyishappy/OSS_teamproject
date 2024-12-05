import gradio as gr

# 1. Vicuna 기반 함수
def recommend_vicuna(ingredients, cuisine_type, chef_level):
    # Vicuna 모델 호출 (여기서는 예제 텍스트로 대체)
    # 실제 Vicuna 호출 코드는 모델 및 환경에 따라 다르게 구성됩니다.
    return (
        f"Vicuna 모델 응답\n\n"
        f"재료: {ingredients}\n"
        f"요리 종류: {cuisine_type}\n"
        f"조리자 수준: {chef_level}\n\n"
        f"추가 재료: 소금, 후추\n"
        f"조리 방법: 팬을 달군 후 재료를 볶습니다.\n"
        f"조리 시간: 20분"
    )


# Gradio 인터페이스 구성
iface = gr.Interface(
    fn=recommend_vicuna,
    inputs=[
        gr.Textbox(label="요리 재료 (ingredients)", placeholder="예: 계란, 우유, 당근"),
        gr.Dropdown(choices=["한식", "중식", "양식", "디저트"], label="요리 종류 (cuisine_type)", value="한식"),
        gr.Radio(choices=["초보", "중급", "고급"], label="조리자 수준 (chef_level)", value="초보")
    ],
    outputs=gr.Textbox(label="추천 레시피", lines=10),
    title="Take care of the fridge!",
    description="입력한 요리 재료, 요리 종류, 조리자 수준에 따라 맞춤 레시피를 추천합니다."
)

iface.launch()
