#!/bin/bash
CWD="$PWD"
cd ..
python -m setup.py clean --all -q
cd "$CWD"
