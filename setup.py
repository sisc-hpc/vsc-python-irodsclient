#!/usr/bin/env python3
#
# Copyright 2020-2020 Vrije Universiteit Brussel
#
# This file is part of vsc-python-irodsclient,
# originally created by the HPC team of Vrij Universiteit Brussel (http://hpc.vub.be),
# with support of Vrije Universiteit Brussel (http://www.vub.be),
# the Flemish Supercomputer Centre (VSC) (https://www.vscentrum.be),
# the Flemish Research Foundation (FWO) (http://www.fwo.be/en)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# https://github.com/hpcleuven/vsc-python-irodsclient
#
# vsc-python-irodsclient is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation v3.
#
# vsc-python-irodsclient is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with vsc-manage.  If not, see <http://www.gnu.org/licenses/>.
#
##
"""
vsc-python-irodsclient base distribution setup.py

@author: Alex Domingo (Vrije Universiteit Brussel)
"""

import vsc.install.shared_setup as shared_setup
from vsc.install.shared_setup import ad

PACKAGE = {
    'version': '0.1',
    'author': ['Vlaams Supercomputer Centrum'],
    'maintainer': ['Vlaams Supercomputer Centrum'],
    'python_requires': '~=3.6',
    'setup_requires': [
        'vsc-install >= 0.15.15',
    ],
    'install_requires': [
        'python-irodsclient',
    ],
    'extras_requires': [
        'sphinx-rtd-theme',
    ],
    'excluded_pkgs_rpm': ['vsc'],  # vsc is default
}

if __name__ == '__main__':
    shared_setup.action_target(PACKAGE)
