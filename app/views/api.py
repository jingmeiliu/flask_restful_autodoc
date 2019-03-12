# 路由视图
import re
from flask_restful import Resource, Api
from flask import Blueprint, render_template, url_for


from .. import get_app

api = Blueprint('api', __name__)

rest_api = Api(api)

api_list = [
    ('hello', '欢迎', '/hello'),
]


def get_api_map():
    return api_list


@api.route('/', methods=['GET'])
def index():
    api_map = sorted(list(get_api_map()))
    index_url = url_for('main.index', _external=True)
    api_map = [(index_url + 'api' + x[2], x[1], x[0]) for x in api_map]
    return render_template('api_index.html', api_map=api_map)


class hello(Resource):
    """
    description===欢迎;
    method===GET,POST;
    parameter===
        data={
            name:fdsf
        }
    ;
    response===
         data=[
              {
               name:fsdg,
                ...
               ]
           },
           ...

       ]

    """

    def get(self):
        return {'hello world'}


rest_api.add_resource(hello, '/hello')
