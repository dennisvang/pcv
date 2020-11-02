# -*- coding: utf-8 -*-
import pathlib
from pcv import render

current_folder = pathlib.Path(__file__).parent.resolve()

with open(current_folder.joinpath('cv.html'), 'w') as output_file:
    output_file.write(render())
