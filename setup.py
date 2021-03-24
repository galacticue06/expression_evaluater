from distutils.core import setup
from setuptools import find_packages
import os


current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
    name="expression_evaluater",
    packages=find_packages('.'),
    version='1.0.0',
    license='MIT',
    description='A basic math evaluater and expression parser',
    long_description = long_description,
    long_description_context_type = 'text/markdown',

    author='Gandalf Sax Guy(AKA Kerbal Galactic)', 
    author_email='kerbalgalactic@gmail.com',
    url='',
    download_url='',
    keywords=['parser','math'],
    install_requires=[],
    classifiers=[]  
)
