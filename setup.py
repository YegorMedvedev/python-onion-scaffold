from setuptools import setup
from src.version import __version__

setup(
    name='python-onion-scaffold',
    version=__version__,
    packages=['src', 'src.api', 'src.core', 'src.services',
              'src.infrastructure'],
    url='https://github.com/YegorMedvedev/python-onion-scaffold',
    license='',
    author='YegorMedvedev',
    author_email='social.neet@gmail.com',
    description='',
    install_requires=['pipenv']
)
