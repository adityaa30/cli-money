import setuptools

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='Money',
    version='1.0.0',
    author='Aditya Kumar',
    author_email='k.aditya00@gmail.com',
    description='Simple CLI to quickly get the latest currency rates',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/adityaa30/cli-money',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
)