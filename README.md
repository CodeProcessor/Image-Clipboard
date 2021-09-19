# Image-Clipboard

Image clipboard is a tool that you can easily copy the text from images. Select the area then past and use. It's that simple...

![Alt Text](https://github.com/CodeProcessor/Image-Clipboard/blob/master/assets/image-clipboard.gif)

## How to install

### Ubuntu system

Install tesseract-ocr
```bash
sudo apt-get update
sudo apt-get install libleptonica-dev 
sudo apt-get install tesseract-ocr tesseract-ocr-dev
sudo apt-get install libtesseract-dev
sudo apt-get install tesseract-ocr
```

Install the package
```bash
cd Image-Clipboard
pip install .
```

## How to run
Open terminal
```bash
imclip
```
Use mouse middle click and drag over the image to copy the content