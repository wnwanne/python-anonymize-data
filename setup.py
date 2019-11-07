from setuptools import setup, find_packages
from anonymize_data import __version__

long_description = ''
with open('./README.md') as f:
    long_description = f.read()

setup(name='anonymize_data',
    version=__version__,
    description='A python package for anonymizing datasets.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/wnwanne/python-anonymize-data',
    author='Chris Pryer',
    author_email='christophpryer@gmail.com',
    license='PUBLIC',
    packages=find_packages(),
    zip_safe=False)
