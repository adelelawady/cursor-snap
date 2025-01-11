from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cursor-snap",
    version="2.0.0",
    author="Adel Elawady",
    author_email="adel50ali50@gmail.com",
    description="A utility tool to manage and reset Cursor Editor app IDs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adelelawady/cursor-snap",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "rich>=10.0.0",
        "pathlib>=1.0.1",
    ],
    entry_points={
        "console_scripts": [
            "cursor-snap=cursor_snap:main",
        ],
    },
) 