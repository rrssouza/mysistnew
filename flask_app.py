# Database alterado de SQLite para PostgreSQL;
# Adicionado novas rotas;
# Adicionado novas Classes de Formulários
# Adicionado novas Classes de tabelas de banco de dados Postgres
# Nessa versão six foi alterado o database de Postgresql para MySQL
from flask import Flask, render_template, redirect, url_for, flash
from models import db, User, Colaborador, Receita, Categoria, Despesas
from forms import LoginForm, RegisterForm, ColaboradorForm, DespesasForm
from sqlalchemy import desc, asc
from config import Config
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'
app.config.from_object(Config)

db.init_app(app)

@app.before_request
def create_tables():
    db.create_all() #cria as tabelas no database


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuário ou senha incorretos.', 'danger')
    return render_template('login.html', form=form)



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registro bem-sucedido! Agora você pode fazer login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você foi desconectado.', 'info')
    return redirect(url_for('login'))


@app.route('/home')
@login_required
def home():
    return render_template('home.html')


@app.route('/despesas', methods=['GET', 'POST']) #Route
@login_required
def index(): # Função

    form = DespesasForm()
    form.categoria_id.choices = [(categoria.id, categoria.nomecategoria) for categoria in Categoria.query.all()]
    if form.validate_on_submit():
        nova_despesa = Despesas(escolagrazi = form.escolagrazi.data,
                                categoria_id = form.categoria_id.data,
                                despesasatualizada_em = form.despesasatualizada_em.data,
                                escolafelipe = form.escolafelipe.data,
                                escolakaique = form.escolakaique.data,
                                contaagua = form.contaagua.data,
                                contaluz = form.contaluz.data,
                                contatelefone = form.contatelefone.data,
                                tv = form.tv.data,
                                internet = form.internet.data,
                                condominio = form.condominio.data,
                                mercado = form.mercado.data,
                                cartaocredito = form.cartaocredito.data,
                                roupas = form.roupas.data,
                                passeio = form.passeio.data,
                                farmacia = form.farmacia.data,
                                estacionamento = form.estacionamento.data,
                                materialescolar = form.materialescolar.data,
                                ipva = form.ipva.data,
                                dpvat = form.dpvat.data,
                                licenciamento = form.licenciamento.data,
                                iptu = form.iptu.data,
                                consorcio = form.consorcio.data,
                                viagem = form.viagem.data,
                                gastoextra = form.gastoextra.data,
                                seguro = form.seguro.data,
                                cursoingles = form.cursoingles.data,
                                dentiste = form.dentiste.data,
                                restauramntefast = form.restauramntefast.data,
                                cabeleireiro = form.cabeleireiro.data,
                                cursokumon = form.cursokumon.data,
                                aluguel = form.aluguel.data,
                                prestacaocasa = form.prestacaocasa.data,
                                prestacaocarro = form.prestacaocarro.data,
                                contagas = form.contagas.data,
                                irpf = form.irpf.data,
                                emprestimobb = form.emprestimobb.data,
                                lavagemcarro = form.lavagemcarro.data,
                                combustivel = form.combustivel.data,
                                manutencaocarro = form.manutencaocarro.data,
                                bilheteunico = form.bilheteunico.data,
                                encargosjuros = form.encargosjuros.data,
                                consultamedica = form.consultamedica.data,
                                jogosgame = form.jogosgame.data)
        db.session.add(nova_despesa)
        db.session.commit()
        flash('Despesas adicionada com sucesso!', 'success')
        return redirect(url_for('index')) #redireciona para função index()
    # Consulta para trazer somente os cinco ultimos registros de Despesas
    despesas = Despesas.query.order_by(desc(Despesas.despesasatualizada_em)).limit(5).all() # Será necessário add campo Data p/ ordenação funcionar corretamente.

    #despesas = Despesas.query.all()
    return render_template('despesas.html', form=form, despesas=despesas)

@app.route('/cliente')
@login_required
def cliente():
    return render_template('cliente.html')


#if __name__ == '__main__':
#    app.run(debug=True)
#