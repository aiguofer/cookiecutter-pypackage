#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
from os import path
from codecs import open
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

exec(open("{{ cookiecutter.package_name }}/_version.py").read())

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

# get the dependencies and installs
with open(path.join(here, "requirements.txt"), encoding="utf-8") as f:
    all_reqs = f.read().split("\n")

install_requires = [x.strip() for x in all_reqs if "git+" not in x]
dependency_links = [
    x.strip().replace("git+", "") for x in all_reqs if x.startswith("git+")
]

# get the dependencies and installs
with open(path.join(here, "requirements_dev.txt"), encoding="utf-8") as f:
    dev_requires = f.read().split("\n")

{%- if cookiecutter.command_line_interface|lower == 'click' %}
install_requires += ["Click>=6.0"]
{%- endif %}

setup_requirements = [
    {%- if cookiecutter.use_pytest == 'y' %}
    "pytest-runner",
    {%- endif %}
]

test_requirements = [
    {%- if cookiecutter.use_pytest == 'y' %}
    "pytest",
    {%- endif %}
]

# {%- set license_classifiers = {
#     "MIT license": "License :: OSI Approved :: MIT License",
#     "BSD license": "License :: OSI Approved :: BSD License",
#     "ISC license": "License :: OSI Approved :: ISC License (ISCL)",
#     "Apache Software License 2.0": "License :: OSI Approved :: Apache Software License",
#     "GNU General Public License v3": "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
# } %}

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email="{{ cookiecutter.email }}",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        {%- if cookiecutter.open_source_license in license_classifiers %}
        "{{ license_classifiers[cookiecutter.open_source_license] }}",
        {%- endif %}
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    description="{{ cookiecutter.project_short_description }}",
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.package_name }}={{ cookiecutter.package_name }}.cli:main"
        ]
    },
    {%- endif %}
    install_requires=install_requires,
    dependency_links=dependency_links,
    {%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
    {%- endif %}
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="{{ cookiecutter.package_name }}",
    name="{{ cookiecutter.package_name }}",
    packages=find_packages(include=["{{ cookiecutter.package_name }}"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    extras_require={"dev": dev_requires},
    url="{{ cookiecutter.git_host }}/{{ cookiecutter.git_host_username }}/{{ cookiecutter.project_slug }}",
    version=__version__,
    zip_safe=False,
)
