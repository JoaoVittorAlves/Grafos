# Nome dos arquivos
MAIN = grafo.py
TEST = testes.py

# Executar o programa principal
run:
	python3 $(MAIN)

# Executar os testes
test:
	python3 $(TEST)

# Limpar arquivos temporários
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} +




