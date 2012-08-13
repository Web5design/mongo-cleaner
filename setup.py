import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='mongo-cleaner',
    version='0.1',
    author = "Cenk Alti",
    author_email = "cenkalti@gmail.com",
    description = "Stale data cleaner for MongoDB.",
    keywords = "mongodb",
    url = "https://github.com/cenkalti/mongo-cleaner",
    packages=['mongo_cleaner'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Database",
        "Topic :: Utilities",
    ],
    install_requires=['pymongo'],
)
