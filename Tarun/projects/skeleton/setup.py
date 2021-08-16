try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Tarun',
    'url': 'URL TO MY WEBSITE',
    'download_url': 'Where to download it',
    'author_email': 'My Email',
    'version': '0.1',
    'install_requires': 'nose',
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
