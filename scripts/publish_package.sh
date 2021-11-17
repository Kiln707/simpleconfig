#!/bin/bash
CWD="$PWD"
cd ..
twine upload pysimpleconfig dist/*
cd "$CWD"
