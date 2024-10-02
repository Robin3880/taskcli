from setuptools import setup

setup(
    name='taskcli',
    version='1.0',
    py_modules=['taskcli'],  # This should match the name of your module (taskcli.py)
    entry_points={
        'console_scripts': [
            'taskcli=taskcli:main',  # Maps the command taskcli to the main() function in taskcli.py
        ],
    },
)
