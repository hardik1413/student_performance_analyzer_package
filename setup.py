"""
Package Setup and Distribution Metadata for Student Performance Analyzer
Allows local installation and distribution of the performance_analyzer package.
"""

from setuptools import setup, find_packages


setup(
    name="performance_analyzer",
    version="1.0.0",
    author="Educational Data Systems Team",
    author_email="devs@educationaldata.org",
    description=(
        "A modular Python package for score validation, "
        "grading rules, and class performance analytics."
    ),

    long_description=(
        "Educational Data Processing Package"
    ),
    long_description_content_type="text/markdown",

    packages=find_packages(),

    python_requires=">=3.8",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],

    install_requires=[],
)