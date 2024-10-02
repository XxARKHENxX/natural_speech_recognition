import pyaudio
import numpy as np
import sys
import torch
import pyttsx3
import ctypes
import subprocess # para executar comandos no sistema
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer, GPT2LMHeadModel, GPT2Tokenizer

# Carregar modelos pré-treinados
modelo_audio = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
tokenizer_audio = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")

modelo_dialogo = GPT2LMHeadModel.from_pretrained("microsoft/DialoGPT-large")
tokenizer_dialogo = GPT2Tokenizer.from_pretrained("microsoft/DialoGPT-large")


# Solicitar privilegios de administrador
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
def falar(self, mensagem):
        engine = pyttsx3.init()
        engine.say(mensagem)
        engine.runAndWait()

# Função para reconhecimento de voz
def reconhecimento_voz():
    fs = 16000  # Taxa de amostragem
    tempo_gravacao = 5  # Tempo de gravação em segundos

    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt16, channels=1, rate=fs, input=True, frames_per_buffer=1024)

    print("Fale algo...")

    frames = []
    for i in range(int(fs / 1024 * tempo_gravacao)):
        data = stream.read(1024)
        frames.append(np.frombuffer(data, dtype=np.int16))

    stream.stop_stream()
    stream.close()
    p.terminate()

    audio_input = np.concatenate(frames)
    input_values = tokenizer_audio(audio_input, return_tensors="pt").input_values

    with torch.no_grad():
        logits = modelo_audio(input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcrição = tokenizer_audio.batch_decode(predicted_ids)[0]

    return transcrição

# Função para geração de respostas em diálogo
def gerar_resposta(prompt):
    entrada_ids = tokenizer_dialogo.encode(prompt, return_tensors="pt")
    resposta_ids = modelo_dialogo.generate(entrada_ids, max_length=150, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)

    resposta_texto = tokenizer_dialogo.decode(resposta_ids[0], skip_special_tokens=True)
    return resposta_texto

# Função para executar comandos
def executar_comando(comando):
    # Adicione lógica para interpretar e executar comandos específicos

    if comando.lower() == "parar": #Comando.Lower so vai ser verdadeiro se falar exatamente oq ta ali
        print("Comando de parar recebido. Encerrando a execução.")
        sys.exit()
    elif "abra o navegador" in comando:
        # Lógica para abrir o navegador
        pass
    elif "spotfy" in comando:

        if "musica" in comando:
            nome_da_musica = transcrição.lower().replace("música", "").strip()
            subprocess.run(["spotify", f"spotify:search:{nome_da_musica}", "&"])
        else:
            subprocess.run(["start", "spotify:"])

    elif "parar" in comando:
        print("Comando de parar recebido. Encerrando a execução.")
        sys.exit()
        
    else:
        # Comando não reconhecido
        pass

# Loop de conversação
aguardando_comando = True
while True:
    try:
        transcrição = reconhecimento_voz()
        print(f"Você disse: {transcrição}")

        if aguardando_comando:
            if not transcrição.strip():
                continue # Volta para o início do loop
        
        if "iniciar" in transcrição.lower():
                esperando_comando = False
                print("Comando de iniciar recebido. Agora aguardando respostas.")
                continue # Volta para o início do loop

        resposta = gerar_resposta(transcrição)
        print(f"IA: {resposta}")

        if "executar" in transcrição.lower(): 
            executar_comando(resposta)
        
        esperando_comando = True # Volta para o modo standBy

    except Exception as e:
        print(f"Erro: {e}")