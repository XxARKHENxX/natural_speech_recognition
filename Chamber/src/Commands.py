import sys
import subprocess
from .Recognition import Recognition
from .Speak import Speak

class Commands:
    def __init__(self):
        self.recognition = Recognition()
        self.speak = Speak()

    # Função para executar comandos
    def executar_comando(self, comando, transcrição = ""):
        # Adicione lógica para interpretar e executar comandos específicos

        if comando.lower() == "parar":
            print("Comando de parar recebido. Encerrando a execução.")
            sys.exit()

        elif "abra o navegador" in comando:
            # Lógica para abrir o navegador
            pass

        elif "spotify" in comando:
            if "musica" in comando:
                nome_da_musica = comando.lower().replace("música", "").strip()
                #ele ja ta pegando o nome da musica do comando, entao se tiver o musica ele ja pega o restante como nome
                #self.speak.falar("Qual o nome da musica?")
                #transcrição = self.recognition.reconhecimento_voz()
                subprocess.run(["spotify", f"spotify:search:{nome_da_musica}", "&"])
            else:
                subprocess.run(["start", "spotify:"])

        else:
            # Comando não reconhecido
            pass