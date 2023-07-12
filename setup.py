from setuptools import setup, find_packages

VERSION = '0.0.0'

install_requires=[
        'plotly',
    ],

extras_require = {
    'dev': [
        'pandas',
        'numpy',
        'scikit-learn',
        'matplotlib',
    ],
    'test': [
            'pytest',
        ],
}
extras_require['dev'] += extras_require['test']

setup(
    name='vistree',
    version=VERSION,
    packages=find_packages(),
    install_requires=install_requires,
    extras_require=extras_require
)
