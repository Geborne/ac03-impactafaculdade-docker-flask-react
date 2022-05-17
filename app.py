from flask import Flask, jsonify, request, render_template, make_response
from model.Product import db
from flask_cors import CORS

from model.product import Product

app = Flask(__name__, static_url_path='',
            static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app, resources={r"*": {"origins": "*"}})

db.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/list')
def productlist():
    return render_template('list.html')


@app.route('/newproduct', methods=['POST'])
def newproduct():
    try:
        db.create_all()
        db.session.commit()

        product_data = request.json

        product_name = product_data['Nome']
        product_categoria = product_data['Categoria']
        product_preco = product_data['Preço']

        product = Product(product_name=product_name, product_categoria=product_categoria,
                    product_preco=product_preco)

        db.session.add(product)
        db.session.commit()

        yes = make_response(jsonify({"YES!": "Um produto foi adicionado!"}), 201)
        return yes
    except Exception as e:
        print(e)
        fuck = make_response(jsonify({"Fuck: ": "Algo de errado não esta certo"}), 500)
        return fuck


@app.route('/allproducts', methods=['GET'])
def get_products():
    try:
        all_products = []
        products = Product.query.all()
        for product in products:
            resultado = {
                "id": product.id,
                "Nome": product.product_name,
                "Categoria": product.product_categoria,
                "Preço": product.product_preco
            }
            all_products.append(resultado)

        res = make_response(jsonify(all_products), 200)
        return res
    except Exception as e:
        print(e)
        fuck = make_response(jsonify({"Fuck: ": "Algo de errado não esta certo"}), 500)
        return fuck


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)