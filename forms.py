from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, Length

class NewProductForm(FlaskForm):
    """ New Product Form """
    name = StringField('Product Name', [
        DataRequired()])
    category = StringField('Category', [
        DataRequired()])
    price = FloatField('Price per unit', [
        DataRequired()])
    stock = IntegerField('Amount in stock', [
        DataRequired()])
    img = StringField('Image URL', [
        DataRequired()])
