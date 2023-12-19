from flask import Flask,render_template as rt,session, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def landing():
    return rt("index.html")

if __name__ == '__main__':
    app.run(debug=True)