class TranscriptionPostprocessing:
    def __init__(self):
        pass

    def postprocess(self, transcription):
        # Remoção de tokens de silêncio
        transcription = transcription.replace("[CLS]", "").replace("[SEP]", "")

        # Correção de erros de pontuação
        transcription = transcription.replace(" .", ".").replace(" ,", ",")

        # Normalização do texto
        transcription = transcription.lower().strip()

        return transcription
