#import os
import sys
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from .Response import Response
from .Recognition import Recognition
from .Commands import Commands 
from .Speak import Speak
    
class Conversation:
    #def __init__(self, minha_ia):
    def __init__(self):    
        self.response = Response()
        self.recognition = Recognition()
        self.commands = Commands()
        self.speak = Speak()
    

    def iniciar_conversacao(self):
        aguardando_comando = True
        while True:
            try:

                '''
                print("iniciando gravação")
                transcrição = self.recognition.reconhecimento_voz()
                #print(f"Você disse: {transcrição}")
                print(f"Voce disse: {transcrição}")
                self.speak.falar(f"Você disse: {transcrição}")
                print("iniciando resposta")
                resposta = self.response.gerar_resposta(transcrição)
                print(f"IA: {resposta}")
                self.speak.falar(f"{resposta}")
                print("Resposta gerada")

            except Exception as e:
                print(f"Erro: {e}")   
            '''         
                transcrição = self.recognition.reconhecimento_voz()

                resposta = self.response.gerar_resposta(transcrição)
                
                print(f"IA: {resposta}")
                self.speak.falar(f"{resposta}")

                if "executar" in transcrição.lower():
                    self.commands.executar_comando(resposta)


                #==============================================================#
                '''
                if aguardando_comando:
                    if not transcrição.strip(): #remove espaços e verifica se esta vazia
                        continue  # Volta para o início do loop
                    else:        
                        #self.speak.falar(f"Você disse: {transcrição}")
                        print(f"Você disse: {transcrição}") 

                        #if "inicializar" in transcrição.lower():

                        aguardando_comando = False
                        #print("Comando de iniciar recebido. Agora aguardando respostas.")
                        self.speak.falar("Comando de iniciar recebido. Agora aguardando respostas.")
                        continue  # Volta para o início do loop

                        resposta = self.response.gerar_resposta(transcrição)
                        print(f"IA: {resposta}")
                        self.speak.falar(f"{resposta}")

                        if "executar" in transcrição.lower():
                            self.commands.executar_comando(resposta)

                        #aguardando_comando = True  # Volta para o modo standBy
                    '''
                    #==============================================================#
            except Exception as e:
                print(f"Erro: {e}")
                sys.exit()
    
'''
        
    def __init__(self):
        self.response = Response()
        self.recognition = Recognition()
        self.commands = Commands()
        self.speak = Speak()

    def aguardar_inicializacao(self):
        while True:
            transcrição = self.recognition.reconhecimento_voz()
            if "inicializar" in transcrição.lower():
                self.speak.falar("Comando de iniciar recebido. Agora aguardando respostas.")
                return transcrição

    def processar_comando(self, transcrição):
        self.speak.falar(f"Você disse: {transcrição}")

        resposta = self.response.gerar_resposta(transcrição)
        print(f"IA: {resposta}")
        self.speak.falar(f"{resposta}")

        if "executar" in transcrição.lower():
            self.commands.executar_comando(resposta)

    def iniciar_conversacao(self):
        aguardando_comando = True
        while True:
            transcrição = self.aguardar_inicializacao()

            while aguardando_comando:
                self.processar_comando(transcrição)
                aguardando_comando = True  # Volta para o modo standBy
'''    
"""
class Conversation:
    #def __init__(self, minha_ia):
    def __init__(self):    
        self.response = Response()
        self.recognition = Recognition()
        self.commands = Commands()
        self.speak = Speak()
    

    def iniciar_conversacao(self):
        aguardando_comando = True
        while True:
            try:
                transcrição = self.recognition.reconhecimento_voz()
                #print(f"Você disse: {transcrição}")
                
                if aguardando_comando:
                    if not transcrição.strip(): #remove espaços e verifica se esta vazia
                        continue  # Volta para o início do loop
                    else:        
                        #self.speak.falar(f"Você disse: {transcrição}")
                        print(f"Você disse: {transcrição}") 

                        if "inicializar" in transcrição.lower():
                            aguardando_comando = False
                            #print("Comando de iniciar recebido. Agora aguardando respostas.")
                            self.speak.falar("Comando de iniciar recebido. Agora aguardando respostas.")
                            continue  # Volta para o início do loop

                        resposta = self.response.gerar_resposta(transcrição)
                        print(f"IA: {resposta}")
                        self.speak.falar(f"{resposta}")

                        if "executar" in transcrição.lower():
                            self.commands.executar_comando(resposta)

                        #aguardando_comando = True  # Volta para o modo standBy

            except Exception as e:
                print(f"Erro: {e}")
"""
# Exemplo de uso
#if __name__ == "__main__":
#    minha_ia = MinhaIA()
#    conversacao = Convesation(minha_ia)
#    conversacao.iniciar_conversacao()