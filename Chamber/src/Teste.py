import pyaudio
import numpy as np
from .Speak import Speak


def gravar():
    fs = 16000  # Taxa de amostragem
    chunk_size = 1024  # Tamanho do buffer de áudio

    # Inicializa o stream de áudio
    stream = pyaudio.PyAudio().open(
        format=pyaudio.paInt16,
        channels=1,
        rate=fs,
        input=True,
        frames_per_buffer=chunk_size,
    )

    # Grava a voz
    audio_frames = []
    txa = 16000  # Taxa de amostragem
    tempo_gravacao = 5  # Tempo de gravação em segundos
    #while True:
    print("Iniciando gravação")
    for i in range(int(txa / 1024 * tempo_gravacao)):
        data = stream.read(chunk_size)
        audio_frames.append(data)

        # Verifica se a gravação foi interrompida
        #if data == b'':
        #   break
    print("Gravação finalizada")
    # Fecha o stream de áudio
    stream.stop_stream()
    stream.close()

    return audio_frames


def reproduzir(audio_frames):
    # Cria o stream de áudio
    stream = pyaudio.PyAudio().open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        output=True,
    )

    # Reproduz a voz
    for audio_frame in audio_frames:
        stream.write(audio_frame)

    # Fecha o stream de áudio
    stream.stop_stream()
    stream.close()


# Grava a voz
audio_frames = gravar()

# Reproduz a voz
reproduzir(audio_frames)
