from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from settings import REGEX_PATTERN, USER_LENGHT


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    URL(message='Введите ссылку целиком')]
    )
    custom_id =  StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(max=USER_LENGHT,
                           message=f'Длина ссылки должна быть до {USER_LENGHT} символов'),
                    Regexp(REGEX_PATTERN,
                           message='Можно использовать только латинские буквы и арабские цифры'),
                    Optional()]
    )
    submit = SubmitField('Создать')
