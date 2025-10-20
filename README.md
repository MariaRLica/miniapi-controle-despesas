git clone https://github.com/seu-usuario/miniapi-controle-despesas.git
cd miniapi-controle-despesas

Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux
venv\Scripts\activate     # Windows

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Rodar a aplicação
python -m src.app


Acesse no navegador:
👉 http://127.0.0.1:5000/

Endpoints principais
Método	Rota	Descrição
GET	/expenses/	Lista todas as despesas
GET	/expenses/<id>	Busca despesa específica
POST	/expenses/	Adiciona nova despesa
PUT	/expenses/<id>	Atualiza uma despesa
DELETE	/expenses/<id>	Remove uma despesa
GET	/expenses/categoria/<categoria>	Filtra por categoria
GET	/expenses/resumo	Mostra resumo financeiro
GET	/expenses/dashboard	Interface web interativa

🧭 Estrutura de Diretórios
miniapi/
│
├── src/
│   ├── app.py           # Configuração principal do Flask
│   ├── models.py        # "Banco de dados" em memória e funções CRUD
│   ├── routes.py        # Rotas e endpoints da API
│   ├── config.py        # Configurações adicionais
│   └── templates/
│       └── dashboard.html  # Interface web interativa
│
├── requirements.txt      # Dependências do projeto
├── .gitignore            # Arquivos e pastas ignorados no Git
└── README.md             # Documentação do projeto

*Endpoints da API*
Método	Rota	Descrição
GET	/expenses/	Lista todas as despesas
GET	/expenses/<id>	Retorna uma despesa específica
POST	/expenses/	Cadastra uma nova despesa
PUT	/expenses/<id>	Atualiza uma despesa existente
DELETE	/expenses/<id>	Remove uma despesa
GET	/expenses/categoria/<categoria>	Lista despesas filtradas por categoria
GET	/expenses/resumo	Mostra resumo financeiro (total por categoria + geral)
GET	/expenses/resumo/html	Exibe gráfico de pizza do resumo
GET	/expenses/dashboard	Interface web com painel, pesquisa e CRUD visual
💻 Funcionalidades do Sistema
🧾 API RESTful

Adicionar, listar, editar e excluir despesas

Filtro por categoria

Resumo financeiro total e por categoria

🌈 Interface Visual (Dashboard)

Tabela interativa de despesas

Botões para adicionar, editar e deletar

Campo de pesquisa instantânea

Painel superior com totais por categoria

Atualização dinâmica via JavaScript (fetch API)

📊 Relatórios e Visualização

Gráfico de pizza mostrando o resumo financeiro

Interface responsiva e estilizada com HTML e CSS

🧰 Tecnologias Utilizadas
Tecnologia	Função
🐍 Python 3.8+	Linguagem base
⚙️ Flask 3.0.3	Framework web principal
🎨 HTML5 / CSS3	Interface visual
🧩 JavaScript (Fetch API)	Comunicação cliente-servidor
📊 Chart.js (CDN)	Visualização gráfica
🧱 Git / GitHub	Versionamento e publicação
🌿 Estratégia de Branches (Branch Strategy)

#--------------------------------------------------------------------#

O projeto segue uma estrutura simples e organizada:

main                → branch principal e estável
feature/dashboard   → desenvolvimento do painel interativo
feature/routes      → implementação das rotas e endpoints


Cada nova funcionalidade é desenvolvida em uma branch feature/ e depois mergeada na main através de commits descritivos (Conventional Commits).

🪶 Exemplo de Histórico de Commits
Commit	Descrição
feat: adicionar rotas principais da API	Criação das rotas GET, POST, PUT e DELETE
feat: implementar dashboard interativo com CRUD visual	Interface web com tabela e botões
fix: corrigir indentação no app.py	Ajuste de identação no Flask app
chore: adicionar requirements.txt e .gitignore	Configuração final de ambiente
docs: criar README.md completo	Documentação do projeto
🧾 Arquivo .gitignore

O projeto inclui um .gitignore configurado para ignorar:

venv/
__pycache__/
*.pyc
*.log
.env
.vscode/

📋 Status do Projeto
Funcionalidade	Status
CRUD de despesas	✅ Concluído
Filtro por categoria	✅ Concluído
Painel de resumo	✅ Concluído
Pesquisa de despesas	✅ Concluído
Interface web interativa	✅ Concluído
Visualização gráfica (Chart.js)	✅ Concluído
Exportação PDF/Excel	🔜 Planejado
🧠 Aprendizados

Durante o desenvolvimento desta API, foram aplicados conceitos de:

Estruturação main                → branch principal e estável
feature/dashboard   → desenvolvimento do painel interativo
feature/routes      → implementação das rotas e endpoints

📋 Status do Projeto
Funcionalidade	Status
CRUD de despesas	✅ Concluído
Filtro por categoria	✅ Concluído
Painel de resumo	✅ Concluído
Pesquisa de despesas	✅ Concluído
Interface web interativa	✅ Concluído
Visualização gráfica (Chart.js)	✅ Concluído
Exportação PDF/Excel	🔜 Planejado

✨ Autora

👩‍💻 Maria Licá
📅 Outubro de 2025
🎓 Projeto TDE — Módulo 1: Organização e Versionamento
🏫 Curso: Sistema de Informaçao
