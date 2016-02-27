from setuptools import find_packages, setup

setup(
    name='chutes-and-ladders',
    version='1.0.0',
    author='William Jackson',
    author_email='william@subtlecoolness.com',
    url='https://github.com/williamjacksn/chutes_and_ladders',
    description='Chutes and Ladders',
    license='MIT License',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'chutes_and_ladders = chutes_and_ladders.chutes_and_ladders:main'
        ]
    }
)
