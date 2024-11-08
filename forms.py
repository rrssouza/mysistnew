from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, IntegerField, FloatField, SubmitField, DateTimeField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo
from datetime import datetime


class LoginForm(FlaskForm): #adicionado
    username = StringField('Usuário', validators=[DataRequired(), Length(min=3, max=150)])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')


class RegisterForm(FlaskForm): #adicionado
    username = StringField('Usuário', validators=[DataRequired(), Length(min=3, max=150)])
    password = PasswordField('Senha', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrar')

#####################################################################################################################################
class ColaboradorForm(FlaskForm):
    nomecompleto = StringField('Nome', validators=[DataRequired()])
    cadastro_em = DateTimeField('Atualizado Em', default=datetime.now, format='%Y-%m-%d %H:%M:%S')
    
    
class ReceitaForm(FlaskForm):
    salario = FloatField('Salário', validators=[DataRequired()])
    receitaatualizada_em = DateTimeField('Receita Atualizada Em', default=datetime.now, format='%Y-%m-%d %H:%M:%S')
    colaborador_id = SelectField('Categoria', coerce=int)

class CategoriaForm(FlaskForm):
    nomecategoria = StringField('Nome Categoria', validators=[DataRequired()])


class DespesasForm(FlaskForm):
    categoria_id = SelectField('Categoria', coerce=int)
    colaborador_id = SelectField('Categoria', coerce=int)
    despesasatualizada_em = DateTimeField('Receita Atualizada Em', default=datetime.now, format='%Y-%m-%d %H:%M:%S')
    
    escolagrazi = FloatField('Escola da Grazi', validators=[DataRequired()])
    escolafelipe = FloatField('Escola do Felipe', validators=[DataRequired()])
    escolakaique = FloatField('Escola Kaique', validators=[DataRequired()])
    contaagua = FloatField('Conta de Agua', validators=[DataRequired()])
    contaluz = FloatField('Conta de Luz', validators=[DataRequired()])
    contatelefone = FloatField('Conta Smartfone', validators=[DataRequired()])
    tv = FloatField('Conta TV', validators=[DataRequired()])
    internet = FloatField('Internet Vivo', validators=[DataRequired()])
    condominio = FloatField('Condominio', validators=[DataRequired()])
    mercado = FloatField('Mercado', validators=[DataRequired()])
    
    cartaocredito = FloatField('Cartão de Crédito', validators=[DataRequired()])
    roupas = FloatField('Compra de Roupas', validators=[DataRequired()])
    passeio = FloatField('Passeio', validators=[DataRequired()])
    farmacia = FloatField('Farmacia', validators=[DataRequired()])
    estacionamento = FloatField('Estacionamento', validators=[DataRequired()])
    materialescolar = FloatField('Material Escolar', validators=[DataRequired()])
    ipva = FloatField('IPVA', validators=[DataRequired()])
    dpvat = FloatField('DPVAT', validators=[DataRequired()])
    licenciamento = FloatField('Licenciamento', validators=[DataRequired()])
    iptu = FloatField('IPTU', validators=[DataRequired()])
    
    consorcio = FloatField('Consorcio', validators=[DataRequired()])
    viagem = FloatField('Viagem', validators=[DataRequired()])
    gastoextra = FloatField('Gastos Extra', validators=[DataRequired()])
    seguro = FloatField('Seguro', validators=[DataRequired()])
    cursoingles = FloatField('Curso de Inglês', validators=[DataRequired()])
    dentiste = FloatField('Dentista', validators=[DataRequired()])
    restauramntefast = FloatField('Restaurante fastfood', validators=[DataRequired()])
    cabeleireiro = FloatField('Cabeleireiro', validators=[DataRequired()])
    cursokumon = FloatField('Kumon', validators=[DataRequired()])
    aluguel = FloatField('Aluguel', validators=[DataRequired()])
    
    prestacaocasa = FloatField('Prestação da Casa', validators=[DataRequired()])
    prestacaocarro = FloatField('Prestação do Carro', validators=[DataRequired()])
    contagas= FloatField('Conta de Gás', validators=[DataRequired()])
    irpf = FloatField('IRPF', validators=[DataRequired()])
    emprestimobb = FloatField('Empréstimo BB', validators=[DataRequired()])
    lavagemcarro = FloatField('Lavagem do Carro', validators=[DataRequired()])
    combustivel = FloatField('Combustivel', validators=[DataRequired()])
    manutencaocarro = FloatField('Manutenção Carro', validators=[DataRequired()])
    bilheteunico = FloatField('Bilhete Único', validators=[DataRequired()])
    encargosjuros = FloatField('Encargos Juros', validators=[DataRequired()])
    
    consultamedica = FloatField('Consulta Médica', validators=[DataRequired()])
    jogosgame = FloatField('Jogos Xbox', validators=[DataRequired()])
    submit = SubmitField('Adicionar Despesas Mensal')

