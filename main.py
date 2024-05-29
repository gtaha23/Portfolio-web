# Import
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    email = db.Column(db.String(35), nullable=True)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Feedback {self.text}'

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python, 
                           button_discord=button_discord,
                           button_html=button_html,
                           button_db=button_db
                           )


if __name__ == "__main__":
    app.run(debug=True)
