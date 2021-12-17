#!/bin/bash
CWD="$PWD"
cd ..
python3 -m setup.py clean --all -q
cd "$CWD"
