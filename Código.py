!pip install gradio transformers pillow

import gradio as gr
from transformers import pipeline

classifier = pipeline("image-classification")

def classify(img):
    result = classifier(img)
    return result

demo = gr.Interface(
    fn=classify,
    inputs=gr.Image(type="pil"),
    outputs="json",
    title="Clasificador de Productos por Imagen"
)

demo.launch()
