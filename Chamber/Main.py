#from src.Conversation import Conversation
from src.Recognition import Recognition

class Main:
    def __init__(self):
        #pass  # Adicione inicializações necessárias aqui
        self.recognition = Recognition()

    def run(self):
        #conversation = Conversation()
        #conversation.iniciar_conversacao()
        
        self.recognition.reconhecimento_voz()

if __name__ == "__main__":
    main = Main()
    main.run()

    #Recognition - silence_threshold = nivel que é considerado silencio