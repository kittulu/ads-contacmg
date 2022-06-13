from flask import Flask, request, render_template, redirect, flash, url_for
from View import User, UserId, Login, ViewDemands, Images, ViewCategories, viewMessage
from application import App
from flask_login import LoginManager, login_required,current_user,login_user, logout_user,login_required
import random, string, os

app = App.app()
app.secret_key = 'Innalhamdulillah.nahmaduhu.taalanastainubihi.wanastagfiruh!'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.config['MAX_CONTENT_LENGTH'] = 160 * 1000 * 1000
app.config['UPLOAD_FOLDER'] = "static/assets/images/upload"
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}

def take_extension(filename):
    arquivo, extensao = os.path.splitext(filename.filename)
    return extensao

def allowed_file(filename):
    return '.' in filename and \
   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def name_gen():
    return ''.join((random.choice(string.ascii_letters + string.digits) for i in range(16)))

@login_manager.user_loader
def load_user(user_id):
    return UserId.user_id(user_id)

@app.route("/")
@login_required
def index():
    categories = ViewCategories.get_categories()
    demands = ViewDemands.get_demands()[:4]
    print(demands)
    return render_template('index.html', cats=categories, dems=demands)


@app.route("/<id>")
@login_required
def index_by(id):
    if id == "0":
        categories = ViewCategories.get_categories()
        demands = ViewDemands.get_demands()
        title = 'Todas as Categorias'
    else:
        id=int(id)
        categories = ViewCategories.get_categories()
        demands = ViewCategories.get_by_categories(id)
        title = categories[(id-1)]
    return render_template('index_all.html', cats=categories, dems=demands, title=title)

@app.route("/login", methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        psw = request.form.get('psw')
        query_id = Login.login(email, psw) 
        if query_id:
            login_user(query_id)
            return redirect("/", code=302)
        else:
            return render_template("login.html", error="Usuario e/ou senha incorretos!")
    else:
        return render_template('login.html')

#@app.route('/user/')
#def profile(): pass
@app.route("/logout", methods = ['GET'])
def logout():
    logout_user()
    return redirect('/',code=302)



@app.route("/register", methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('name')
        last_name = request.form.get('lname')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        cpf = request.form.get('cpfcnpj')
        psw = request.form.get('psw') 
        f = request.files.get('file')
        img= name_gen()+take_extension(f)
        if f:
            if allowed_file(f.filename):
                reg = Login.register(first_name,last_name, telefone, email, cpf, psw, img)
                f.save(dst=f"static/assets/images/uploads/{img}")
            else:
                return render_template('register.html', error='Imagem Inválida')
        else:
            img = None
            reg = Login.register(first_name,last_name, telefone, email, cpf, psw, img)
        if reg == 'shuu':
            return redirect("/login", code=302)
        else:
            return render_template('register.html', error=reg)
    else:
        return render_template('register.html')


@app.route("/demand/<id>", methods = ['GET'])
def ViewDemand(id):
    user=current_user
    current = ViewDemands.get_demand(id)
    print(current[4])
    
    content = ViewDemands.get_demands()[2:6]
    proposal = ViewDemands.get_proposal(int(id))
    print(proposal)
    return render_template('product.html', content=content, proposal=proposal, curr= current,user=user)

@app.route("/cadastrodemanda", methods = ['GET','POST'])
@login_required
def cadastrodemandas():
    categories = ViewCategories.get_categories()

    if request.method == 'POST':
        demand_name = request.form.get('name')
        desc = request.form.get('desc')
        category_id = int(request.form.get('cat'))
        user_id = current_user.id
        f = request.files.get('file')
        img= name_gen()+take_extension(f)
        if f:
            if allowed_file(f.filename):
                reg = ViewDemands.post_demand(demand_name,desc,category_id,user_id,img)
                f.save(dst=f"static/assets/images/uploads/{img}")
            else:
                return render_template('cadservice.html', cats=categories, error="Imagem inválida", cor='#ff0000')
        else:
            img = None
            reg = ViewDemands.post_demand(demand_name,desc,category_id,user_id,img)
        if reg == 'shuu':
            return render_template('cadservice.html', cats=categories, error="Cadastrado com sucesso!", cor='#00f56e')
        else:
            return render_template('cadservice.html', cats=categories, error="Algo deu errado, tente novamente.", cor='#ff0000')
    else:
        return  render_template('cadservice.html', error='', cor='',cats=categories)

@app.route("/criarproposta/<id>", methods = ['GET','POST'])
@login_required
def criarproposta(id):
    if request.method == 'POST':
        desc = request.form.get('desc')
        user_id = current_user.id
        demand_id = id
        ViewDemands.post_proposal(desc, demand_id, user_id)
        returnvalue = ViewDemands.get_demand(int(id))
        return render_template('cadproposta.html', error="Cadastrado com sucesso!",  value=returnvalue)
    else:
        returnvalue = ViewDemands.get_demand(int(id))
        print(returnvalue)
        return  render_template('cadproposta.html', value=returnvalue)


@app.route("/perfil", methods = ['GET'])
@login_required
def perfil():
    user = current_user
    return render_template('perfil.html', user=user)

@app.route("/perfil/editar", methods = ['GET','POST'])
@login_required
def editarperfil():
    user = current_user
    if request.method == 'POST':
        first_name = request.form.get('name')
        last_name = request.form.get('lname')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        cpf = request.form.get('cpfcnpj')
        psw = request.form.get('psw') 
        f = request.files.get('file')
        img=user.img_path
        if f:
            if allowed_file(f.filename):
                reg = Login.update(user.id,first_name,last_name, telefone, email, cpf, psw, img)
                f.save(dst=f"static/assets/images/uploads/{img}")
            else:
                return render_template('profile-setting.html', error='Imagem Inválida', user=user)
        else:
            reg = Login.update(user.id, first_name,last_name, telefone, email, cpf, psw, img)
        if reg == 'shuu':
            return redirect("/perfil", code=302)
        else:
            return render_template('profile-setting.html', error=reg, user=user)
    else:
        return render_template('profile-setting.html', code=302, user=user)



@app.route("/chat/<id>", methods = ['GET','POST'])
@login_required
def chat(id):
    users = current_user
    user2 = UserId.user_id(id)
    message=''
    if request.method == 'POST':
        content= request.form.get('send')
        viewMessage.sendmessage(int(users.id), int(user2.id), content)
        message = viewMessage.get_message(users.id, id)
        return render_template('chat.html', message=message, users=users, user2=user2)
    else:
        message = viewMessage.get_message(int(users.id),int(user2.id))
        if not message:
            return render_template('chat.html', message=message, users=users, user2=user2)
        else:
            return render_template('chat.html', message=message, users=users, user2=user2)


@app.route("/historico", methods = ['GET','POST'])
@login_required
def historico():
    user=current_user
    users=[]
    chats=viewMessage.chats(user.id)
    for i in chats:
        print (i)
        users.append(UserId.user_id(i))
    return render_template('history.html', users=users, user=user)
##
# @app.route("/proposta", methods = ['GET','POST'])
# @login_required
# def cadastroproposta():
#     if request.method == 'POST':
#         desc = request.form.get('desc')
#         desc = request.form.get('desc')
#         category_id = int(request.form.get('cat'))-1
#         user_id = current_user.id
#         print(request.form)
#         reg = ViewDemands.post_demand(demand_name,desc,category_id,user_id)
#         return render_template('cadservice.html', error="Cadastrado com sucesso!")

#     else:
#         return  render_template('cadservice.html')
