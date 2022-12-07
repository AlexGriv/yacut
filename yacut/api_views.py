import re
from http import HTTPStatus
from urllib.parse import urljoin

from flask import jsonify, request

from settings import REGEX_PATTERN, USER_LENGHT

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utilities import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def create_id():
    data = request.get_json()
    request_URL = request.url_root
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    condition = ('custom_id' in data and
                 data['custom_id'] is not None and
                 len(data['custom_id']) > 0)
    if condition:
        custom_id = data['custom_id']

        condition_first = (len(custom_id) > USER_LENGHT or not
                           re.match(REGEX_PATTERN, custom_id))
        condition_second = URLMap.query.filter_by(
            short=custom_id
        ).first() is not None
        if condition_first:
            raise InvalidAPIUsage('Указано недопустимое '
                                  'имя для короткой ссылки')
        elif condition_second:
            raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.')
    else:
        custom_id = get_unique_short_id()
    original = data['url']
    url = URLMap(
        original=original,
        short=custom_id
    )
    db.session.add(url)
    db.session.commit()
    return jsonify(
        {'url': original, 'short_link': urljoin(request_URL, custom_id)}
    ), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url.original}), HTTPStatus.OK