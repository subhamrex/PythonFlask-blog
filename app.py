from flask import Flask, render_template,request,session,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import pymysql
import os
import math
import json
# import socket
# socket.getaddrinfo('localhost', 25)

with open ("config.json", 'r') as c:
    params = json.load(c)["params"]
local_server = True
app = Flask(__name__)
app.secret_key = 'the random string'
app.config['UPLOAD_FOLDER'] = params['upload_loc']

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail_user'],
    MAIL_PASSWORD=  params['gmail_pass'] 
)
mail = Mail(app)
if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)

class Contacts(db.Model):
    '''
    SLNo, name, phn_no, msg, date, email
    '''
    SLNo = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phn_no = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

class Posts(db.Model):
    '''
   
    '''
    SLNo = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    slug= db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(30), nullable=True)
    content = db.Column(db.String(120), nullable=False)    
    img_file = db.Column(db.String(50), nullable=True)
@app.route("/",methods=['GET'])
def index():
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(params['no_of_posts']))
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page-1)*int(params['no_of_posts']): (page-1)*int(params['no_of_posts'])+ int(params['no_of_posts'])]    
    if (page==1):
        prev="#"
        next="/?page="+ str(page+1) 

    elif (page ==last):
        next="#"
        prev="/?page="+ str(page-1) 

    else:
        next="/?page="+ str(page+1)  
        prev="/?page="+ str(page-1)     

    return render_template('index.html',params=params,posts =posts,prev=prev,next=next)


@app.route("/about")
def about():
    return render_template('about.html',params=params)

@app.route("/login",methods=['GET','POST'])
def dash():
    if ('user' in session and session['user']== params['admin_user']):
        posts =Posts.query.all()
        return render_template('dash.html',params=params,posts=posts)

    if(request.method=="POST"):
        username = request.form.get('user')
        userpass = request.form.get('pass')
        if (username == params['admin_user'] and userpass == params['admin_password']):
            session['user']= username
            posts =Posts.query.all()
            return render_template('dash.html',params=params,posts=posts)
    return render_template('login.html',params=params)

@app.route("/uploader",methods=['GET','POST'])
def uploader():
    
    if ('user' in session and session['user']== params['admin_user']):
        if(request.method=="POST"):
            f = request.files['myfile']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
            return redirect('/login')       
        return render_template('dash.html',params=params)         

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect("/login")

@app.route("/del/<string:SLNo>",methods=['GET','POST'])
def delpost(SLNo):
    if ('user' in session and session['user']== params['admin_user']):
        post = Posts.query.filter_by(SLNo=SLNo).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/login')    

@app.route("/contact", methods =['GET','POST'])
def contact():
    if(request.method=="POST"):
        name = request.form.get('name')
        phn_no = request.form.get('phn_no')
        msg = request.form.get('msg')
        email = request.form.get('email')
        entry = Contacts(name=name, phn_no = phn_no, msg = msg, date= datetime.now(),email = email )
        db.session.add(entry)
        db.session.commit()
        mail.send_message("New message from "+ name,sender= email,recipients= [params['gmail_user']],body= msg + "\n" + phn_no)
        flash("Thanks for submitting your details","success")
    return render_template('contact.html',params=params)


@app.route("/Addpost",methods=['GET','POST'])
def addpost():
    if ('user' in session and session['user']== params['admin_user']):
        if(request.method=="POST"):
            edit_title1 = request.form.get('title')
            edit_slug1 = request.form.get('slug')
            edit_content1 = request.form.get('content')
            edit_img_file1 = request.form.get('img_file')
            date1 = datetime.now()
            post = Posts(title = edit_title1,slug = edit_slug1,content=edit_content1,img_file = edit_img_file1,date = date1)
            db.session.add(post)
            db.session.commit()
            return redirect('/Addpost') 
        return render_template('newpost.html',params = params)    


@app.route("/edit/<string:SLNo>",methods=['GET','POST'])
def edit(SLNo):
    if ('user' in session and session['user']== params['admin_user']):
        if(request.method=="POST"):
            edit_title = request.form.get('title')
            edit_slug = request.form.get('slug')
            edit_content = request.form.get('content')
            edit_img_file = request.form.get('img_file')
            date = datetime.now()
            post = Posts.query.filter_by(SLNo=SLNo).first()  
            post.title = edit_title  
            post.slug = edit_slug
            post.content = edit_content
            post.img_file = edit_img_file
            post.date = date
            db.session.commit()
            return redirect('/edit/'+SLNo) 

        post = Posts.query.filter_by(SLNo=SLNo).first()
        return render_template('edit.html',params = params,post=post)

@app.route("/post/<string:post_slug>",methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)


app.run(debug=True)
