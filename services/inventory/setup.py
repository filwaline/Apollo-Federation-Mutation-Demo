from setuptools import find_namespace_packages, setup

setup(
    name="inventory",
    version="0.0.1",
    author="filwaline",
    author_email="skywalker950925@gmail.com",
    packages=find_namespace_packages("."),
    package_dir={
        "": "./",
    },
    install_requires=[
        "fastapi==0.88.0",
        "strawberry-graphql[debug-server]",
        "dataclass-mapper",
    ],
)
