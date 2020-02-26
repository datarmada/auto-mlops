import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="auto-mlops-datarmada",
    version="0.1.7",
    author="Datarmada",
    author_email="contact@datarmada.com",
    description="Deploy your ML model with 1 line of Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/borisghidaglia/auto-mlops",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "scikit-learn = ^0.22.1",
        "requests = ^2.23.0",
        "cloudpickle = ^1.3.0",
    ]
)
