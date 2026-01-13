from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name="myeda",
    version="0.1.1",
    description="Lightweight Exploratory Data Analysis library",
    author="Khaja Mubashir Arsalan",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
    ],
    python_requires=">=3.9",

    long_description = description,
    long_description_content_type="text/markdown",
)




