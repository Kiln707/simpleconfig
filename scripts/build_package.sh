#! /bin/bash
CWD="$PWD"
cd ..
python setup.py sdist bdist_wheel
cd "$CWD"
