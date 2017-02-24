[![Build Status](https://travis-ci.org/micknudsen/plotXHMM.svg?branch=master)](https://travis-ci.org/micknudsen/plotXHMM)

# plotXHMM
Script for making plots from XHMM ([eXome Hidden Markov Model](https://atgu.mgh.harvard.edu/xhmm/)) output. For unknown reasons, the plotting feature included with XHMM runs for days without using any resources.

# Installing plotXHMM

plotXHMM is written in **Python 3.6** and uses `matplotlib` for plotting. The software may (or may not) work with earlier Python versions – use at your own risk!

The simplest way to install plotXHMM is by using `pip` from the command line:

```
$ pip install git+https://github.com/micknudsen/plotXHMM.git
```

# Running plotXHMM

Among the output files from XHMM is a file containing normalized read depth Z-scores ([example](tests/normalized_zscores.txt)).
