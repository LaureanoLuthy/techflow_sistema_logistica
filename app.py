def validar_prioridade(p):
    return p in ["Normal", "Urgente", "Crítica"]

def criar_tarefa(id, destino, prioridade):
    return {"id": id, "destino": destino, "status": "A Fazer"}