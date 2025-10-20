from flask import Flask
from src.routes import expenses_bp

def create_app():
    app = Flask(__name__)

    # carregar configurações
    app.config.from_object('src.config.Config')

    # registrar blueprint de despesas
    app.register_blueprint(expenses_bp)

    @app.route('/')
    def home():
        return """
        <html>
            <head>
                <title>💰 Mini API - Controle de Despesas</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background: linear-gradient(135deg, #dbeafe, #e0f2fe);
                        color: #1e293b;
                        text-align: center;
                        padding: 40px;
                    }
                    h1 {
                        color: #0ea5e9;
                    }
                    .card {
                        background: white;
                        border-radius: 16px;
                        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                        padding: 20px;
                        margin: 20px auto;
                        width: 60%;
                        transition: 0.3s;
                    }
                    .card:hover {
                        transform: scale(1.02);
                    }
                    a {
                        text-decoration: none;
                        color: #0ea5e9;
                        font-weight: bold;
                    }
                    footer {
                        margin-top: 40px;
                        color: #64748b;
                    }
                </style>
            </head>
            <body>
                <h1>💰 API de Controle de Despesas</h1>
                <p>Bem-vindo! Use os endpoints abaixo para explorar as rotas da API:</p>

                <div class="card">
                    <p>📄 <a href="/expenses/">GET /expenses</a> — Lista todas as despesas</p>
                    <p>🧾 <a href="/expenses/categoria/Transporte">GET /expenses/categoria/&lt;categoria&gt;</a> — Filtra por categoria</p>
                    <p>📊 <a href="/expenses/resumo">GET /expenses/resumo</a> — Exibe o resumo financeiro</p>
                </div>

                <footer>Desenvolvido por <strong>Maria Licá</strong> 🪶 — Flask API • 2025</footer>
            </body>
        </html>
        """

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
