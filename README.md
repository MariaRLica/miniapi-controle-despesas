# 💰 Mini API - Controle de Despesas

API desenvolvida em **Flask (Python)** para o controle e visualização de despesas pessoais.  
Inclui **CRUD completo**, **filtro por categoria**, **resumo financeiro**, e **dashboard interativo** com gráficos e pesquisa dinâmica.

---

## 🧩 Como executar

### 🌀 Clonar o repositório
```bash
git clone https://github.com/seu-usuario/miniapi-controle-despesas.git
cd miniapi-controle-despesas
```

### 🧱 Criar ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate   # Linux
venv\Scripts\activate      # Windows
```

### 📦 Instalar dependências
```bash
pip install -r requirements.txt
```

### ▶️ Rodar a aplicação
```bash
python -m src.app
```

Acesse no navegador:  
👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🌍 Endpoints principais

| Método | Rota | Descrição |
|:------:|:-------------------------------|:----------------------------------|
| GET | `/expenses/` | Lista todas as despesas |
| GET | `/expenses/<id>` | Busca despesa específica |
| POST | `/expenses/` | Adiciona nova despesa |
| PUT | `/expenses/<id>` | Atualiza uma despesa |
| DELETE | `/expenses/<id>` | Remove uma despesa |
| GET | `/expenses/categoria/<categoria>` | Filtra por categoria |
| GET | `/expenses/resumo` | Mostra resumo financeiro |
| GET | `/expenses/dashboard` | Interface web interativa |

---

## 🧭 Estrutura de Diretórios

```
miniapi/
│
├── src/
│   ├── app.py             # Configuração principal do Flask
│   ├── models.py          # "Banco de dados" em memória e funções CRUD
│   ├── routes.py          # Rotas e endpoints da API
│   ├── config.py          # Configurações adicionais
│   └── templates/
│       └── dashboard.html  # Interface web interativa
│
├── requirements.txt        # Dependências do projeto
├── .gitignore              # Arquivos e pastas ignorados no Git
└── README.md               # Documentação do projeto
```

---

## ⚙️ Funcionalidades do Sistema

### 🧾 API RESTful
- Adicionar, listar, editar e excluir despesas  
- Filtro por categoria  
- Resumo financeiro total e por categoria  

### 🌈 Interface Visual (Dashboard)
- Tabela interativa de despesas  
- Botões para **Adicionar**, **Editar**, e **Excluir**  
- Campo de **pesquisa instantânea**  
- Painel superior com totais por categoria  
- Atualização dinâmica via JavaScript (Fetch API)  

### 📊 Relatórios e Visualização
- Gráfico de **pizza (Chart.js)** mostrando o resumo financeiro  
- Interface responsiva e estilizada com HTML e CSS  

---

## 🧰 Tecnologias Utilizadas

| Tecnologia | Função |
|:-----------|:--------|
| 🐍 Python 3.8+ | Linguagem base |
| ⚙️ Flask 3.0.3 | Framework web principal |
| 🎨 HTML5 / CSS3 | Interface visual |
| 🧩 JavaScript (Fetch API) | Comunicação cliente-servidor |
| 📊 Chart.js (CDN) | Visualização gráfica |
| 🧱 Git / GitHub | Versionamento e publicação |

---

## 🌿 Estratégia de Branches

O projeto segue uma estrutura simples e organizada:

| Branch | Descrição |
|:--------|:------------------------------------------|
| `main` | Branch principal e estável |
| `feature/dashboard` | Desenvolvimento do painel interativo |
| `feature/routes` | Implementação das rotas e endpoints |

Cada nova funcionalidade é desenvolvida em uma `branch feature/`  
e depois mergeada na `main` através de **commits descritivos (Conventional Commits)**.

---

## 🪶 Exemplo de Histórico de Commits

| Commit | Descrição |
|:-------|:-------------------------------------------|
| `feat: adicionar rotas principais da API` | Criação das rotas GET, POST, PUT e DELETE |
| `feat: implementar dashboard interativo com CRUD visual` | Interface web com tabela e botões |
| `fix: corrigir indentação no app.py` | Ajuste de indentação |
| `chore: adicionar requirements.txt e .gitignore` | Configuração final de ambiente |
| `docs: criar README.md completo` | Documentação do projeto |

---

## 🧾 Arquivo `.gitignore`

O projeto inclui um `.gitignore` configurado para ignorar:

```
venv/
__pycache__/
*.pyc
*.log
.env
.vscode/
```

---

## 📋 Status do Projeto

| Funcionalidade | Status |
|:-----------------------------|:-----------:|
| CRUD de despesas | ✅ Concluído |
| Filtro por categoria | ✅ Concluído |
| Painel de resumo | ✅ Concluído |
| Pesquisa de despesas | ✅ Concluído |
| Interface web interativa | ✅ Concluído |
| Visualização gráfica (Chart.js) | ✅ Concluído |
| Exportação PDF/Excel | 🔜 Planejado |

---

## 🧠 Aprendizados

Durante o desenvolvimento desta API, foram aplicados conceitos de:
- Estrutura de rotas e modularização no Flask  
- Versionamento com Git e GitHub  
- Organização de branches (`main` e `feature/`)  
- Commits descritivos seguindo **Conventional Commits**  
- Desenvolvimento de **interface web dinâmica** com Chart.js e Fetch API  

---

## ✨ Autora

👩‍💻 **Maria Licá**  
📅 **Outubro de 2025**  
🎓 **Projeto TDE — Módulo 1: Organização e Versionamento**  
🏫 **Curso: Sistema de Informação**

---

📌 **Repositório público:**  
🔗 [https://github.com/seu-usuario/miniapi-controle-despesas](https://github.com/seu-usuario/miniapi-controle-despesas)
