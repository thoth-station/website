#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   thoth-dependency-monkey
#   Copyright(C) 2018 Christoph Görn
#
#   This program is free software: you can redistribute it and / or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Thoth: Dependency Monkey API"""

import os
import time
import logging

from flask import Flask
from flask import render_template


DEBUG = bool(os.getenv('DEBUG', False))

if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/graph')
def graphexp():
    return render_template('graphexp.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=DEBUG)
