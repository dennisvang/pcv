# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATE_FOLDERS = ['templates']


def render(template_name='onepage.html'):
    env = Environment(loader=FileSystemLoader(searchpath=TEMPLATE_FOLDERS),
                      autoescape=select_autoescape(['html', 'css']))
    return env.get_template(template_name).render()
