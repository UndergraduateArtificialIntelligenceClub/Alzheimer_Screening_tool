import gradio as gr
import time

info = """
## About
Alzheimer's disease (AD) is a progressive neurodegenerative disease that impairs memory, thinking, and behaviour. It is the most common form of dementia, and initial symptoms are often confused with normal brain aging. AD is most conclusively diagnosed by positron emission tomography (PET) and cerebrospinal fluid examinations. However, these procedures are costly and invasive, and the current challenge is diagnosing Alzheimer's disease at the stage of mild cognitive impairment before memory loss occurs.

## How It Works
Symptoms of early AD often include speech impairment, object naming problems, and reduction in vocabulary. These linguistic signs can often be identified in speech patterns using NLP methods. This tool uses [BERT](https://en.wikipedia.org/wiki/BERT_(language_model))-family models trained on the ADReSS dataset from [DementiaBank](https://talkbank.org/dementia/) to estimate the likelihood of early-stage AD.
"""

def show_image(checkbox_state):
    return gr.update(visible=checkbox_state)

# This has an auto progress bar if it takes long.
def analyze_speech(audio):
    if audio is None:
        return ["", ""]
    # Simulate thinking
    time.sleep(1)
    return [
            gr.Textbox("You do not have Alzheimer's!"),
            gr.Textbox("You said blah blah blah")
    ]

def clear_all_components():
    return [None, "", ""]

with gr.Blocks(theme=gr.themes.Ocean()) as demo:

    gr.Markdown("<h1 style='text-align: center;'>Alzheimer's Screening Tool</h1>")

    gr.HTML("""
    <figure>
        <img
          src="https://uais.dev/images/logo.svg"
          alt="A brain made up of circuits"
          style="display: block; margin-left: auto; margin-right: auto; max-width: 300px; max-height: 300px;">
    </figure>
    """)

    gr.Markdown(info)

    gr.Markdown("## Try it now!")

    gr.Markdown("Start a recording, and describe the following image with as much detail as you can within 30 seconds.")

    disclaimer_checkbox = gr.Checkbox(label="I accept that this tool is for informational use only and does not constitute medical advice.")

    cookie_image = gr.Image(
        value="cookie-theft.jpg",
        show_label=False,
        visible=False
    )

    disclaimer_checkbox.change(
        fn=show_image,
        inputs=disclaimer_checkbox,
        outputs=cookie_image
    )

    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(
                sources="microphone",
                label="Describe the image",
            )

            with gr.Row():
                clear_btn = gr.Button("Clear")
                analyze_btn = gr.Button("Analyze", variant="primary")

        with gr.Column():
            prediction_output = gr.Textbox(label="Prediction")
            transcript_output = gr.Textbox(label="Transcript")

    clear_btn.click(
        fn=clear_all_components,
        inputs=None,
        outputs=[audio_input, prediction_output, transcript_output]
    )

    analyze_btn.click(
        fn=analyze_speech,
        inputs=audio_input,
        outputs=[prediction_output, transcript_output]
    )

demo.queue().launch()
