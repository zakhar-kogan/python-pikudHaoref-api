from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="tzevaadom",
    packages=["tzevaadom"],
    version="1.0",
    license="MIT",
    description="A Python library for Pikud Haoref's unofficial rocket alert API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Itai Guli, Zakhar Kogan",
    author_email="app.redalert@gmail.com, zakhar@teleogenic.com",
    # url="https://github.com/itaiguli",
    # download_url="https://github.com/itaiguli/python-pikudHaoref-api/archive/1.0.tar.gz",
    url="https://github.com/zakhar-kogan/python-pikudHaoref-api",
    keywords=["tzevaadom", "pikud", "oref", "redalert", "rocket"],
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)
