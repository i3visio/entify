#from distutils.core import setup
import os

# Ensuring that Setuptools is install
import ez_setup
ez_setup.use_setuptools()

# Depending on the place in which the project is going to be upgraded
from setuptools import setup
try:
	from pypandoc import convert
	read_md = lambda f: convert(f, 'rst')
except ImportError:
	print("warning: pypandoc module not found, could not convert Markdown to RST")
	read_md = lambda f: open(f, 'r').read()

setup(	name="Entify",
	version="v0.3.0",
	description="entify.py - entify.py is a program designed to extract using regular expressions all the entities from the files on a given folder. This software also provides an interface to look for these entities in any given text.",
	author="Felix Brezo and Yaiza Rubio",
	author_email="contacto@i3visio.com",
	url="http://github.com/i3visio/entify",
	license="COPYING",
	packages=["entify", "entify.lib", "entify.lib.regexp"],
	long_description=read_md("README.md"),
#	long_description=open('README.md').read(),
	install_requires=[
	"argparse",
	"i3visiotools",
#	"pypandoc",
	],
)

