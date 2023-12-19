from flask import Flask,render_template as rt,session, redirect, url_for, request
from api.GemPages import getPages
from api.getPageNumber import get_page_number
from api.GemProducts import process_page

app = Flask(__name__)

app.secret_key = 'BCQWR#$@@WE@12332423@121'
current_page = 1

#Routes Will be here
@app.route('/',methods = ["GET","POST"])
def landing():
    return rt('index.html')

@app.route('/categories', methods = ["POST"])
def result():
    query = request.form.get("searchquery")
    categorylist = getPages(query)
    return rt('category_page.html', searchquery = query, categories = categorylist)

@app.route('/Products', methods = ["POST"])
def showProducts():
    page_link = request.form.get("selected_product")
    url = "https://mkp.gem.gov.in" + page_link
    total_pages = get_page_number(url)
    
    if total_pages == None:
        return rt("failure.html")
    else :
        detail_list = process_page(page_link)
        return rt('products.html', productlist = detail_list, total_pages = total_pages, current_page=current_page, page_link=page_link)
 
if __name__ == '__main__':
    app.run(debug=True)