from setuptools import setup, find_packages
from openai_api_utils import __version__

setup(
    name='openai-api-utils',
    version=__version__,
    packages=find_packages(),
    description='Utilities for OpenAI API Calls',
    author='Dexter Jung',
    author_email='dropyourcoffee@gmail.com',
    install_requires=[
        # List of dependencies
        'requests',
        'openai',
        'colorama',
        'wheel',
    ],
)

"""
 Upload Steps
 
  1. Check __version__
  
  2. Build whl
      python setup.py bdist_wheel
      
  3. Upload on Pypi
      twine upload dist/openai_api_utils-{version}-py3-none-any.whl
      
"""
