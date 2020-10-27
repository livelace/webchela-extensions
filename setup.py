from setuptools import find_packages, setup

setup(
    name="webchela-extensions",
    description="Various browser extensions for Webchela",
    version="1.0.0",
    url="https://github.com/livelace/webchela-extensions",
    author="Oleg Popov",
    author_email="o.popov@livelace.ru",
    license="BSD",
    packages=find_packages(),
    include_package_data=True
)
