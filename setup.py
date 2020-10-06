import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

requirements = ['requests<=2.24.0']

setuptools.setup(
    name='hello_world_crock-dev',
    version='0.0.1',
    author='Crock-dev',
    author_email='leiko.dima2013@yandex.by',
    description='A Hello World package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ericjaychi/sample-pypi-package',
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)