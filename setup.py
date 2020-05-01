from setuptools import setup, find_packages
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
    install_requires=['pipenv'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.8.*'
)
