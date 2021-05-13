"""Build and install the Final Solution."""
from setuptools import setup, find_packages

LONG_DESCRIPTION = "Final solution for all of our stock needs."

with open("version", "r") as fd:
    version = fd.read()

with open("requirements.txt", "r") as req:
    requirements = req.read().splitlines()

setup(
    name='stock-grapher',
    install_requires=requirements,
    version=version,
    description="Final Solution",
    long_description=LONG_DESCRIPTION,
    url='https://github.com/Michawl1/StockGrapher.git',
    download_url='https://github.com/Michawl1/StockGrapher',
    author='One Retard With a Keyboard',
    author_email='lol',
    maintainer='Maybe',
    maintainer_email="Don't ask",
    classifiers=[
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: STONK",
    ],
    package_dir={"": "src"},
    packages=find_packages('src'),
)
