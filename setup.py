from setuptools import setup, find_packages

LONG_DESC = """
## Usage
```
getpalette [-h] [-c COUNT] [-s] image

positional arguments:
  image

optional arguments:
  -c COUNT, --count COUNT
                        Number of colors to find
  -s, --show            Show/Hide hexadecimal color values
  -h, --help            show this help message and exit
```

## Output
The tool will output two files into the main folder your image was initially in. The first file will be named IMAGE_palette and will contain just the color palette. The second file will be called IMAGE_with_palette and this will contain the original image with the palette below it.
"""

setup(
    name="getpalette",
    version="1.0.2",
    description="Get color palette from images",
    long_description = LONG_DESC,
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
    },
)