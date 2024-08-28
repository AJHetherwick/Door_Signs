from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Automatic door sign printing script'
LONG_DESCRIPTION = 'A package that allows user to automatically create lab door signs for their division (MSD, ALS, CSD)' \
                   'after they have mounted their Google Drive.'

# Setting up
setup(
    name="door_signs_script",
    version=VERSION,
    author="Adam Hetherwick",
    author_email="<adamhetherwick@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['datetime==5.5', 'pandas==2.0.3', 'pdfrw==0.4', 'PyPDF2==3.0.1', 'reportlab==4.2.2'],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)