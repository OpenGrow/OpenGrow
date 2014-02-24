# -*- coding: utf-8 -*-

from flask.ext.wtf import Form, TextField, BooleanField, PasswordField, SelectField, SubmitField
from flask.ext.wtf import Required, NumberRange, IPAddress


class LoginForm(Form):
    password = PasswordField('password', validators = [Required()])


class NewProjectForm(Form):
    name = TextField('name', validators=[Required("Enter a name")])
    description = TextField('name', validators=[Required("Short description")])
    submit = SubmitField("Create")

    def validate(self):
        validation = True
        #if not Form.validate(self):
        #    validation = False
        #    return validation

        if "<" in self.name.data or ">" in self.name.data:
            validation = False
            self.name.errors.append("Illegal chars in name")

        if "<" in self.description.data or ">" in self.description.data:
            validation = False
            self.description.errors.append("Illegal chars in description")
        print validation
        return validation