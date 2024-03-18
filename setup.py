from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.MD").read_text()
setup(
    name='gqldataclass',
    version='1.0.1',
    url='https://github.com/nikikuzi/graphql-dataclass/tree/1.0.0',
    author='Mikita Kuzniatsou, Alex Dap',
    author_email='nikikuzi@gmail.com, shlisi2017@gmail.com',
    description='A python library to generate dataclasses for GraphQL types',
    long_description=long_description,
    include_package_data=True,
    packages=['pygqlmap', 'pygqlmap.src', 'codegen', 'codegen.src', 'codegen.src.templates'],
    data_files=[('', ['pygqlmap/config.ini'])],
    python_requires='>=3.10',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)