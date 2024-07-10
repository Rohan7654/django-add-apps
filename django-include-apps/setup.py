# setup.py

from setuptools import setup, find_packages

setup(
    name='django-add-apps-cli',       # Package name
    version='0.1.0',         # Package version
    packages=find_packages(),
    install_requires=[
        'typer',             # Dependencies
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'django-include-apps = django-include-apps.main:app',   # CLI entry point
        ],
    },
    author='Rohan',
    author_email='rohanroni2019@gamil.com',
    description='CLI tool to install and add Django apps in INSTALLED_APPS',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
    ],
)
