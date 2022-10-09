from setuptools import setup,find_packages
from os import path

basedir = path.abspath(path.dirname(__file__))
with open(path.join(basedir, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='catwallpaper',
    version='0.9',
    url='https://github.com/CyberSecByte/catwallpaper',
    install_requires=["requests"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Topic :: System",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"
    ],
    author='CyberSecByte',
    author_email='cybersecbyte@gmail.com',
    description='Random cat wallpapers on every platform (windows, mac or even linux)',
    long_description_content_type='text/markdown',
    keywords=['cat', 'catwallpaper', 'wallpaper', 'meow', 'cats'],
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": ["catwallpaper = catwallpaper:main"]
    },
    
)
