# src/routes.py

from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from src.core.exchange_service import get_usd_to_brl_exchange_rate, calculate_conversion
from src.models import (
    get_all_expenses,
    get_expense_by_id,
    create_expense,
    update_expense,
    delete_expense,
    get_expenses_by_category,
    get_financial_summary
)

# ----------------------------------------------------
# BLUEPRINTS
# ----------------------------------------------------
expenses_bp = Blueprint('expenses', __name__, url_prefix='/expenses')
exchange_bp = Blueprint('exchange', __name__, url_prefix='/exchange')

# ----------------------------------------------------
# 1. ROTAS DE DESPESAS (JSON API - CRUD Completo)
# ----------------------------------------------------

# GET: lista todas as despesas ou POST: cria nova despesa (JSON)
@expenses_bp.route('/', methods=['GET', 'POST'])
def handle_expenses_api():
    if request.method == 'POST':
        data = request.get_json()
        if not data or "descricao" not in data or "valor" not in data:
            return jsonify({"error": "Dados inválidos"}), 400
        try:
            # Garante que o valor é float antes de criar
            data['valor'] = float(data['valor'])
            expense = create_expense(data)
            return jsonify(expense), 201
        except ValueError:
             return jsonify({"error": "Valor da despesa deve ser numérico"}), 400
    
    # GET: lista todas as despesas (JSON)
    return jsonify(get_all_expenses())

# GET/PUT/DELETE por ID (JSON)
@expenses_bp.route('/<int:expense_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_expense_by_id_api(expense_id):
    expense = get_expense_by_id(expense_id)
    if not expense:
        return jsonify({"error": "Despesa não encontrada"}), 404
    
    if request.method == 'GET':
        return jsonify(expense)
    
    if request.method == 'PUT':
        data = request.get_json()
        try:
            updated_expense = update_expense(expense_id, data)
            return jsonify(updated_expense)
        except ValueError:
            return jsonify({"error": "Valor da despesa deve ser numérico"}), 400
    
    if request.method == 'DELETE':
        delete_expense(expense_id)
        return jsonify({"message": "Despesa removida com sucesso"})

# GET: despesas por categoria (JSON)
@expenses_bp.route('/categoria/<string:categoria>', methods=['GET'])
def list_by_category(categoria):
    expenses = get_expenses_by_category(categoria)
    if expenses:
        return jsonify(expenses)
    return jsonify({"message": f"Nenhuma despesa encontrada na categoria '{categoria}'"}), 404

# GET: resumo financeiro (JSON)
@expenses_bp.route('/resumo', methods=['GET'])
def summary():
    resumo = get_financial_summary()
    return jsonify(resumo)


# ----------------------------------------------------
# 2. ROTAS DE DESPESAS (VISUAL DASHBOARD - CRUD)
# ----------------------------------------------------

# VISUAL DASHBOARD (LISTAR e CRIAR via POST de formulário HTML)
@expenses_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        try:
            # Obtém dados do formulário HTML
            data = {
                'descricao': request.form['descricao'],
                'valor': request.form['valor'],
                'categoria': request.form['categoria'],
                'data': request.form['data']
            }
            create_expense(data) # Chama a função do models.py
            return redirect(url_for('expenses.dashboard'))
        except ValueError:
            # Exibe erro se o valor não for numérico
            error = "O valor da despesa deve ser um número válido."
        except Exception:
            error = "Ocorreu um erro ao adicionar a despesa."
    
    # GET: Renderiza o dashboard com todas as despesas e resumo
    all_expenses = get_all_expenses()
    summary = get_financial_summary()
    return render_template('dashboard.html', 
                           expenses=all_expenses, 
                           summary=summary, 
                           error=locals().get('error'))

# VISUAL DELETAR (Chamado pelo botão na tabela)
@expenses_bp.route('/delete-visual/<int:expense_id>', methods=['POST'])
def delete_expense_visual(expense_id):
    # A deleção deve ser feita via POST, mas só redireciona.
    delete_expense(expense_id)
    return redirect(url_for('expenses.dashboard'))

# VISUAL RESUMO (HTML)
@expenses_bp.route('/resumo/visual', methods=['GET'])
def summary_visual():
    resumo = get_financial_summary()
    # Usa o render_template para evitar o HTML bruto
    return render_template('resumo_visual.html', resumo=resumo)


# ----------------------------------------------------
# 3. ROTAS DE CÂMBIO (Obrigatório TDE2)
# ----------------------------------------------------

# GET: Cotação USD-BRL (JSON) - Rota Obrigatória TDE2
@exchange_bp.route('/usd-to-brl', methods=['GET'])
def get_exchange_rate():
    exchange_rate = get_usd_to_brl_exchange_rate()
    
    if exchange_rate is not None:
        return jsonify({
            "source_currency": "USD",
            "target_currency": "BRL",
            "rate": exchange_rate 
        }), 200
    else:
        return jsonify({
            "error": "Service Unavailable",
            "message": "Could not retrieve exchange rate from external API."
        }), 503
    
# INTERATIVA: Conversão USD/BRL (HTML com formulário)
@exchange_bp.route('/convert', methods=['GET', 'POST'])
def convert_currency():
    result = None
    amount = None
    error = None

    if request.method == 'POST':
        try:
            amount_str = request.form.get('amount')
            amount = float(amount_str)
            calculated_result = calculate_conversion(amount)
            
            if calculated_result is not None:
                result = f"{calculated_result:,.2f}"
            else:
                error = "Não foi possível obter a taxa de câmbio para a conversão."
                
        except ValueError:
            error = "Por favor, digite um valor numérico válido."
        except Exception:
            error = "Ocorreu um erro inesperado."
            
    return render_template(
        'convert.html', 
        amount=amount, 
        result=result, 
        error=error
    )