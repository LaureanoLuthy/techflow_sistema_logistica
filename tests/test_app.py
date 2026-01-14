import sys
import os

# Este bloco garante que o teste encontre o arquivo app.py dentro da pasta /src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import validar_prioridade, criar_tarefa

def test_check_prioridade():
    # Testa se a função aceita uma prioridade válida
    assert validar_prioridade("Normal") is True

def test_check_tarefa():
    # Testa se a tarefa é criada com o status inicial correto
    t = criar_tarefa(1, "Porto", "Normal")
    assert t["status"] == "A Fazer"