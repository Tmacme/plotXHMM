[![Build Status](https://travis-ci.org/micknudsen/plotXHMM.svg?branch=master)](https://travis-ci.org/micknudsen/plotXHMM) [![Coverage Status](https://coveralls.io/repos/github/micknudsen/plotXHMM/badge.svg?branch=master)](https://coveralls.io/github/micknudsen/plotXHMM?branch=master) [![Code Health](https://landscape.io/github/micknudsen/plotXHMM/master/landscape.svg?style=flat)](https://landscape.io/github/micknudsen/plotXHMM/master)

# plotXHMM
Script for making plots from XHMM ([eXome Hidden Markov Model](https://atgu.mgh.harvard.edu/xhmm/)) output. For unknown reasons, the plotting feature included with XHMM runs for days without using any resources.

# Installing plotXHMM

plotXHMM is written in **Python 3.6** and uses `matplotlib` for plotting. The software may (or may not) work with earlier Python versions – use at your own risk!

```
$ pip install git+https://github.com/micknudsen/plotXHMM.git
```

# Running plotXHMM

Among the output files from XHMM is a file containing normalized read depth Z-scores (for a simple example, see [this](tests/normalized_zscores.txt)).
