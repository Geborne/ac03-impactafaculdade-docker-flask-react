from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db. Column(db.String(100), nullable=False)
    product_categoria = db.Column(db.String(100), nullable=False)
    product_preco = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return "<Product %r>" % self.product_name
