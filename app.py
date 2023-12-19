from flask import Flask,render_template as rt,session, redirect, url_for, request
from api.GemPages import getPages


app = Flask(__name__)
current_page = 1

app.secret_key = 'BCQWR#$@@WE@12332423@121'

@app.route("/")
def landing():
    return rt("index.html")

@app.route("/categories", methods=["POST"])
def category():
    query = request.form.get("searchquery")
    categorylist = getPages(query)
    return rt('category_page.html', searchquery = query, categories = categorylist)

if __name__ == '__main__':
    app.run(debug=True)