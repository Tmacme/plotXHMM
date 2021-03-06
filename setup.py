from setuptools import setup

setup(

    name='plotXHMM',

    author='Michael Knudsen',
    author_email='micknudsen@gmail.com',

    packages=['plotxhmm'],

    scripts=['scripts/plotxhmm'],

    install_requires=['pandas', 'matplotlib'],

    test_suite='tests'

)
