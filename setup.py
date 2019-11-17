from setuptools import setup

setup(
    name='getpalette',
    version='1.0.0',
    packages=['getpalette'],
    include_package_data=True,
    install_requires=[
        'Pillow==6.2.1',
        'matplotlib==3.0.3',
        'scipy==1.3.1',
        'pandas==0.24.2',
        'click==6.7'
    ],
    entry_points={
        'console_scripts': [
            'getpalette = getpalette.__main__:main',
        ]
    },
)

