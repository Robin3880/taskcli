from setuptools import setup
#makes taskcli a executable command
setup(
    name='taskcli',
    version='1.0',
    py_modules=['taskcli'],  
    entry_points={
        'console_scripts': [
            'taskcli=taskcli:main', 
        ],
    },
)
