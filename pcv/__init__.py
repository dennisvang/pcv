# -*- coding: utf-8 -*-
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATE_FOLDERS = ['templates']


def as_circles(value, max_value=5):
    return '●' * value + '○' * (max_value - value)


def render(data_file=None, template_name='onepage.html'):
    data = None
    if data_file:
        with open(data_file, 'r') as file_obj:
            data = json.load(file_obj)
    env = Environment(loader=FileSystemLoader(searchpath=TEMPLATE_FOLDERS),
                      autoescape=select_autoescape(['html', 'css']))
    env.filters['as_circles'] = as_circles
    return env.get_template(template_name).render(**data)
