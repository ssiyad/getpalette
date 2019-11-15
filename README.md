# ColorPalette
Find the dominant colors in any image

## Setup
```
python3 -m venv env
source env/bin/activate
pip install -e .
```

## Usage
```
./bin/run EXAMPLE_IMAGE.jpg NUM_COLORS
```
In the above, NUM_COLORS refers to the number of colors you want displayed. Additionally, you may follow NUM_COLORS with either a 0 or a 1 to specify whether you would like the hexadecimal color codes of each number to be displayed in the final picture.

## Output
The tool will output two files into the main folder your image was initially in. The first file will be named YOUR_FILE_palette and will contain just the color palette. The second file will be called YOUR_FILE_with_palette and this will contain the original image with the palette below it.

## Examples:
### Image without color names
![alt text](https://github.com/ssiyad/ColorPalette/blob/master/Example/fox_with_palette.jpg)

### Image with color names
![alt text](https://github.com/ssiyad/ColorPalette/blob/master/Example/fox_with_pallete_text.jpg)

## Contribution
- Report issues
- Open pull request with improvements
- Spread the word
---