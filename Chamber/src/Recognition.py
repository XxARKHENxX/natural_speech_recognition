import pyaudio
import numpy as np
from .TranscriptionPostProcess import TranscriptionPostprocessing
from .AudioPreprocessing import AudioPreprocessing
from .NeMoSpeechRecognition import NeMoSpeechRecognition

class Recognition:

    def __init__(self, silence_threshold=50.000):
        self.audio_preprocessing = AudioPreprocessing()
        self.nemo_speech_recognition = NeMoSpeechRecognition()
        self.transcription_postprocessing = TranscriptionPostprocessing()
        self.silence_threshold = silence_threshold
        self.pyAud = pyaudio.PyAudio()

    def reconhecimento_voz(self):
        fs = 16000  # Taxa de amostragem
        stream = None
        frames = []

        # Solicitação de detecção automática de voz
        while True:
            audio_chunk = self.pyAud.get_next_audio_chunk()
            if self.audio_preprocessing.detect_voice(audio_chunk):
                break

        # Inicializa o stream de áudio
        stream = pyaudio.PyAudio().open(
            format=pyaudio.paInt16,
            channels=1,
            rate=fs,
            input=True,
            frames_per_buffer=1024,
        )

        # Grava o áudio
        for i in range(int(fs / 1024 * self.tempo_gravacao)):
            data = stream.read(1024)
            audio_chunk = np.frombuffer(data, dtype=np.int16)
            frames.append(audio_chunk)

        # Encerra o stream de áudio
        stream.stop_stream()
        stream.close()
        self.pyAud.terminate()

        # Processa o áudio
        audio_input = np.concatenate(frames)
        audio_input = self.audio_preprocessing.preprocess(audio_input)

        # Detecta silêncio
        if np.mean(np.abs(audio_chunk)) < self.silence_threshold:
            return None

        # Reconhece a fala
        transcription = self.nemo_speech_recognition.recognize(audio_input)
        transcription = self.transcription_postprocessing.postprocess(transcription)

        return transcription

    @property
    def tempo_gravacao(self):
        return self._tempo_gravacao

    @tempo_gravacao.setter
    def tempo_gravacao(self, valor):
        if valor <= 0:
            raise ValueError("O tempo de gravação deve ser maior que zero.")
        self._tempo_gravacao = valor
