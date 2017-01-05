import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use('ggplot')

class Parser:

    def __init__(self, normalized_zscores_file):
        self._df = pd.read_csv(normalized_zscores_file, sep='\t', index_col='Matrix')
        self._df.index.names = ['SAMPLE']

    def _zscores_subset(self, interval):

        selected_columns = []

        for column in self._df.columns:

            chromosome = column.split(':')[0]
            start = int(column.split(':')[1].split('-')[0])
            end = int(column.split(':')[1].split('-')[1])

            if interval.overlaps(Interval(chromosome, start, end)):
                selected_columns.append(column)

        return self._df[selected_columns]

    def plot_interval(self, interval, sample, pdf_file):

        df = self._zscores_subset(interval)

        x_ticks = []
        for column in df.columns:
            start = int(column.split(':')[1].split('-')[0])
            end = int(column.split(':')[1].split('-')[1])
            x_ticks.append(int(start + (end - start) / 2))

        df.columns = x_ticks

        plt.figure()

        _, ax = plt.subplots()
        ax.ticklabel_format(style='plain')

        plt.ylabel('Normalized Read Depth Z-Score')

        for this_sample, row in df.iterrows():

            if this_sample == sample:
                row.plot(linewidth=3.0, color='red')

            else:
                row.plot(linewidth=0.25, color='black')

        plt.title(sample)
        plt.savefig(pdf_file)


class Interval:
    ''' Reperesents an interval (1-based, end inclusive) from an IntervalList. '''

    def __init__(self, chromosome, start, end):

        self._chromosome = chromosome
        self._start = start
        self._end = end

    def overlaps(self, other_interval):

        if not self.chromosome == other_interval.chromosome:
            return False

        if self.start <= other_interval.start and other_interval.start <= self.end:
            return True

        if self.start <= other_interval.end and other_interval.end <= self.end:
            return True

        return False

    @property
    def chromosome(self):
        return self._chromosome

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end
