from setuptools import setup
import sdist_upip

with open("README.MD", "r") as long_description_file_reader:
    long_description = long_description_file_reader.read()

setup(
    name='micropython-picoconnection',
    version="v0.0.0",
    description="Pi Pico AP and Wifi Connection helper",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MikeSchapp/PicoConnection',
    author='MikeSchapp',
    keywords='micropython, wifi',
    project_urls={
        'Source': 'https://github.com/MikeSchapp/PicoConnection',
    },
    license='BSD 2',
    packages=['picoconnection'],
    cmdclass={'sdist': sdist_upip.sdist}
)
