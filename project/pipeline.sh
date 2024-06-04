#!/bin/bash
rm ./data/population.sqlite
jv -d ./project/pipeline.jv
python3 ./project/pipeline2.py
python3 ./project/plot.py