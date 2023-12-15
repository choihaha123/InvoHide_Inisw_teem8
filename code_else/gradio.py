import gradio as gr
import cv2
import numpy as np

# 임의의 마스킹 함수 정의 (실제 모델을 여기에 연결)
def mask_image(image):
    return image

with gr.Blocks(title="Privacy Mask", css="footer{display:none !important}") as demo:
    gr.Markdown(
    """
    ## Invoice Info Auto-Masking Service
    # InvoHide
    ### Simply Protect your private informations in Invoice Image
    """)
    with gr.Row():
        image_input = gr.Image()
        #image_output = gr.Image() # download [ok]
        image_output = gr.Image(
                show_download_button=True
            )
    image_button = gr.Button("masking")
    image_button.click(
        mask_image,
        inputs=image_input,
        outputs=image_output
    )
demo.launch()