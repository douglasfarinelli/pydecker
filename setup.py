import codecs
import os

from setuptools import find_packages, setup


name = 'decker'

description = (
    "Simple development tool that simplifies a pythonist's daily tasks."
)
version = '0.1.0'

release_status = 'Development Status :: 3 - Alpha'

dependencies = [
    'autoflake',
    'black',
    'click',
    'colorama',
    'docformatter',
    'ipython',
    'isort',
    'pdbpp',
    'ramos',
    'toml',
    'unify',
]

extras = {}

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

packages = [
    package
    for package in find_packages(
        where=os.path.join(here, 'src'), exclude=['tests', 'tests.*']
    )
]

setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Douglas Farinelli',
    license='MIT',
    url='https://github.com/douglasfarinelli/decker',
    classifiers=[
        release_status,
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={'console_scripts': ['decker=decker.__main__:main']},
    package_dir={'': 'src'},
    packages=packages,
    install_requires=dependencies,
    package_data={'': ['LICENSE']},
    python_requires='>=3.6',
    include_package_data=True,
    zip_safe=False,
)
