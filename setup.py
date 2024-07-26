# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyhere",
    version="1.0.3",
    author="Josh P. Sawyer",
    author_email="josh@joshpsawyer.com",
    license="MIT",
    description="Load files easily using relative path names and simple heuristics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wildland-creative/pyhere",
    packages=setuptools.find_packages(),
    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=2.7',
)