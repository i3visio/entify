	=============================================================
	entify  Copyright (C) 2014  F. Brezo and Y. Rubio, i3visio
	=============================================================

Description:
============
entify is a GPLv3 piece of software that looks for regular expressions in 
a series of files in a folder. It can also be imported by other modules to 
look for entities in any kind of data.

License: GPLv3
==============

This is free software, and you are welcome to redistribute it under certain conditions.

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.


For more details on this issue, run:
```
	python entify-launcher.py --license
```

Installation:
=============
The installation under Python 2.7 for the release package Entify-v0.x.x is as follows:
```
git clone http://github.com/i3visio/entify
cd entify-master
sudo python setup.py build
sudo python setup.py install
```
or
```
wget http://github.com/i3visio/entify/archive/master.zip
unzip master.zip
cd master
sudo python setup.py build
sudo python setup.py install
```
Superuser privileges are required so as to complete the installation. Afterwards, 
the module will be importable from any python code. You can check this by typing:
```
python -c "import entify"
```
If no error is displayed, the installation would have been performed correctly.

Usage:
======
So as to run the program, navigate to entify-master/entify/ and run:
```
python entify-launcher.py -h
```
The usage is described as follows:
```
usage: entify.py
                 (-r <name> [<name> ...] | -R <regular_expression> [<regular_expression> ...])
                 [-e <sum_ext> [<sum_ext> ...]] -f <path_to_input_folder>
                 [-o <path_to_output_folder>] [--recursive] [-v <verbosity>]
                 [-h] [--version]
```

The functionalities are described as follows:
```
Input options (one required):
  -r <name> [<name> ...], --regexp <name> [<name> ...]
                        select the regular expressions to be looked for
                        amongst the following: ['all', 'email', 'md5']
  -R <regular_expression> [<regular_expression> ...], --new_regexp <regular_expression> [<regular_expression> ...]
                        add a new regular expression, for example, for testing
                        purposes.

Input and output arguments:
  Configuring the input and output options.

  -e <sum_ext> [<sum_ext> ...], --extension <sum_ext> [<sum_ext> ...]
                        output extension for the summary files (at least one
                        is required).
  -i <path_to_input_folder>, --input_folder <path_to_input_folder>
                        path to the file where the list of Classes is stored
                        (one per line).
  -o <path_to_output_folder>, --output_folder <path_to_output_folder>
                        path to the output folder where the results will be
                        stored.
  --recursive           Variable to tell the system to perform a recursive
                        search on the folder tree.
  -v <verbosity>, --verbose <verbosity>
                        select the verbosity level: 0 - none; 1 - normal
                        (default); 2 - debug.

About arguments:
  Showing additional information about this program.

  -h, --help            shows this help and exists.
  --version             shows the version of the program and exists.
```

