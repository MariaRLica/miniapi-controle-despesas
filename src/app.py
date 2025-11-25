# src/app.py

from flask import Flask, url_for
# Importa AMBOS os Blueprints necessários:
from src.routes import expenses_bp, exchange_bp 

# Importa a função que você precisa para o filtro, se necessário.
# Por exemplo, para formatar moedas no HTML, mas vamos ignorar o filtro por enquanto.
# from src.models import format_currency 


def create_app():
    # 1. Cria a instância da aplicação Flask
    app = Flask(__name__, static_folder='static', template_folder='templates')

    # carregar configurações (verifique se src.config.Config existe)
    app.config.from_object('src.config.Config')
    
    # Exemplo de como adicionar um filtro de template, se necessário:
    # app.jinja_env.filters['formatar_moeda'] = format_currency 

    # 2. Registra AMBOS os blueprints DENTRO da função create_app
    app.register_blueprint(expenses_bp)
    app.register_blueprint(exchange_bp) 

   # src/app.py (Apenas o trecho da função home())

# Certifique-se de que url_for está importado: from flask import Flask, url_for
# ...

    @app.route('/')
    def home():
        return f"""
        <html>
            <head>
                <title>💰 Mini API - Controle de Despesas</title>
                <link rel="stylesheet" href="{url_for('static', filename='style.css')}">
            </head>
            <body>
                <div class="header">
                    <h1 class="title">💰 API de Controle de Despesas</h1>
                </div>
                <div class="container">
                    <p>Bem-vindo! Use os links abaixo para acessar os painéis visuais:</p>

                    <div class="card">
                        <div class="link-item">📝 <a href="/expenses/dashboard">Dashboard de Despesas (CRUD VISUAL)</a> — Listar, Adicionar e Excluir</div>
                        <div class="link-item">📊 <a href="/expenses/resumo/visual">Resumo Financeiro (Gráfico)</a> — Visualização de gastos por categoria</div>
                        <div class="link-item">💱 <a href="/exchange/convert">Conversor USD para BRL (INTERATIVO)</a> — Nova funcionalidade do TDE2</div>
                    </div>

                    <p>
                        <small>Para acessar a API JSON pura:</small>
                        <a href="/expenses/">/expenses/</a> | 
                        <a href="/exchange/usd-to-brl">/exchange/usd-to-brl</a>
                    </p>

                    <footer>Desenvolvido por <strong>Maria Licá</strong> 🪶 — Flask API • 2025</footer>
                </div>
            </body>
        </html>
        """

    return app

# ...


if __name__ == '__main__':
    # Este bloco só é executado se você rodar 'python src/app.py'
    # Ao usar 'flask run', este bloco é ignorado.
    app = create_app()
    app.run(debug=True)