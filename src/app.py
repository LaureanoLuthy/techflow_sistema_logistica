# Lista global para simular um banco de dados de tarefas
banco_de_tarefas = []

def validar_prioridade(prioridade):
    """Regra de negócio: Valida se a prioridade é permitida."""
    niveis_validos = ["Alta", "Normal", "Baixa"]
    return prioridade in niveis_validos

def criar_tarefa(id, destino, prioridade):
    """Cria uma nova tarefa com a mudança de escopo: aviso de URGENTE."""
    if not validar_prioridade(prioridade):
        prioridade = "Normal"
    
    # MUDANÇA DE ESCOPO: Se for Alta, o sistema agora destaca o destino
    if prioridade == "Alta":
        destino = f"⚠️ URGENTE: {destino}"
    
    nova_tarefa = {
        "id": id,
        "destino": destino,
        "prioridade": prioridade,
        "status": "A Fazer"
    }
    
    banco_de_tarefas.append(nova_tarefa)
    return nova_tarefa

def listar_tarefas():
    """Retorna todas as tarefas cadastradas."""
    return banco_de_tarefas