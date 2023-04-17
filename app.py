from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET','POST'])
def form_view():
    if request.method=='POST':
       name = request.form['name']
       email = request.form['email']
       file = request.files['file']
       gender = request.form['gender']
       city  = request.form['city']
       if file:
            filename = secure_filename(file.filename)
            file.save('static/'+filename)
            print(filename)
            print(name)
            print(email)
            print(gender)
            print(city)
    return render_template('form_input.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)
 