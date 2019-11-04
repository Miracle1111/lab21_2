from flask_wtf import Form
from wtforms import StringField, SubmitField, DateField, HiddenField, IntegerField, BooleanField
from datetime import date
from wtforms import validators


class UniverForm(Form):

    name = StringField("name: ", [
        validators.DataRequired("Please enter univer`s name."),
        validators.Length(3, 255, "Text should be from 3 to 255 symbols")
    ])

    addr = StringField("addr : ", [
        validators.DataRequired("Please enter address."),
        validators.Length(2, 255, "Text should be from 2 to 255 symbols")
    ])

    counter = IntegerField("Number_of_groups: ")

    balance = IntegerField("Balance: ")

    submit = SubmitField("Save")