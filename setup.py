import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='Discrept',
    version='1.0',
    scripts=['discrept, subscrept'],
    author="Andrew Reed",
    author_email="AndrewReed2017@icloud.com",
    description="A Language that Generates PDF / Math coding language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/areed2017/Discrept",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )