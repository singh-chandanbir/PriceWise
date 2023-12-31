import json
from flask import Flask,render_template as rt,session, redirect, url_for, request
from api.GemPages import getPages
from api.getPageNumber import get_page_number
from api.GemProducts import process_page
from api.flipkart import getFlipkartProducts
from api.exportersindia import get_exporters_products

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
    # query = query.replace(" ", "%20")
    categorylist = getPages(query)
    return rt('category_page.html', searchquery = query, categories = categorylist)

@app.route('/quickaccess', methods = ["POST"])
def quick_access():
    query = request.form.get("selected_button")
    # query = query.replace(" ", "%20")
    categorylist = getPages(query)
    return rt('category_page.html', searchquery = query, categories = categorylist)

@app.route('/Products', methods = ["POST"])
def showProducts():
    page_link = request.form.get("selected_product")
    url = "https://mkp.gem.gov.in" + page_link
    total_pages = get_page_number(url)
    query = request.form.get("query")
    page_title = request.form.get("page_title")
    print("0000000000000000", page_title, "00000000000000")
    if total_pages == None:
        return rt("failure.html")
    else :
        detail_list = process_page(page_link)
        with open("list.json", 'w') as file:
            json.dump(detail_list, file)
        return rt('products.html', productlist = detail_list, total_pages = total_pages, current_page=current_page, page_link=page_link, searchquery = query, page_title = page_title)
 
@app.route('/Products_page=', methods=['POST'])
def products_page():
    page_number = request.form.get("button_name")
    current_page = int(page_number)
    final_page = request.form.get("total pages")
    total_pages = int(final_page)
    page_link = request.form.get("page link")
    search_index = page_link.find('/search')
    query = request.form.get("query")
    if search_index != -1:
        result = page_link[:search_index + len('/search')]
    url = result + f"?don_load_facets=true&home=false&page={current_page}"
    detail_list = process_page(url)
    with open("list.json", 'w') as file:
        json.dump(detail_list, file)
    return rt('products.html', productlist = detail_list, total_pages = total_pages, current_page = current_page, page_link=page_link, searchquery = query)
 
@app.route("/comparison", methods = ["POST"])
def comparison():
    product_link = request.form.get("selected_button")
    page_title = request.form.get("page_title")
    search_index = page_title.find("(")
    if search_index != -1:
        page_title = page_title[:search_index]
    selected_product = ""
    query = request.form.get("query")
    with open("list.json", 'r') as f:
        new_list = json.load(f)
    for product in new_list:
        if product['product_link'] == product_link:
            selected_product = product
            break
    flipkartlist = getFlipkartProducts(page_title)
    exportslist = get_exporters_products(page_title)

    print("0000000000000000", page_title, "00000000000000")
    
    return rt("product_view.html", flipkartlist = flipkartlist , exportslist = exportslist ,product=selected_product, product_url = product_link)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)