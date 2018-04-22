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
import daiquiri

from github import Github
from github import UnknownObjectException

from flask import Flask
from flask import render_template


DEBUG = bool(os.getenv('DEBUG', False))
SESHETA_GITHUB_ACCESS_TOKEN = os.getenv('SESHETA_GITHUB_ACCESS_TOKEN', None)


daiquiri.setup(level=logging.INFO)
logger = daiquiri.getLogger(__name__)

if DEBUG:
    logger.setLevel(level=logging.DEBUG)
else:
    logger.setLevel(level=logging.INFO)

app = Flask(__name__)


def _get_open_pullrequests():
    github = Github(SESHETA_GITHUB_ACCESS_TOKEN)
    org = github.get_organization('thoth-station')
    open_prs = []

    for repo in org.get_repos():
        for pr in repo.get_pulls(state='open'):
            _pr = {}
            _pr['repo'] = repo.name
            _pr['title'] = pr.title
            _pr['labels'] = pr.as_issue().labels
            _pr['html_url'] = pr.html_url
            _pr['user'] = pr.user.login

            open_prs.append(_pr)

    return open_prs


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/graph')
def graphexp():
    return render_template('graphexp.html')


@app.route('/open-prs')
def open_prs():
    return render_template('open-prs.html', open_prs=_get_open_pullrequests())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=DEBUG)
