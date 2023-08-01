#!/bin/bash

#activate virtual environment
./venv/Scripts/activate

#run test
pytest visualizer_test.py

#exit code of pytest program
exit $?