from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup, find_packages

with open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='JTX2Tools',
    url='',
    author='Thys Meintjes',
    author_email='matthys.meintjes@bhp.com',
    description='JTX2 Tools',
    long_description=readme,
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'txt2-show-gpu=jtx2tools.cli:cli',
        ],
    },
    install_requires=[
        'click',
        'knobs',
    ],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
)
