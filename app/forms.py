from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, FloatField, IntegerField, RadioField
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
    submit = SubmitField("Submit")

class UpdateProductForm(FlaskForm):
    """ Update Product Form """
    old_name = StringField('Product Name', [
        DataRequired()])
    select = RadioField('Choose field to modify:', choices=[('prod_name','Change Product Name'),('prod_cat','Change product category'),('prod_price', 'Change Product Price'),('prod_stock','Change Amount of Product'),('prod_img','Change Image URL')])
    change_to = StringField('Change option to:', [
        DataRequired()])
    submit = SubmitField("Submit")

class RemoveProductForm(FlaskForm):
    """ Update Product Form """
    name_to_remove = StringField('Product Name', [
        DataRequired()])
    submit = SubmitField("Submit")