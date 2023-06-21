# Whisper
Simple codes for transcribing an audio file using OpenAI's Whisper locally or via API.

# How to use
First, `pdm install` to set up the repo. If not installed, you can directly get PDM [here](https://pdm.fming.dev/latest/) or manage it via e.g., [asdf](https://github.com/asdf-vm/asdf).

## Use locally
Simply type `pdm run whisper <path to your audio file>`. Then, whisper runs locally and creates output files. See whisper's help by `pdm run whisper --help` for options.

## Use via API
You need an OpenAI key set in your shell as an environmental variable `OPENAI_API_KEY`. If set, simply run the main code `pdm run python main.py <path to your audio file>`. This is much faster than the local version, if you are on e.g., MacBook, though it's not free ([$0.006 / minute](https://openai.com/blog/introducing-chatgpt-and-whisper-apis)).
