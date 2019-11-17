# GetPalette
Find the dominant colors in any image

## Setup
```
git clone https://github.com/ssiyad/getpalette
cd getpalette
python3 -m venv env
source venv/bin/activate
pip install -e .
```
or
```
pip install getpalette
```

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

## Examples:
### Output Palette
![alt text](https://github.com/ssiyad/getpalette/blob/master/Example/example_palette.jpg)

### Image with Palette
![alt text](https://github.com/ssiyad/getpalette/blob/master/Example/example_with_palette.jpg)

## Contribution
- Report issues
- Open pull request with improvements
- Spread the word
---