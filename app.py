import os
from flask import Flask,render_template,request,redirect,flash,url_for
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '/users/saral/desktop'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.config['DEBUG'] = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

def allowed_file(filename):
# Check if there is an extension in the file. Split the extension and check if it is present in allowed extenstions
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
        return render_template("index.html")

@app.route("/data")
def data():
    return render_template("data.html")

@app.route('/upload', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      file = request.files['file']
      if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('upload.html',filename=filename)