import heapq
from collections import defaultdict

class NodoHuffman:
    def __init__(self, simbolo, frequencia):
        self.simbolo = simbolo
        self.frequencia = frequencia
        self.filho_esquerda = None
        self.filho_direita = None

    def __lt__(self, outro):
        return self.frequencia < outro.frequencia

def construir_arvore_huffman(frequencias):
    heap = [NodoHuffman(simbolo, frequencia) for simbolo, frequencia in frequencias.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        nodo1 = heapq.heappop(heap)
        nodo2 = heapq.heappop(heap)

        novo_nodo = NodoHuffman(None, nodo1.frequencia + nodo2.frequencia)
        novo_nodo.filho_esquerda = nodo1
        novo_nodo.filho_direita = nodo2

        heapq.heappush(heap, novo_nodo)

    return heap[0]

def gerar_codigos_huffman(arvore, prefixo="", codigos=None):
    if codigos is None:
        codigos = {}
    if arvore.simbolo is not None:
        codigos[arvore.simbolo] = prefixo
    if arvore.filho_esquerda is not None:
        gerar_codigos_huffman(arvore.filho_esquerda, prefixo + "0", codigos)
    if arvore.filho_direita is not None:
        gerar_codigos_huffman(arvore.filho_direita, prefixo + "1", codigos)

def codificar_mensagem(mensagem, codigos):
    return ''.join(codigos[caractere] for caractere in mensagem)

def decodificar_mensagem(codigo, arvore):
    mensagem_decodificada = ""
    nodo_atual = arvore

    for bit in codigo:
        if bit == '0':
            nodo_atual = nodo_atual.filho_esquerda
        else:
            nodo_atual = nodo_atual.filho_direita

        if nodo_atual.simbolo is not None:
            mensagem_decodificada += nodo_atual.simbolo
            nodo_atual = arvore

    return mensagem_decodificada

# Exemplo de uso
mensagem_original = "chiquinho"
frequencias = defaultdict(int)

for simbolo in mensagem_original:
    frequencias[simbolo] += 1

arvore_huffman = construir_arvore_huffman(frequencias)
codigos_huffman = {}
gerar_codigos_huffman(arvore_huffman, codigos=codigos_huffman)

mensagem_codificada = codificar_mensagem(mensagem_original, codigos_huffman)
mensagem_decodificada = decodificar_mensagem(mensagem_codificada, arvore_huffman)

print(f'Mensagem Original: {mensagem_original}')
print(f'Mensagem Codificada: {mensagem_codificada}')
print(f'Mensagem Decodificada: {mensagem_decodificada}')
