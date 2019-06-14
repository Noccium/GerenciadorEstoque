from datetime import datetime, timezone, timedelta
from app import db

class Mantimento(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(120), unique = True, nullable = False)
    descricao = db.Column(db.Text, nullable = True, default='-')
    quantidadeAtual = db.Column(db.Integer, nullable = False, default=0)
    quantidadeMin = db.Column(db.Integer, nullable = False, default=0)
    consumoDiario = db.Column(db.Integer, nullable = False, default=0)
    logQuantidade = db.relationship('LogQuantidade', backref='mantimento', lazy=True)

    def __repr__(self):
        return f"Mantimento(nome: '{self.nome}', descricao: '{self.descricao}', quantidadeAtual: '{self.quantidadeAtual}', quantidadeMin: '{self.quantidadeMin}', consumoDiario: '{self.consumoDiario}')"

class LogQuantidade(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    quantidadeNova = db.Column(db.Integer, nullable = False, default=0)
    quantidadeAntiga = db.Column(db.Integer, nullable = False, default=0)
    data = db.Column(db.DateTime, nullable = False, default=datetime.utcnow().astimezone(timezone(timedelta(minutes=+2,hours=-3))))
    mantimento_id = db.Column(db.Integer, db.ForeignKey('mantimento.id'), nullable = False)

    def __repr__(self):
        return f"Log('{self.quantidadeNova}', '{self.quantidadeAntiga}', '{self.data}')"
