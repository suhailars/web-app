from flask import Flask, render_template,request
import psycopg2
import os 
app = Flask(__name__)     
 
@app.route('/')
def home():
  return render_template('home.html')
@app.route('/about')
def about():
  return render_template('about.html')
@app.route('/post')
def post():
    return render_template('post.html') 
@app.route('/post',methods=['POST'])
def add_entry():    
    con = psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)
  
    cur = con.cursor()  
    cur.execute("INSERT INTO blog (author,post) VALUES (%s,%s)",  (request.form['name'],request.form['blogpost']))
    #con.commit()
    #con.close()  
    #return render_template('post.html')
    #con = psycopg2.connect(database='testdb', user='suhail') 
    
    #cur = con.cursor()     
    cur.execute("SELECT * FROM blog ORDER BY id desc") 
    posts=[dict(id=i[0],author=i[1],post=i[2]) for i in cur.fetchall()]
    con.commit()
    con.close()        
    if not posts:
         return render_template('post.html')
    else:
         return render_template('post.html',posts=posts)      

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
