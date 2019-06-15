from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange, InputRequired, StopValidation
from app.models import Mantimento, LogQuantidade

class CadastroForm(FlaskForm):
    nome = StringField('Nome', validators=[InputRequired(message="Campo Obrigatório!"), Length(min=1, max=20, message='Máximo 20 caracteres')])
    descricao = TextAreaField('Descrição', validators=[Length(min=0, max=120, message='Máximo 120 caracteres')])
    quantidadeAtual = IntegerField('Quantidade Atual')
    quantidadeMin = IntegerField('Quantidade Mínima')
    consumoDiario = IntegerField('Consumo Diário')
    submit = SubmitField('Cadastrar')

    def validate_nome(self, nome):
        nome = Mantimento.query.filter_by(nome=nome.data).first()
        if nome:
            nome.errors = []
            raise ValidationError('Mantimento já cadastrado.')

    def validate_quantidadeAtual(self, quantidadeAtual):
        if (quantidadeAtual.data == None):
            quantidadeAtual.errors = []
            raise ValidationError('Preencha com números!')
        else:
            if quantidadeAtual.data>100 or quantidadeAtual.data<0:
                quantidadeAtual.errors = []
                raise ValidationError('Quantidade apenas de 0 até 100!')

    def validate_quantidadeMin(self, quantidadeMin):
        if (quantidadeMin.data == None):
            quantidadeMin.errors = []
            raise ValidationError('Preencha com números!')
        else:
            if quantidadeMin.data>100 or quantidadeMin.data<0:
                quantidadeMin.errors = []
                raise ValidationError('Quantidade apenas de 0 até 100!')

    def validate_consumoDiario(self, consumoDiario):
        if (consumoDiario.data == None):
            consumoDiario.errors = []
            raise ValidationError('Preencha com números!')
        else:
            if consumoDiario.data>100 or consumoDiario.data<0:
                consumoDiario.errors = []
                raise ValidationError('Quantidade apenas de 0 até 100!')

class AtualizarForm(FlaskForm):
    nome = StringField('Nome', validators=[InputRequired(message="Campo Obrigatório!"),
                                           Length(min=1, max=20, message='Máximo 20 caracteres')])
    novoNome = StringField('Novo Nome', validators=[InputRequired(message="Campo Obrigatório!"),
                                           Length(min=1, max=20, message='Máximo 20 caracteres')])
    descricao = TextAreaField('Descrição', validators=[Length(min=0, max=120, message='Máximo 120 caracteres')])
    quantidadeAtual = IntegerField('Quantidade Atual')
    quantidadeMin = IntegerField('Quantidade Mínima')
    consumoDiario = IntegerField('Consumo Diário')
    submit = SubmitField('Atualizar')

    def validate_nome(self, nome):
        nome = Mantimento.query.filter_by(nome=nome.data).first()
        if nome == None:
            raise ValidationError('Mantimento não cadastrado.')

    def validate_novoNome(self, novoNome):
        novoNome = Mantimento.query.filter_by(nome=novoNome.data).first()
        if novoNome:
            if novoNome.nome != self.nome.data:
                raise ValidationError('Nome já cadastrado.')

    def validate_quantidadeAtual(self, quantidadeAtual):
        if (quantidadeAtual.data == None):
            quantidadeAtual.errors = []
            raise ValidationError('Preencha com números!')
        else:
            if quantidadeAtual.data > 100 or quantidadeAtual.data < 0:
                quantidadeAtual.errors = []
                raise ValidationError('Quantidade apenas de 0 até 100!')

    def validate_quantidadeMin(self, quantidadeMin):
        if (quantidadeMin.data == None):
            quantidadeMin.errors = []
            raise ValidationError('Preencha com números!')
        else:
            if quantidadeMin.data > 100 or quantidadeMin.data < 0:
                quantidadeMin.errors = []
                raise ValidationError('Quantidade apenas de 0 até 100!')

    def validate_consumoDiario(self, consumoDiario):
        if (consumoDiario.data == None):
            consumoDiario.errors = []
            raise ValidationError('Preencha com números!')
        else:
            if consumoDiario.data > 100 or consumoDiario.data < 0:
                consumoDiario.errors = []
                raise ValidationError('Quantidade apenas de 0 até 100!')
