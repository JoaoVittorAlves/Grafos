"""4
   0 3 4 0
   3 0 5 7
   4 5 0 0
   0 7 0 0
"""

import unittest
from grafos import GrafoListaAdjacencia, bfs_caminho, dfs_pilha

class TestGrafo(unittest.TestCase):
    def setUp(self):
        # Criando o grafo a partir da matriz de adjacência
        self.grafo = GrafoListaAdjacencia(4)
        self.grafo.adicionar_aresta(0, 1)
        self.grafo.adicionar_aresta(0, 2)
        self.grafo.adicionar_aresta(1, 2)
        self.grafo.adicionar_aresta(1, 3)

    def test_bfs_caminho(self):
        # Teste para verificar se BFS encontra o caminho correto
        print("\nTeste BFS:")
        bfs_caminho(self.grafo, 0, 3)  # Deve encontrar um caminho de 0 a 3

    def test_dfs_pilha(self):
        # Teste para verificar a ordem de visitação do DFS
        print("\nTeste DFS:")
        dfs_pilha(self.grafo, 0)  # Deve visitar todos os vértices conectados a partir de 0

if __name__ == '__main__':
    unittest.main()
