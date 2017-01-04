import pandas as pd


class Parser:

    def __init__(self, normalized_zscores_file):
        self._df = pd.read_csv(normalized_zscores_file, sep='\t', index_col='Matrix')


class Interval:

    def __init__(self, chromosome, start, end):

        self._chromosome = chromosome
        self._start = start
        self._end = end
