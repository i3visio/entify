# Looking for files and executing the pydoc application
find ../entify/ -name "*py"  -exec pydoc -w {} \;
# Removing those .html regarding  to  the __init__.py files.
find  -name "__init__*"  -exec rm {} \;

