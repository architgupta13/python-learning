#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Archit Gupta",
    author_email="gupta.archit13@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    description="Data Structures is a package that contains all the abstract data structures that can be manually written in Python",
    entry_points={
        "console_scripts": [
            "data_structures=data_structures.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="data_structures",
    name="data_structures",
    packages=find_packages(include=["data_structures", "data_structures.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/architgupta13/data_structures",
    version="0.1.0",
    zip_safe=False,
)
