# -*- coding: utf-8 -*-
import pathlib
import shutil
from pcv import render

base_path = pathlib.Path(__file__).parent.resolve()
source_path = base_path.joinpath('src')
dist_path = base_path.joinpath('dist')
dist_path.mkdir(exist_ok=True)
if source_path.joinpath('static').exists():
    # copy static content to distribution folder
    shutil.copytree(
        source_path.joinpath('static'), dist_path.joinpath('static'),
        dirs_exist_ok=True)


# render to file
with dist_path.joinpath('cv.html').open('w', encoding='utf-8') as o:
    o.write(render(pages=['onepage.html', 'technologies.html'],
                   data_files=['cv.json', 'technologies.json'],
                   source_path=source_path))
