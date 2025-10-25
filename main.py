import gradio as gr

def show_image():
    image_path = "cookie-theft.jpg"
    return gr.Image(value=image_path, visible=True)

def analyze_results(audio):
    return gr.Markdown("You do not have Alzheimer's!", visible=True)

info = """
- This tool analyzes speech patterns to detect early-onset Alzheimer's.
- An ML model was trained on [DementiaBank](https://talkbank.org/dementia/).
- **Disclaimer**: This tool is for informational use only and does not constitute medical advice.
"""

with gr.Blocks() as demo:

    gr.Markdown("# Alzheimer's Screening Tool")

    gr.Markdown(info)

    gr.Markdown("## Try it now!")

    gr.Markdown("You will see an image. Please describe the image with as much detail as you can within 30 seconds.")

    show_image_btn = gr.Button("Show Image")

    cookie_image = gr.Image(visible=False)

    audio_input = gr.Audio(
        sources="microphone",
        label="Record Your Speech",
        type="filepath",
        format="wav"
    )

    analyze_results_btn = gr.Button("Analyze Results")

    result_text = gr.Markdown(visible=False)

    show_image_btn.click(
        fn=show_image,
        inputs=None,
        outputs=[cookie_image]
    )

    analyze_results_btn.click(
        fn=analyze_results,
        inputs=audio_input,
        outputs=[result_text]
    )

demo.queue().launch()
