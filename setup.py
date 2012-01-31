from distutils.core import setup
from distutils.command.install import install
import os
		
setup(
    name = "denmark",
    version = "0.1",
    author = "Colin Marc",
    author_email = "colinmarc@gmail.com",
    description = ("a  utility to open markdown files in the browser"),
    scripts = ['denmark'],
    data_files = [
    	('share/applications', ['denmark.desktop'])
    ]
)
