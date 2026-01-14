from app import validar_prioridade, criar_tarefa

def test_check_prioridade():
    assert validar_prioridade("Normal") is True

def test_check_tarefa():
    t = criar_tarefa(1, "Porto", "Normal")
    assert t["status"] == "A Fazer"