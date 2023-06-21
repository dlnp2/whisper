"""Transcribe an audio file via OpenAI Whisper API."""
import argparse
import os
from pathlib import Path

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

parser = argparse.ArgumentParser()
parser.add_argument("audio", type=str)
args = parser.parse_args()

# https://platform.openai.com/docs/guides/speech-to-text
with open(args.audio, "rb") as fin:
    print("Querying...")
    results = openai.Audio.transcribe("whisper-1", fin)
    print("Done.")

with (Path(args.audio).parent / (Path(args.audio).stem + "_whisper.txt")).open("w") as fout:
    fout.write(results["text"])
