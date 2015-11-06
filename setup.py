import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()


PACKAGE = 'structural_types'
VERSION = '0.1.0'


def _get_requires(filepath):
    path = '{}/{}'.format(os.path.abspath(os.path.dirname(__file__)), filepath)
    with open(path) as reqs:
        return [req for req in reqs.read().split('\n') if req]

keywords = ['structural_types',
            'type system', 'type checking', 'subclass', 'classes']
description = ('Structural type checking for Python.')

setup(
    name='structural_types',
    version=VERSION,
    description=description,
    author='Chris Tabor',
    author_email='dxdstudio@gmail.com',
    maintainer='Chris Tabor',
    maintainer_email='dxdstudio@gmail.com',
    url='https://github.com/automotron/structural_types',
    keywords=keywords,
    license='GNU GENERAL PUBLIC LICENSE V3',
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=[
        'setuptools>=0.8',
    ],
    tests_require=[
        'nose',
    ],
    test_suite='tests',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
    ]
)
