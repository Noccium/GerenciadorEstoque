from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import CadastroForm
from app.models import Mantimento, LogQuantidade

@app.route('/visualizar')
def visualizar():
    mantimento = Mantimento.query.all()
    return render_template('visualizar.html', title='Visualizar Mantimento', mantimento = mantimento)

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
