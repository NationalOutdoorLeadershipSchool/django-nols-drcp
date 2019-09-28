#!/usr/bin/env python
from setuptools import find_packages, setup


setup(
    name="django-nols-drcp",
    packages=find_packages(),
    url="https://github.com/JohnPapps/django-oracle-drcp",
    version="1.0.4",
    description="A Django database backend for Oracle with DRCP",
    author="John Papanastasiou",
    author_email="s@johnpapps.com",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Topic :: Database",
    ],
)
