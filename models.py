from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin): # Adicionei UserMixin aqui e classe adicionada
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(350), unique=True, nullable=False)
    password = db.Column(db.String(350), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    

# de usuario passou para colaborador
class Colaborador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomecompleto = db.Column(db.String(200), nullable=True)
    cadastro_em = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    receitas = db.relationship('Receita', backref='colaborador', lazy=True) #ok
    despesas = db.relationship('Despesas', backref='colaborador', lazy=True) #ok

    def __repr__(self):
        return f'<Venda {self.nomecompleto}>'


class Receita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    receita = db.Column(db.Float, nullable=True) ####
    receitaatualizada_em = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    colaborador_id = db.Column(db.Integer, db.ForeignKey('colaborador.id'), nullable=False) # FK relacionado com a tabela Colaborador
   
    def __repr__(self):
        return f'<Cliente {self.receita}>'
    
    
class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomecategoria = db.Column(db.String(200), nullable=True)
    despesas = db.relationship('Despesas', backref='categoria', lazy=True) #ok
    
    def __repr__(self):
        return f'<Categoria {self.nomecategoria}>'


class Despesas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False) # FK
    colaborador_id = db.Column(db.Integer, db.ForeignKey('colaborador.id'), nullable=False) #FK
    despesasatualizada_em = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    escolagrazi = db.Column(db.Float, nullable=True)
    escolafelipe = db.Column(db.Float, nullable=True)
    escolakaique = db.Column(db.Float, nullable=True)
    contaagua = db.Column(db.Float, nullable=True)
    contaluz = db.Column(db.Float, nullable=True)
    contatelefone = db.Column(db.Float, nullable=True)
    tv = db.Column(db.Float, nullable=True)
    internet = db.Column(db.Float, nullable=True)
    condominio = db.Column(db.Float, nullable=True)
    mercado = db.Column(db.Float, nullable=True)
    cartaocredito = db.Column(db.Float, nullable=True)
    roupas = db.Column(db.Float, nullable=True)
    passeio = db.Column(db.Float, nullable=True)
    farmacia = db.Column(db.Float, nullable=True)
    estacionamento = db.Column(db.Float, nullable=True)
    materialescolar = db.Column(db.Float, nullable=True)
    ipva = db.Column(db.Float, nullable=True)
    dpvat = db.Column(db.Float, nullable=True)
    licenciamento = db.Column(db.Float, nullable=True)
    iptu = db.Column(db.Float, nullable=True)
    consorcio = db.Column(db.Float, nullable=True)
    viagem = db.Column(db.Float, nullable=True)
    gastoextra = db.Column(db.Float, nullable=True)
    seguro = db.Column(db.Float, nullable=True)
    cursoingles = db.Column(db.Float, nullable=True)
    dentiste = db.Column(db.Float, nullable=True)
    restauramntefast = db.Column(db.Float, nullable=True)
    cabeleireiro = db.Column(db.Float, nullable=True)
    cursokumon = db.Column(db.Float, nullable=True)
    aluguel = db.Column(db.Float, nullable=True)
    prestacaocasa = db.Column(db.Float, nullable=True)
    prestacaocarro = db.Column(db.Float, nullable=True)
    contagas= db.Column(db.Float, nullable=True)
    irpf = db.Column(db.Float, nullable=True)
    emprestimobb = db.Column(db.Float, nullable=True)
    lavagemcarro = db.Column(db.Float, nullable=True)
    combustivel = db.Column(db.Float, nullable=True)
    manutencaocarro = db.Column(db.Float, nullable=True)
    bilheteunico = db.Column(db.Float, nullable=True)
    encargosjuros = db.Column(db.Float, nullable=True)
    consultamedica = db.Column(db.Float, nullable=True)
    jogosgame = db.Column(db.Float, nullable=True)

    
    def __repr__(self):
        return f'<Despesas {self.escolagrazi}>'