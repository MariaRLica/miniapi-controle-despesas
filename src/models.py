import typing # <<<< CORREÇÃO ESSENCIAL PARA PYTHON 3.8

# Simulando um "banco de dados" em memória com despesas diversas
# CORREÇÃO 1: Renomear DESPESAS para 'expenses' (ou 'despesas') em minúsculas
# para indicar que é uma estrutura de dados MUTÁVEL, não uma constante.
expenses = [
    {"id": 1, "descricao": "Supermercado", "valor": 250.75, "categoria": "Alimentação", "data": "2025-10-10"},
    {"id": 2, "descricao": "Conta de luz", "valor": 120.00, "categoria": "Moradia", "data": "2025-10-05"},
    {"id": 3, "descricao": "Uber para o trabalho", "valor": 32.50, "categoria": "Transporte", "data": "2025-10-09"},
    {"id": 4, "descricao": "Cinema", "valor": 45.00, "categoria": "Laser", "data": "2025-10-12"},
    {"id": 5, "descricao": "Mensalidade da academia", "valor": 89.90, "categoria": "Saúde", "data": "2025-10-07"},
    {"id": 6, "descricao": "Combustível", "valor": 180.00, "categoria": "Transporte", "data": "2025-10-13"},
    {"id": 7, "descricao": "Jantar com amigos", "valor": 95.30, "categoria": "Laser", "data": "2025-10-14"},
    {"id": 8, "descricao": "Farmácia", "valor": 63.80, "categoria": "Saúde", "data": "2025-10-15"},
]

NEXT_ID = 9 # Variável em maiúsculas porque é uma constante ou variável de controle global

def obter_todas_as_despesas():
    """Retorna a lista completa de despesas."""
    return expenses # Usando a nova variável

def obter_despesa_por_id(expense_id: int) -> typing.Union[dict, None]:
    """Busca uma despesa pelo ID."""
    for expense in expenses:
        if expense["id"] == expense_id:
            return expense
    return None

def criar_despesa(data: dict) -> dict:
    """Crie e adicione uma nova despesa à lista na memória."""
    global NEXT_ID
    expense = {
        "id": NEXT_ID,
        "descricao": data.get("descricao"),
        "valor": float(data.get("valor", 0.0)),
        "categoria": data.get("categoria"),
        "data": data.get("data")
    }
    expenses.append(expense) # Usando a nova variável
    NEXT_ID += 1
    return expense

def atualizar_despesa(expense_id: int, data: dict) -> typing.Union[dict, None]:
    """Atualiza uma despesa existente pelo ID."""
    expense = obter_despesa_por_id(expense_id)
    if expense:
        if 'valor' in data:
             data['valor'] = float(data['valor'])
        
        expense.update({
            "descricao": data.get("descricao", expense["descricao"]),
            "valor": data.get("valor", expense["valor"]),
            "categoria": data.get("categoria", expense["categoria"]),
            "data": data.get("data", expense["data"])
        })
        return expense
    return None

def excluir_despesa(expense_id: int) -> bool:
    """Remover uma despesa pelo ID."""
    global expenses
    initial_length = len(expenses)
    # Filtre a lista, mantendo apenas os itens com ID diferente
    expenses = [e for e in expenses if e["id"] != expense_id] # Usando a nova variável
    return len(expenses) < initial_length

def obter_despesas_por_categoria(category_name: str) -> list:
    """Filtra despesas por categoria (sem distinção entre maiúsculas e minúsculas)."""
    # Usando a nova variável 'expenses' e renomeando 'nome_da_categoria'
    return [e for e in expenses if e["categoria"].lower() == category_name.lower()]

def obter_resumo_financeiro() -> dict:
    """Cálculo do resumo financeiro (total e por categoria)."""
    summary = {}
    total = 0.0
    for expense in expenses: # Usando a nova variável
        category = expense["categoria"]
        value = expense["valor"]
        summary[category] = summary.get(category, 0) + value
        total += value
        
    return {
        "resumo_por_categoria": summary,
        "total_geral": round(total, 2),
        "total_por_mes": round(total, 2)
    }

# CORREÇÃO 2: Remover autoatribuição inútil
# obter_resumo_financeiro = obter_resumo_financeiro # Removida!