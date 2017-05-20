try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Scrabble_Hacker',
    'author': 'Aaron Merten',
    'url': 'https://snowden24@bitbucket.org/snowden24/testing.git',
    'download_url': 'download location TBD.',
    'author_email': 'mertenar@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'Scrabble_Hacker'
}

setup(**config)
