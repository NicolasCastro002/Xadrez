# xadrez.py
# Desafio - Movimentando as Peças do Xadrez
# Autor: Nicolas Lima

class Peca:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao  # (linha, coluna)

    def movimentos_possiveis(self):
        return []


class Rei(Peca):
    def movimentos_possiveis(self):
        linha, coluna = self.posicao
        movimentos = [
            (linha+1, coluna), (linha-1, coluna),
            (linha, coluna+1), (linha, coluna-1),
            (linha+1, coluna+1), (linha+1, coluna-1),
            (linha-1, coluna+1), (linha-1, coluna-1)
        ]
        return [(l, c) for l, c in movimentos if 0 <= l < 8 and 0 <= c < 8]


class Rainha(Peca):
    def movimentos_possiveis(self):
        linha, coluna = self.posicao
        movimentos = []
        for i in range(8):
            if i != linha:
                movimentos.append((i, coluna))  # verticais
            if i != coluna:
                movimentos.append((linha, i))  # horizontais
        for i in range(1, 8):
            if 0 <= linha+i < 8 and 0 <= coluna+i < 8:
                movimentos.append((linha+i, coluna+i))
            if 0 <= linha-i < 8 and 0 <= coluna-i < 8:
                movimentos.append((linha-i, coluna-i))
            if 0 <= linha+i < 8 and 0 <= coluna-i < 8:
                movimentos.append((linha+i, coluna-i))
            if 0 <= linha-i < 8 and 0 <= coluna+i < 8:
                movimentos.append((linha-i, coluna+i))
        return movimentos


class Torre(Peca):
    def movimentos_possiveis(self):
        linha, coluna = self.posicao
        movimentos = []
        for i in range(8):
            if i != linha:
                movimentos.append((i, coluna))
            if i != coluna:
                movimentos.append((linha, i))
        return movimentos


class Bispo(Peca):
    def movimentos_possiveis(self):
        linha, coluna = self.posicao
        movimentos = []
        for i in range(1, 8):
            if 0 <= linha+i < 8 and 0 <= coluna+i < 8:
                movimentos.append((linha+i, coluna+i))
            if 0 <= linha-i < 8 and 0 <= coluna-i < 8:
                movimentos.append((linha-i, coluna-i))
            if 0 <= linha+i < 8 and 0 <= coluna-i < 8:
                movimentos.append((linha+i, coluna-i))
            if 0 <= linha-i < 8 and 0 <= coluna+i < 8:
                movimentos.append((linha-i, coluna+i))
        return movimentos


class Cavalo(Peca):
    def movimentos_possiveis(self):
        linha, coluna = self.posicao
        movimentos = [
            (linha+2, coluna+1), (linha+2, coluna-1),
            (linha-2, coluna+1), (linha-2, coluna-1),
            (linha+1, coluna+2), (linha+1, coluna-2),
            (linha-1, coluna+2), (linha-1, coluna-2)
        ]
        return [(l, c) for l, c in movimentos if 0 <= l < 8 and 0 <= c < 8]


class Peao(Peca):
    def movimentos_possiveis(self):
        linha, coluna = self.posicao
        movimentos = []
        # Movimento simples para frente
        if linha+1 < 8:
            movimentos.append((linha+1, coluna))
        # Movimento de duas casas se estiver na linha inicial
        if linha == 1 and linha+2 < 8:
            movimentos.append((linha+2, coluna))
        # Capturas em diagonal
        if linha+1 < 8 and coluna+1 < 8:
            movimentos.append((linha+1, coluna+1))
        if linha+1 < 8 and coluna-1 >= 0:
            movimentos.append((linha+1, coluna-1))
        return movimentos


# ==========================
# Exemplo de execução
# ==========================
if __name__ == "__main__":
    pecas = [
        Rei("Rei", (4, 4)),
        Rainha("Rainha", (3, 3)),
        Torre("Torre", (0, 0)),
        Bispo("Bispo", (2, 2)),
        Cavalo("Cavalo", (4, 4)),
        Peao("Peão", (1, 3))
    ]

    for peca in pecas:
        print(f"\n{peca.nome} na posição {peca.posicao}")
        print("Movimentos possíveis:", peca.movimentos_possiveis())
