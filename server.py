from flask import Flask, redirect, render_template,request,session,url_for

print('started')

app = Flask(__name__)
app.secret_key = "very secret key"
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Ahmed9112",
  database="hospital"
)

mycursor = mydb.cursor()

@app.route('/')
def base():
   print('base')
   return render_template('Base.html')

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == 'POST':
        userEmail = request.form['email']
        password = request.form['password']
        mycursor.execute("SELECT * FROM USERS WHERE email = %s AND password = %s",(userEmail,password))
        record = mycursor.fetchone()
        
        if record:
            session['user'] = userEmail
            session['loggedIn'] = True
            return render_template('base.html')
        else:
            print(111111)
            return render_template('login.html',msg = True)
    else:
        print(0000000)
        return render_template('login.html',msg = False)
  
@app.route('/signUp')
def signUp():
    if request.method == 'GET':
        return render_template('signUp.html')
    else:
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        
        mycursor.execute("INSET INTO USERS (email,password) VALUES (%s,%s)",(email,password))
        mydb.commit()
        
        session['name'] = name
        session['email'] = email
        return redirect(url_for('base'))

@app.route("/logout")
def logout():
    session.pop('loggedin',None)
    session.pop('user',None)
    session.clear()
    # return render_template('Base.html')
    return redirect(url_for('base'))


@app.route('/adddoctor',methods = ['POST','GET'])
def adddoctor():
    if request.method == 'POST':
        name = request.form['name1']
        dep = request.form['dep1']
        sql = "INSERT INTo DOCTOR (name,department) VALUES (%s,%s)"
        val = (name,dep)
        mycursor.execute(sql,val)
        mydb.commit()
        return render_template('index.html')
    else:
        print('get')
        return render_template('adddoctor.html')


@app.route('/viewdoctor')
def viewdoctor():
   sql = "SELECT * FROM DOCTOR"
   mycursor.execute(sql)
   result = mycursor.fetchall()
   return render_template('viewdoctor.html',data = result)

@app.route('/services')
def services():
    return("flask")

@app.route('/doctors')
def doctors():
    return("doctors")        

if __name__ == '__main__':
    app.run(debug = True)