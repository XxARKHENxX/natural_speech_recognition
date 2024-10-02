import librosa
import numpy as np
import torchaudio

class AudioPreprocessing:
    def __init__(self, sampling_rate=16000):
        self.sampling_rate = sampling_rate

    def preprocess(self, audio):
        # Normalização da amplitude
        audio = audio / np.max(np.abs(audio))

        # Resample
        if self.sampling_rate != audio.shape[0]:
            audio = librosa.resample(audio, orig_sr=audio.shape[0], target_sr=self.sampling_rate)

        return audio