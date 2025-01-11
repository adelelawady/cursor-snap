from setuptools import setup, find_packages

setup(
    name="cursor-snap",
    version="2.0.0",
    description="A utility tool to manage and reset Cursor Editor app IDs",
    author="Adel Elawady",
    author_email="adel50ali50@gmail.com",
    packages=find_packages(),
    install_requires=[
        "rich>=10.0.0",
        "pathlib>=1.0.1",
    ],
    entry_points={
        'console_scripts': [
            'cursor-snap=cursor_snap.cursor_snap:main',
        ],
    },
    python_requires=">=3.6",
) 