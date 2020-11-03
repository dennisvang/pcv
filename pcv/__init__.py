# -*- coding: utf-8 -*-
import logging
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pcv.filters import reformat, as_circles, sort_and_group

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

TEMPLATE_FOLDERS = ['templates']


def render(data_file=None, template_name='onepage.html'):
    data = None
    if data_file:
        with open(data_file, 'r') as file_obj:
            data = json.load(file_obj)
    env = Environment(loader=FileSystemLoader(searchpath=TEMPLATE_FOLDERS),
                      autoescape=select_autoescape(['html', 'css']))
    env.filters['reformat'] = reformat
    env.filters['as_circles'] = as_circles
    env.filters['sort_and_group'] = sort_and_group
    return env.get_template(template_name).render(**data)
