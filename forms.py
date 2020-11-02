from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms.validators import DataRequired, EqualTo
from models import Myuser

class RegisterForm(FlaskForm):
    userid = StringField('userid', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('repassword')])
    repassword = PasswordField('repassword', validators=[DataRequired()])

class LoginForm(FlaskForm):

    class UserPassword(object):
        def __init__(self, message=None):
            self.message = message

        def __call__(self, form, field):
            userid = form['userid'].data
            password = field.data

            fcuser = Myuser.query.filter_by(userid=userid).first()
            if fcuser.password!=password:
                print('Wrong Password')
                #raise ValueError('Wrong Password')

    userid = StringField('userid', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), UserPassword()])