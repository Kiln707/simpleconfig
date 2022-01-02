#! /bin/bash
CWD="$PWD"
cd ..
python3 setup.py sdist bdist_wheel
cd "$CWD"
