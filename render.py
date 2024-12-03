from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask App on Render!"

@app.route('/about')
def about():
    return "This is a basic Flask app deployed on Render."

if __name__ == '__main__':
    app.run(debug=True)
