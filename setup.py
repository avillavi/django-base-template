#!/usr/bin/env python
import os
from setuptools import setup, find_packages

project_name = "{{ project_name }}"
setup(
    name='{{ project_name }}',
    version='1.0',
    description="",
    author="Unholster S.A",
    author_email='info@unholster.com',
    url='',
    packages=find_packages(),
    package_data={project_name: ['bin/*.*', 'static/*.*', 'templates/*.*']},
    exclude_package_data={project_name: ['bin/*.pyc']},
    scripts=[ os.path.join(project_name, "bin", "manage.py")]
)