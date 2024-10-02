import pyttsx3
import pyaudio

class Speak:
    def __init__(self):
        # Inicializar o motor de síntese de voz
        self.engine = pyttsx3.init()

    def falar(self, mensagem):
        self.engine.say(mensagem)
        self.engine.runAndWait()

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

# Exemplo de uso da classe
#if __name__ == "__main__":
#    minha_ia = Speak()
#    minha_ia.falar("Olá! Esta é uma mensagem de exemplo.")