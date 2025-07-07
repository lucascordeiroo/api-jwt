from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from models import db, Usuario
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["JWT_SECRET_KEY"] = "minha-chave-secreta"  # 🔐 Troque por algo seguro
db.init_app(app)
jwt = JWTManager(app)

# Inicializa o banco
with app.app_context():
    db.create_all()


# Rota de registro
@app.route("/registro", methods=["POST"])
def registro():
    dados = request.get_json()
    username = dados.get("username")
    senha = dados.get("senha")

    if Usuario.query.filter_by(username=username).first():
        return jsonify({"msg": "Usuário já existe"}), 409

    usuario = Usuario(username=username, senha=generate_password_hash(senha))
    db.session.add(usuario)
    db.session.commit()
    return jsonify({"msg": "Usuário criado com sucesso!"}), 201

# Rota de login
@app.route("/login", methods=["POST"])
def login():
    dados = request.get_json()
    username = dados.get("username")
    senha = dados.get("senha")

    usuario = Usuario.query.filter_by(username=username).first()
    if not usuario or not check_password_hash(usuario.senha, senha):
        return jsonify({"msg": "Credenciais inválidas"}), 401

    token = create_access_token(identity=usuario.id)
    return jsonify(access_token=token)

# Rota protegida
@app.route("/protegido", methods=["GET"])
@jwt_required()
def rota_protegida():
    return jsonify({"msg": "Acesso autorizado à rota protegida!"})

if __name__ == "__main__":
    app.run(debug=True)
