# Implementação do Grafo usando Lista de Adjacência
class GrafoListaAdjacencia:
    def __init__(self, num_vertices):
        # Inicializa o número de vértices do grafo
        self.num_vertices = num_vertices
        # Cria uma lista de adjacência vazia para cada vértice
        self.lista = [[] for _ in range(num_vertices)]

    def adicionar_aresta(self, u, v):
        # Adiciona uma aresta entre os vértices u e v
        self.lista[u].append(v)
        self.lista[v].append(u)  # Para grafos não direcionados

    def imprimir(self):
        # Imprime a lista de adjacência
        for idx, adj in enumerate(self.lista):
            print(f"{idx}: {adj}")


# Implementação da Busca em Largura (BFS)
from collections import deque

def bfs_caminho(grafo, inicio, fim):
    num_vertices = grafo.num_vertices
    visitado = [False] * num_vertices
    anterior = [-1] * num_vertices

    fila = deque([inicio])
    visitado[inicio] = True

    while fila:
        vertice = fila.popleft()
        
        for vizinho in grafo.lista[vertice]:  # Para lista de adjacência
            if not visitado[vizinho]:
                visitado[vizinho] = True
                anterior[vizinho] = vertice
                fila.append(vizinho)

    caminho = []
    atual = fim
    while atual != -1:
        caminho.append(atual)
        atual = anterior[atual]

    caminho.reverse()
    
    if caminho[0] == inicio:
        print(f"Caminho entre {inicio} e {fim}: {caminho}")
    else:
        print(f"Não há caminho entre {inicio} e {fim}")


# Implementação da Busca em Profundidade (DFS) sem recursão
def dfs_pilha(grafo, inicio):
    num_vertices = grafo.num_vertices
    visitado = [False] * num_vertices
    pilha = [inicio]

    while pilha:
        vertice = pilha.pop()
        
        if not visitado[vertice]:
            visitado[vertice] = True
            print(vertice, end=' ')
            
            for vizinho in reversed(grafo.lista[vertice]):  # Inverte para garantir ordem correta
                if not visitado[vizinho]:
                    pilha.append(vizinho)
    print()



def main():
    # Exemplo 
    grafo = GrafoListaAdjacencia(4)
    grafo.adicionar_aresta(0, 1)
    grafo.adicionar_aresta(0, 2)
    grafo.adicionar_aresta(1, 2)
    grafo.adicionar_aresta(1, 3)
    grafo.adicionar_aresta(2, 3)
    
    print("Grafo:")
    grafo.imprimir()

    # Executa BFS e DFS
    print("\nBusca em Largura (BFS):")
    bfs_caminho(grafo, 0, 3)
    
    print("\nBusca em Profundidade (DFS):")
    dfs_pilha(grafo, 0)

if __name__ == "__main__":
    main()
