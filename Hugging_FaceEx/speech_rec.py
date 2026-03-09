from transformers import pipeline
from datasets import load_dataset, Audio

asr = pipeline(
    "automatic-speech-recognition",
    model="facebook/wav2vec2-base-960h"
)

dataset = load_dataset(
    "PolyAI/minds14",
    name="en-US",
    split="train"
)

dataset = dataset.cast_column(
    "audio",
    Audio(sampling_rate=asr.feature_extractor.sampling_rate)
)

audio_inputs = dataset[:4]["audio"]
texts = asr(audio_inputs)

print([t["text"] for t in texts])