# 自动生成文档路由
from flask import Blueprint, redirect, url_for, render_template

from .. import get_app

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    """Redirect home page to docs page."""
    return redirect(url_for('api.index'))

@main.route('/docs/<endpoint>', methods=['GET'])
def docs(endpoint):
    """Document page for an endpoint."""
    api = {
        'endpoint': endpoint,
        'methods': '',
        'doc': '',
        'url': '',
        'name': ''
    }
    try:
        func = get_app().view_functions[endpoint]
        api=_get_api_doc_split(func)
        api['name'] = _get_api_name(func)
        for rule in get_app().url_map.iter_rules():
            if rule.endpoint == endpoint:
                api['url'] = str(rule)

    except:
        api['doc'] = 'Invalid api endpoint: "{}"!'.format(endpoint)
    return render_template('api_docs.html', api=api)


def _get_api_name(func):
    """e.g. Convert 'do_work' to 'Do Work'"""
    words = func.__name__.split('_')
    words = [w.capitalize() for w in words]
    return ' '.join(words)


def _get_api_doc(func):
    if func.__doc__:
        return func.__doc__
    else:
        return 'No doc found for this API!'


def _get_api_doc_split(func):
    api_docs = {'description': '', 'methods':'','parameter': '', 'response': ''}
    description,methods, parameter, response = _get_api_doc(func).split(';')
    api_docs['description'] = description.split('===')[1]
    api_docs['methods'] = methods.split('===')[1]
    api_docs['parameter'] = parameter.split('===')[1]
    api_docs['response'] = response.split('===')[1]
    return api_docs
