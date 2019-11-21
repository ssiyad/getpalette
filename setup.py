from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="getpalette",
    version="1.0.7",
    description="Get color palette from images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ssiyad/getpalette",
    author="Sabu Siyad",
    author_email="sabu.siyad.p@gmail.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Pillow==6.2.1',
        'matplotlib==3.0.3',
        'scipy==1.3.1',
        'pandas==0.24.2'
    ],
    entry_points={
        "console_scripts": [
            "getpalette = getpalette.__main__:main",
        ]
    }
)
