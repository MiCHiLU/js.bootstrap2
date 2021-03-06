from setuptools import setup, find_packages
import os

version = '2.0.1'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'bootstrap2', 'test_bootstrap.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.bootstrap2',
    version=version,
    description="fanstatic twitter bootstrap.",
    long_description=long_description,
    classifiers=[],
    keywords='fanstatic twitter bootstrap redturtle',
    author='RedTurtle Developers',
    url = 'https://github.com/MiCHiLU/js.bootstrap2',
    author_email='svilplone@redturtle.it',
    license='GPL',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'js.jquery',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'bootstrap = js.bootstrap2:library',
            ],
        },
    )
