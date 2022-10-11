import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "dependency_network_metamodel",
    version = "0.1.0",
    author = "Antonio Germán Márquez Trujillo",
    author_email = "amtrujillo@us.es",
    description = "This repo host the dependency network model concrete classes",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/GermanMT/dependency_network_metamodel",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=[
        'famapy>=1.0.0'
    ]
)