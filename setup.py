# setup.py

from setuptools import setup, find_packages

setup(
    name="DIYables_LCD_I2C",
    version="0.1.1",
    description="Library for controlling I2C LCD displays with Raspberry Pi Pico, created by DIYables",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="DIYables",
    author_email="DIYables.io@gmail.com",
    url="https://diyables.io",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: Implementation :: MicroPython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
