#!/bin/bash
CWD="$PWD"
cd ..
tox
cd "$CWD"
