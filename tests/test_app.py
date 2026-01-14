import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import validar_prioridade, criar_tarefa, listar_tarefas

def test_validacao_prioridade():
    assert validar_prioridade("Alta") is True
    assert validar_prioridade("Inexistente") is False

def test_fluxo_criacao_tarefa():
    # Limpa a lista antes do teste
    from app import banco_de_tarefas
    banco_de_tarefas.clear()
    
    tarefa = criar_tarefa(1, "Porto de Santos", "Alta")
    
    assert tarefa["destino"] == "Porto de Santos"
    assert len(listar_tarefas()) == 1

def test_mudanca_escopo_urgente():
    # Testa se a tag URGENTE é adicionada corretamente
    tarefa = criar_tarefa(99, "Cuiabá", "Alta")
    assert "⚠️ URGENTE" in tarefa["destino"]