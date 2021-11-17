#!/bin/bash
CWD="$PWD"
cd ..
python -m setup.py sphinx
cd "$CWD"
