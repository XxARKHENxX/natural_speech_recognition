from transformers import GPT2LMHeadModel, GPT2Tokenizer

class Response:

    def __init__(self):
        self.modelo_dialogo = GPT2LMHeadModel.from_pretrained("microsoft/DialoGPT-large")
        self.tokenizer_dialogo = GPT2Tokenizer.from_pretrained("microsoft/DialoGPT-large")

    # Função para geração de respostas em diálogo
    def gerar_resposta(self, prompt):
        entrada_ids = self.tokenizer_dialogo.encode(prompt, return_tensors="pt")
        resposta_ids = self.modelo_dialogo.generate(entrada_ids, max_length=150, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)

        resposta_texto = self.tokenizer_dialogo.decode(resposta_ids[0], skip_special_tokens=True)
        return resposta_texto