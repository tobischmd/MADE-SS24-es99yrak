#!/bin/bash
rm ./data/population.sqlite
jv -d ./project/pipeline.jv
python3 ./project/pipeline2.py
# python3 ./project/plot.py
# pandoc ./project/data-report.md -o ./project/data-report.pdf -V papersize:a4 -V geometry:margin=2.5cm -V fontsize=11pt