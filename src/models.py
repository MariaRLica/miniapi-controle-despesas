# Simulando um "banco de dados" em memória com despesas diversas
expenses = [
    {"id": 1, "descricao": "Supermercado", "valor": 250.75, "categoria": "Alimentação", "data": "2025-10-10"},
    {"id": 2, "descricao": "Conta de luz", "valor": 120.00, "categoria": "Moradia", "data": "2025-10-05"},
    {"id": 3, "descricao": "Uber para o trabalho", "valor": 32.50, "categoria": "Transporte", "data": "2025-10-09"},
    {"id": 4, "descricao": "Cinema", "valor": 45.00, "categoria": "Lazer", "data": "2025-10-12"},
    {"id": 5, "descricao": "Mensalidade da academia", "valor": 89.90, "categoria": "Saúde", "data": "2025-10-07"},
    {"id": 6, "descricao": "Combustível", "valor": 180.00, "categoria": "Transporte", "data": "2025-10-13"},
    {"id": 7, "descricao": "Jantar com amigos", "valor": 95.30, "categoria": "Lazer", "data": "2025-10-14"},
    {"id": 8, "descricao": "Farmácia", "valor": 63.80, "categoria": "Saúde", "data": "2025-10-15"},
]

next_id = 9

def get_all_expenses():
    return expenses

def get_expense_by_id(expense_id):
    for expense in expenses:
        if expense["id"] == expense_id:
            return expense
    return None

def create_expense(data):
    global next_id
    expense = {
        "id": next_id,
        "descricao": data.get("descricao"),
        "valor": data.get("valor"),
        "categoria": data.get("categoria"),
        "data": data.get("data")
    }
    expenses.append(expense)
    next_id += 1
    return expense

def update_expense(expense_id, data):
    expense = get_expense_by_id(expense_id)
    if expense:
        expense.update({
            "descricao": data.get("descricao", expense["descricao"]),
            "valor": data.get("valor", expense["valor"]),
            "categoria": data.get("categoria", expense["categoria"]),
            "data": data.get("data", expense["data"])
        })
        return expense
    return None

def delete_expense(expense_id):
    global expenses
    expense = get_expense_by_id(expense_id)
    if expense:
        expenses = [e for e in expenses if e["id"] != expense_id]
        return True
    return False

def get_expenses_by_category(category_name):
    return [e for e in expenses if e["categoria"].lower() == category_name.lower()]

def get_financial_summary():
    summary = {}
    total = 0.0
    for expense in expenses:
        categoria = expense["categoria"]
        valor = expense["valor"]
        summary[categoria] = summary.get(categoria, 0) + valor
        total += valor
    return {
        "resumo_por_categoria": summary,
        "total_geral": round(total, 2)
    }
