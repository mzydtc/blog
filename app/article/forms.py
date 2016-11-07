from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,PasswordField
from wtforms.validators import DataRequired,EqualTo


class CommentForm(FlaskForm):
    content = StringField('content', validators=[DataRequired()])
    article_id = StringField('article_id', validators=[DataRequired()])
    is_reply = StringField('is_reply', validators=[DataRequired()])
    reply_to = StringField('reply_to')