from flask import Flask,render_template as rt,session, redirect, url_for, request

app = Flask(__name__)

app.secret_key = 'BCQWR#$@@WE@12332423@121'

@app.route("/")
def landing():
    return rt("index.html")

@app.route("/categories", methods=["POST"])
def category():
    query = request.form.get("searchquery")
    print(query)
    return rt("index.html")

if __name__ == '__main__':
    app.run(debug=True)