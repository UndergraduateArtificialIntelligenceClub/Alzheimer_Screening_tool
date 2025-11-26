# Alzheimer Screening Tool

Simple Gradio demo that records a short cookie-theft description, runs Whisper to transcribe the audio, and (soon) will send the transcript through an Alzheimer-screening language model.

## Requirements

- Python 3.13+
- Chocolatey (Package Manager) to easily install some of the dependencies on Windows. Instructions are here: https://chocolatey.org/install
- FFmpeg (speech-to-text needs it)
  - macOS: `brew install ffmpeg`
  - Ubuntu/Debian: `sudo apt install ffmpeg`
  - Windows: `choco install ffmpeg`
- libsndfile (used by the `soundfile` Python package)
  - macOS Homebrew installs this automatically with `pip install soundfile`
  - Ubuntu/Debian: `sudo apt install libsndfile1`
  - Windows: `choco install libsndfile`
- (Optional) `python3 -m venv .venv && source .venv/bin/activate`

## Install

pip install -e .That pulls in:

- `gradio`
- `torch`, `torchaudio`
- `transformers`
- `soundfile` (for temp WAV handling)

Make sure to also install ffmpeg and libsndfile using the instructions under "Requirements" above

## Run

python main.py - Gradio will print a local URL (defaults to http://127.0.0.1:7860). Open it in a browser, accept the disclaimer to reveal the image, record up to 30 seconds of speech, then click “Analyze”.

## Notes

- Recordings longer than ~30 seconds trigger Whisper’s long-form mode; in that case the app enables timestamp prediction automatically.
- Whisper downloads its model weights the first time you run; expect a short pause.
- If transcription quality is poor, ensure you’re recording in a quiet room with the mic close to your mouth, and that FFmpeg/libsndfile are installed correctly.
