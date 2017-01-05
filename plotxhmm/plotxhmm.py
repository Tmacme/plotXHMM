import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use('ggplot')


class Parser:
    ''' Must be initialized with an XHMM output file containing normalized
        read depth Z-scores. Following the XHMM tutorial, such files are
        name SAMPLE_NAME.PCA_normalized.filtered.sample_zscores.RD.txt. '''

    def __init__(self, normalized_zscores_file):
        self._df = pd.read_csv(normalized_zscores_file, sep='\t', index_col='Matrix')
        self._df.index.names = ['SAMPLE']

    def _zscores_subset(self, interval):
        ''' Returns dataframe with subset of Z-scores corresponding to targets overlapping
            with a given interval. Column names are target midpoints. '''

        selected_columns = []
        target_midpoints = []

        for column in self._df.columns:

            # Assuming that column names are on the form CHROMOSOME:START-END
            chromosome = column.split(':')[0]
            start = int(column.split(':')[1].split('-')[0])
            end = int(column.split(':')[1].split('-')[1])

            # Keep only columns overlapping with interval
            column_interval = Interval(chromosome, start, end)
            if interval.overlaps(column_interval):
                selected_columns.append(column)
                target_midpoints.append(int(start + (end - start) / 2))

        subset_df = self._df[selected_columns]
        subset_df.columns = target_midpoints

        return subset_df

    def plot_interval(self, interval, sample, pdf_file):
        ''' Plot Z-scores corresponding to targets overlapping with a given
            interval. The specified sample is highlighted. Output is in PDF format. '''

        # Get the Z-scores
        df = self._zscores_subset(interval)

        # Create new figure
        fig = plt.figure()

        # Avoid scientific notation on axes
        ax = fig.add_subplot(111)
        ax.ticklabel_format(useOffset=False, style='plain')

        for this_sample, row in df.iterrows():

            # Highlight sample
            if this_sample == sample:
                row.plot(linewidth=3.0, color='red')

            # All other samples not highlighted
            else:
                row.plot(linewidth=0.25, color='black')

        plt.title(sample)
        plt.xlabel(f'Position (Chromosome {interval.chromosome})')
        plt.ylabel('Normalized Read Depth Z-Score')

        plt.savefig(pdf_file)


class Interval:
    ''' Reperesents an interval (1-based, end inclusive) from an IntervalList. '''

    def __init__(self, chromosome, start, end):

        self._chromosome = chromosome
        self._start = start
        self._end = end

    def overlaps(self, other_interval):

        # Intervals are on different chromosomes
        if not self.chromosome == other_interval.chromosome:
            return False

        # The start of other_interval is within this interval
        if self.start <= other_interval.start and other_interval.start <= self.end:
            return True

        # The end of other_interval is within this interval
        if self.start <= other_interval.end and other_interval.end <= self.end:
            return True

        # Intervals are on same chromosome but do not overlap
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
