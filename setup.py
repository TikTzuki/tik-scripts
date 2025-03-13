from setuptools import setup, find_packages

NAME = "tik-scripts"
VERSION = "0.0.12"
REQUIRES = [
    "fastapi>=0.65.2"
    "loguru>=0.5.3"
    "orjson>=3.5.4"
]
LONG_DESCRIPTION = open("README.md", "r").read()

setup(
    name=NAME,
    version=VERSION,
    license="MIT",
    author="TikTuzki",
    author_email="tiktuzki@gmail.com",
    packages=find_packages(".", include=["src*"]),
    package_dir={"": "."},
    url="https://github.com/TikTzuki/tik-scripts",
    keywords=["Tik", "Script", "Utility"],
    install_requires=REQUIRES,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION
)
