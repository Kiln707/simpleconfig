#!/bin/bash
CWD="$PWD"
cd ..
twine upload dist/*
cd "$CWD"
