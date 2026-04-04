# Desafio para consolidar
# Tente criar uma classe chamada GeradorDeMusica que
#  recebe uma lista de músicas e, a cada next(),
#  ela imprime "Tocando agora: [Nome da Música]".
#  Quando as músicas acabarem, ela deve dizer "Playlist finalizada!".

class GeradorDeMusica:
    def __init__(self, lista_musicas):
        # Guardamos as músicas e começamos o ponteiro no zero
        self.musicas = lista_musicas
        self.indice = 0

    def __iter__(self):
        # Dizemos ao Python: "Pode me usar num loop!"
        return self

    def __next__(self):
        # Verificamos se o nosso ponteiro ainda está dentro da lista
        if self.indice < len(self.musicas):
            musica_atual = self.musicas[self.indice]
            self.indice += 1  # Movemos o ponteiro para a próxima música
            return f"Tocando agora: {musica_atual}"
        else:
            # Quando não há mais músicas, avisamos e paramos
            print("--- Playlist finalizada! ---")
            raise StopIteration

# --- Vamos testar nossa Vitrola ---

minhas_favoritas = ["Bohemian Rhapsody", "Imagine", "Hotel California", ""]
vitrola = GeradorDeMusica(minhas_favoritas)

print("Iniciando a festa:")
for musica in vitrola:
    print(musica)

"""
Vamos analisar o papel de cada parte, como se estivéssemos olhando o mecanismo 
de uma vitrola antiga:

    self.indice = 0: É o nosso braço da vitrola. 
                     Ele começa na borda do disco (posição 0).

    len(self.musicas): É o limite do disco. O código pergunta: 
                       "O braço ainda está em cima do disco ou já saiu pela 
                       borda?".

    self.indice += 1: Toda vez que uma música termina, o braço se move 
                      fisicamente para a próxima faixa.

    raise StopIteration: É o mecanismo automático que levanta o braço da vitrola
                         e desliga o motor quando o disco acaba.

"""
