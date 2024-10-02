import torch
import numpy as np
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

class NeMoSpeechRecognition:
    def __init__(self, model_name="facebook/wav2vec2-base-960h"):
        self.model = Wav2Vec2ForCTC.from_pretrained(model_name)
        self.tokenizer = Wav2Vec2Tokenizer.from_pretrained(model_name)

    def recognize(self, audio):
        # Preprocessamento do áudio
        audio = audio / np.max(np.abs(audio))

        # Tokenização do áudio
        input_values = self.tokenizer(audio, return_tensors="pt").input_values.to("cuda")

        # Reconhecimento de voz com NeMo
        with torch.no_grad():
            logits = self.model(input_values).logits

        # Decodificação da transcrição
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = self.tokenizer.batch_decode(predicted_ids)[0]

        return transcription
