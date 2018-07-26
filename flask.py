from flask import Flask,render_template, request
#import pymysql.cursors

import MySQLdb
def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "l",
                           db = "project")
    c = conn.cursor()
    return c, conn	


app =Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/validation' ,methods = ['GET','POST'])
def validation():

	try:
		c, conn = connection()
		if request.method=='POST':
			name = request.form['Name']
			contact = request.form['contact']
			email = request.form['Name']
			password = request.form['Name']
			city = request.form['Name']
		
			return email
			
			x = c.execute("SELECT * FROM users WHERE email = (%s)",(Email))

			if int(x) > 0:
				flash("username exist, please try something different")
				return render_template('register.html')
			else:
				try:
#					with conn.cursor() as cur:

					sql = "INSERT INTO validation (name,contact,email,password,city,) VALUES (%s, %s, %s, %s)"
					c.execute(sql,(Name,Contact,Email,Password,City))
					conn.commit()
					msg = "thanks for registering!!"
					return render_template('login.html', msg = msg)
					c.close()
					#conn.close()
				except:
					conn.rollback()
					msg = "error in insertion.."
#					return "e"
					return render_template('register.html', msg = msg)

				finally:
					c.close()
					conn.close()

	except:
		msg = "error"
		return render_template('register.html', msg = msg)




'''@app.route('/login/', methods=["GET","POST"])
def login_page():
    error = ''
    try:
        c, conn = connection()
        if request.method == "POST":
			     
        	username = request.form['Name']
		password = request.form['contact']
                data = c.execute("SELECT * FROM users WHERE username = (%s)",('username'))
            
                data = c.fetchone()[2]

          #  if sha256_crypt.verify(password, data):
           #     session['logged_in'] = True
            #    session['username'] = username

             #   flash("You are now logged in")
              #  return redirect(url_for("dashboard"))

        else:
                error = "Invalid credentials, try again."

        gc.collect()

        return render_template("login.html", error=error)

    except Exception as e:
        #flash(e)
        error = "Invalid credentials, try again."
        return render_template("login.html", error = error)'''
		


if __name__ == '__main__':
	app.run(debug = True)
