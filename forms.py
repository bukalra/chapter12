from flask_wtf import FlaskForm
from wtforms import (
StringField, 
PasswordField, 
TextAreaField, 
BooleanField, 
DateField, 
TimeField, 
SelectField, 
IntegerField
)
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    name = StringField('Product name', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    unit = StringField('Unit', validators=[DataRequired()])
    unit_price = IntegerField('Unit price', validators=[DataRequired()])


class ProductSaleForm(FlaskForm):
    quantity = IntegerField('Quantity to sell', validators=[DataRequired()])

