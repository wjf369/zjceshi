
from flask import Flask
app = Flask(__name__)
app.debug=True

@app.route('/')
def hello_world():  #  http://127.0.0.1:5000
    return 'hello_world'

@app.route('/login')  # http://127.0.0.1:5000/login
def login():
    return 'Logi11111n'


if __name__ == '__main__':
    app.run()


from flask import request
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['GET', 'POST'])   # http://127.0.0.1:5000/upload
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('D:\pythonProject\q2xuexi' + secure_filename(f.filename))