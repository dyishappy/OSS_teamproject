import gradio as gr
from vicuna_2a import generate_recipe
from gpt_4a import get_recipe

# Gradio 인터페이스 구성
iface = gr.Interface(
    fn=get_recipe,
    inputs=[
        gr.Textbox(label="요리 재료 (ingredients)", placeholder="예: 계란, 우유, 당근"),
        gr.Dropdown(choices=["한식", "중식", "양식", "디저트"], label="요리 종류 (cuisine_type)", value="한식"),
        gr.Radio(choices=["초보", "중급", "고급"], label="조리자 수준 (chef_level)", value="초보")
    ],
    outputs=gr.Textbox(label="추천 레시피"),
    title="Take care of the fridge!",
    description="입력한 요리 재료, 요리 종류, 조리자 수준에 따라 맞춤 레시피를 추천합니다."
)

iface.launch()