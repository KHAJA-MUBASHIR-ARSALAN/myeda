from setuptools import setup, find_packages

setup(
    name="myeda",
    version="0.1.0",
    description="Lightweight Exploratory Data Analysis library",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
    ],
    python_requires=">=3.9",
)
