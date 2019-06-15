from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import CadastroForm, AtualizarForm
from app.models import Mantimento, LogQuantidade

@app.route('/atualizar', methods=['GET', 'POST'])
def atualizar():
    form = AtualizarForm()
    if form.validate_on_submit():
        flash('Mantimento {} atualizado com sucesso!'.format(
            form.nome.data),'sucess')
        mantimento = Mantimento.query.filter_by(nome=form.nome.data).first()
        log = LogQuantidade(quantidadeAntiga=mantimento.quantidadeAtual, quantidadeNova=form.quantidadeAtual.data,
                            mantimento_id=mantimento.id)
        db.session.add(log)
        db.session.commit()
        mantimento.nome = form.novoNome.data
        mantimento.descricao = form.descricao.data
        mantimento.quantidadeAtual = form.quantidadeAtual.data
        mantimento.quantidadeMin = form.quantidadeMin.data
        mantimento.consumoDiario = form.consumoDiario.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('atualizar.html', title='Atualizar', form=form, db=db)

@app.route('/visualizar')
def visualizar():
    mantimento = Mantimento.query.all()
    return render_template('visualizar.html', title='Visualizar', mantimento = mantimento)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        flash('Mantimento {} cadastrado com sucesso!'.format(
            form.nome.data),'sucess')
        mantimento = Mantimento(nome=form.nome.data, descricao=form.descricao.data, quantidadeAtual=form.quantidadeAtual.data,
                                    quantidadeMin=form.quantidadeMin.data, consumoDiario=form.consumoDiario.data)
        db.session.add(mantimento)
        db.session.commit()
        mantimento = Mantimento.query.filter_by(nome=form.nome.data).first()
        log = LogQuantidade(quantidadeNova=form.quantidadeAtual.data, mantimento_id=mantimento.id)
        db.session.add(log)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('cadastro.html', title='Cadastrar Mantimento', form=form)

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', title='Home')
