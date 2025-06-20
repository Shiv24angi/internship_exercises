# setup.py

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Lexicon Scanner for a Game',
    'author': 'Shivangi Sharma',
    'url': 'https://github.com/Shiv24angi/ex48',
    'download_url': 'https://github.com/Shiv24angi/ex48/archive/main.zip',
    'author_email': 'your.email@example.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'ex48'
}

setup(**config)
