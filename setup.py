import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='Discrept',
    version='1.2',
    scripts=['discrept.py'],
    author="Andrew Reed",
    author_email="AndrewReed2017@icloud.com",
    description="A Language that Generates PDF / Math coding language",
    long_description=long_description,
    url="https://github.com/areed2017/Discrept",
    packages=[
        'discrept_pac.parsetree',
        'discrept_pac.parsetree.cfg',
        'discrept_pac.parsetree.helpers',
        'discrept_pac.parsetree.list',
        'discrept_pac.parsetree.new',
        'discrept_pac.parsetree.proofs',
        'discrept_pac.parsetree.table',
        'discrept_pac.parsetree.title',
        'discrept_pac.printpdf',
        'discrept_pac.tokenizer',
    ],
    data_files=[('styles', ['styles/document.css', 'styles/lab report.css'])],

    install_requires=[
          'weasyprint',
          'subscrept',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )