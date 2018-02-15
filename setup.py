import setuptools


setuptools.setup(
    name="mdc",
    version="0.1.0",
    description="",
    url="https://git.vpgrp.io/noc/python-mdc",
    author="Damien PLENARD",
    author_email="dplenard@vente-privee.com",
    license="Apache License 2.0",
    long_description=open("README.md").read(),
    entry_points={
        "console_scripts": ["mdc=mdc.__main__:main"]
    },
    packages=["mdc"],
    install_requires=[],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Home Automation",
        "Topic :: Multimedia :: Video :: Display"
    ],
)