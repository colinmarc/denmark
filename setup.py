from distutils.core import setup
from distutils.command.install import install
import os

class install_mimetype(install):
	def run(self):
		install.run(self)
		os.system('update-mime-database /usr/share/mime')
		os.system('cat markdown.xml > /usr/share/mime/packages/Overrides.xml')
		os.system('echo "text/x-web-markdown=denmark.desktop" >> /etc/gnome/defaults.list')

setup(
    name = "denmark",
    version = "0.1",
    author = "Colin Marc",
    author_email = "colinmarc@gmail.com",
    description = ("a quick utility to open markdown files in the browser"),
    scripts = ['denmark'],
    data_files = [
    	('share/applications', ['denmark.desktop'])
    ],
    cmdclass={'install': install_mimetype}
)
