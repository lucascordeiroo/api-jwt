# 🔐 API de Autenticação com JWT – Flask + SQLite

API RESTful desenvolvida com Flask e JWT (JSON Web Token) para autenticação de usuários. Permite registrar, fazer login e acessar rotas protegidas por token. Um projeto prático que simula autenticação real, ideal para portfólio de desenvolvedor backend.

---

## ✅ Funcionalidades

- 🔸 Registro de usuários com hash de senha
- 🔸 Login com retorno de token JWT
- 🔸 Proteção de rotas com autenticação
- 🔸 Banco de dados SQLite com SQLAlchemy
- 🔸 Testes via Postman ou Insomnia
- 🔸 Estrutura simples, clara e extensível

---

## 🛠 Tecnologias utilizadas

- Python 3
- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- Werkzeug (para hash de senhas)
- SQLite

---

## ▶️ Como executar

### 1. Clone o repositório
git clone https://github.com/lucascordeiroo/api-jwt.git
cd api-jwt-auth

2. Instale as dependências
pip install flask flask-jwt-extended flask-sqlalchemy

4. Execute a aplicação
python app.py

🔗 Endpoints disponíveis

🟢 POST /registro
Cria um novo usuário
Body (JSON):
{
  "username": "lucas",
  "senha": "123456"
}

🟢 POST /login
Realiza login e retorna um token de acesso
Body (JSON):
{
  "username": "lucas",
  "senha": "123456"
}

Resposta:
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhb..."
}

🔒 GET /protegido
Acesso restrito com token JWT

Header:
Authorization: Bearer SEU_TOKEN_AQUI

📂 Estrutura do projeto
api-jwt-auth/
├── app.py        # Lógica principal da API
├── models.py     # Modelo de dados (usuários)
└── banco.db      # Banco SQLite (gerado automaticamente)

👨‍💻 Autor
Desenvolvido por Lucas Cordeiro
📧 lucascordeirooliveira50@gmail.com
🔗 https://github.com/lucascordeiroo
