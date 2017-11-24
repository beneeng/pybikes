# -*- coding: utf-8 -*-
# Copyright (C) 2010-2012, eskerda <eskerda@gmail.com>
# Distributed under the AGPL license, see LICENSE.txt

from setuptools import setup
import glob
additional_files = []
additional_files_data =  glob.glob('pybikes/data/*.json')
additional_files_kml = [*glob.glob('pybikes/kml/*.kml'), *glob.glob('pybikes/kml/*.kml.gz')]

setup(
    name="pybikes",
    version="1.0",
    author="Lluis Esquerda",
    author_email="eskerda@gmail.com",
    packages=["pybikes"],
    package_data={
        'pybikes': additional_files,
        'pybikes/data': additional_files_data,
        'pybikes/kml': additional_files_kml
    },
    data_files=[('pybikes', additional_files), ('pybikes/data', additional_files_data), ('pybikes/kml', additional_files_kml)],
    license="LICENSE.txt",
    description="A python library for scrapping bike sharing data",
    long_description=open('README.md').read(),
    install_requires=[
        'requests>=2.6.0',
        'lxml',
        'cssselect>=0.9',
        'shapely>=1.5.13',
        'demjson',
    ],
)
