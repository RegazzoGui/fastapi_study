import io
import os
from setuptools import find_packages, setup


def read(*path, **kwargs):
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *path),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requeriments(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]

setup(
    name="pamps",
    version="0.1.0",
    description="Pamps is a social posting app",
    url="pamps.io",
    python_requeres=">=3.8",
    long_description="Pamps is a social posting app",
    long_descritption_content_type="text/markdown",
    author="ZzoG",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=read_requeriments("requeriments.txt"),
    entry_points={
        "console_scripts": ["pamps = pamps.cli:main"]
    }
)