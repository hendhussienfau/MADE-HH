#!/bin/bash

pip install pytest
pip install pandas
pip install sqlite3
pip install tabulate


python3 ./project/Pipeline.py
python3 ./project/pipeline_test.py
