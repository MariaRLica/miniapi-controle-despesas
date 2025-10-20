from flask import Blueprint, jsonify, request
from src.models import (
    get_all_expenses,
    get_expense_by_id,
    create_expense,
    update_expense,
    delete_expense,
    get_expenses_by_category
)

expenses_bp = Blueprint('expenses', __name__, url_prefix='/expenses')

# ---------------------------
# GET: todas as despesas
# ---------------------------
@expenses_bp.route('/', methods=['GET'])
def list_expenses():
    return jsonify(get_all_expenses())

# ---------------------------
# GET: despesas por categoria
# ---------------------------
@expenses_bp.route('/categoria/<string:categoria>', methods=['GET'])
def list_by_category(categoria):
    expenses = get_expenses_by_category(categoria)
    if expenses:
        return jsonify(expenses)
    return jsonify({"message": f"Nenhuma despesa encontrada na categoria '{categoria}'"}), 404

# ---------------------------
# GET: despesa por ID
# ---------------------------
@expenses_bp.route('/<int:expense_id>', methods=['GET'])
def get_expense(expense_id):
    expense = get_expense_by_id(expense_id)
    if expense:
        return jsonify(expense)
    return jsonify({"error": "Despesa não encontrada"}), 404

# ---------------------------
# POST: criar nova despesa
# ---------------------------
@expenses_bp.route('/', methods=['POST'])
def add_expense():
    data = request.get_json()
    if not data or "descricao" not in data or "valor" not in data:
        return jsonify({"error": "Dados inválidos"}), 400
    expense = create_expense(data)
    return jsonify(expense), 201

# ---------------------------
# PUT: atualizar despesa
# ---------------------------
@expenses_bp.route('/<int:expense_id>', methods=['PUT'])
def edit_expense(expense_id):
    data = request.get_json()
    expense = update_expense(expense_id, data)
    if expense:
        return jsonify(expense)
    return jsonify({"error": "Despesa não encontrada"}), 404

# ---------------------------
# DELETE: remover despesa
# ---------------------------
@expenses_bp.route('/<int:expense_id>', methods=['DELETE'])
def remove_expense(expense_id):
    success = delete_expense(expense_id)
    if success:
        return jsonify({"message": "Despesa removida com sucesso"})
    return jsonify({"error": "Despesa não encontrada"}), 404

# RESUMO FINANCEIRO ---------------------------

from src.models import get_financial_summary
@expenses_bp.route('/resumo', methods=['GET'])
def summary():
    resumo = get_financial_summary()
    return jsonify(resumo)
@expenses_bp.route('/resumo/html', methods=['GET'])
def summary_html():
    resumo = get_financial_summary()
    categorias = list(resumo["resumo_por_categoria"].keys())
    valores = list(resumo["resumo_por_categoria"].values())

    html = f"""
    <html>
        <head>
            <title>📊 Resumo Financeiro</title>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
                    text-align: center;
                    padding: 40px;
                    color: #1e293b;
                }}
                h1 {{
                    color: #0284c7;
                }}
                .chart-container {{
                    width: 500px;
                    margin: 40px auto;
                    background: white;
                    padding: 20px;
                    border-radius: 16px;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                }}
                a {{
                    text-decoration: none;
                    color: #0369a1;
                }}
            </style>
        </head>
        <body>
            <h1>📊 Resumo Financeiro por Categoria</h1>
            <div class="chart-container">
                <canvas id="chart"></canvas>
            </div>
            <p><a href="/">🏠 Voltar à página inicial</a></p>

            <script>
                const ctx = document.getElementById('chart').getContext('2d');
                const chart = new Chart(ctx, {{
                    type: 'pie',
                    data: {{
                        labels: {categorias},
                        datasets: [{{
                            label: 'Total gasto por categoria',
                            data: {valores},
                            backgroundColor: [
                                '#0ea5e9','#22c55e','#eab308','#ef4444','#8b5cf6','#ec4899','#14b8a6'
                            ],
                            borderWidth: 1
                        }}]
                    }},
                    options: {{
                        plugins: {{
                            legend: {{
                                position: 'bottom',
                                labels: {{ color: '#0f172a', font: {{ size: 14 }} }}
                            }}
                        }}
                    }}
                }});
            </script>
        </body>
    </html>
    """
    return html

from flask import render_template

@expenses_bp.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

from flask import render_template




