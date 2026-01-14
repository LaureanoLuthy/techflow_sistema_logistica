import sys
import os

# Garante que o teste encontre o arquivo app.py na pasta /src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import validar_prioridade, criar_tarefa, listar_tarefas, banco_de_tarefas

def test_validacao_prioridade():
    """Testa se as prioridades permitidas estão corretas."""
    assert validar_prioridade("Alta") is True
    assert validar_prioridade("Normal") is True
    assert validar_prioridade("Inexistente") is False

def test_fluxo_criacao_tarefa_urgente():
    """Testa a mudança de escopo: Prioridade Alta deve ter tag URGENTE."""
    banco_de_tarefas.clear()
    tarefa = criar_tarefa(1, "Porto de Santos", "Alta")
    
    # Agora o teste espera o aviso que adicionamos no código
    assert "⚠️ URGENTE" in tarefa["destino"]
    assert "Porto de Santos" in tarefa["destino"]

def test_listagem_tarefas():
    """Testa se a tarefa foi salva no banco de dados temporário."""
    banco_de_tarefas.clear()
    criar_tarefa(2, "Rio de Janeiro", "Normal")
    assert len(listar_tarefas()) == 1