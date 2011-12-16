from setuptools import setup
from setuptools import find_packages


setup(
    name='pyfeddic',
    version='0.1',
    description='Python Federal Reserve E-Payments Routing Directory Library',
    author='',
    author_email='',
    url='https://github.com/mjallday/pyfeddic',
    install_requires=[
        'mock==0.7.2',
        'mocker==1.1',
        'nose==1.1.2',
    ],
    setup_requires=[],
    packages=find_packages(),
    include_package_data=True,
    test_suite='nose.collector',
    zip_safe=True,
    entry_points={},
)
