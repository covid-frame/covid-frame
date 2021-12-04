import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="covidframe",
    version="0.0.1",
    author="Covid-frame",
    author_email="luighi.viton@pucp.edu.pe",
    description="Framework to process X-ray images and detect COVID-19",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/covid-frame/covid-frame",
    project_urls={
        "Bug Tracker": "https://github.com/covid-frame/covid-frame/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License ",
        "Operating System :: POSIX :: Linux ",
    ],
    packages=["covidframe"],
    python_requires=">=3.6",
    install_requires=[
        'colorlog',
        'python-dotenv',
        'numpy',
        'keras',
        'opencv_contrib_python',
        'pandas',
        'Wand'
    ],
    entry_points={
        'console_scripts': [
            'covidframe=covidframe.__main__',
        ],
    },
)
