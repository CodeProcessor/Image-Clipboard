#!/usr/bin/env python3
"""
@Filename:    setup.py
@Author:      dulanj
@Time:        2021-09-19 14.35
"""
import image_clipboard
from setuptools import setup, find_packages

setup(
    name='image_clipboard',
    version=image_clipboard.__version__,
    description='Image Clipboard Captre',
    url='https://about.dulanj.com/',
    author='CodeProcessor Incorporated',
    author_email='dulanjayasuriya@gmail.com',
    license='MIT',
    scripts=['bin/imclip'],
    packages=find_packages(),
    install_requires=[
        'pyscreenshot==3.0',
        'pytesseract==0.3.8',
        'pyperclip==1.8.2',
        'pynput==1.7.3'
    ],
    zip_safe=False
)
