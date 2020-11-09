# -*- coding: utf-8 -*-
import logging
import pathlib
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pcv.filters import (
    reformat, as_circles, sort_and_group, sort_and_join_labels,
    group_by_category)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

TEMPLATE_FOLDERS = ['templates']


def render(pages, data_files, source_path=None, styles=None):
    if source_path is None:
        source_path = pathlib.Path('')
    else:
        source_path = pathlib.Path(source_path)
    if styles is None:
        styles = ['style_pages.css', 'style_zero.css']
    # combine data from json files in a single dictionary
    data = dict()
    for filename in data_files:
        with source_path.joinpath(filename).open('r') as file_obj:
            data.update(json.load(file_obj))
    # configure template environment
    env = Environment(loader=FileSystemLoader(searchpath=TEMPLATE_FOLDERS),
                      autoescape=select_autoescape(['html', 'css']))
    # register template filters
    env.filters['reformat'] = reformat
    env.filters['as_circles'] = as_circles
    env.filters['sort_and_group'] = sort_and_group
    env.filters['sort_and_join_labels'] = sort_and_join_labels
    env.filters['group_by_category'] = group_by_category
    # render pages
    return env.get_template('pages.html').render(
        pages=pages, styles=styles, **data)
