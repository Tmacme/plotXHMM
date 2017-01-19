import unittest
from plotxhmm.plotxhmm import Interval, Parser

class TestPlotXHMM(unittest.TestCase):

    def test_interval(self):

        self.assertFalse(Interval('chr1', 1000, 2000).overlaps(Interval('chr2', 1000, 2000)))

        self.assertFalse(Interval('chr1', 1000, 2000).overlaps(Interval('chr1', 3000, 4000)))
        self.assertFalse(Interval('chr1', 1000, 2000).overlaps(Interval('chr1', 500, 999)))
        self.assertFalse(Interval('chr1', 1000, 2000).overlaps(Interval('chr1', 2001, 3000)))

        self.assertTrue(Interval('chr1', 1000, 2000).overlaps(Interval('chr1', 500, 1500)))
        self.assertTrue(Interval('chr1', 1000, 2000).overlaps(Interval('chr1', 1500, 2500)))
        self.assertTrue(Interval('chr1', 1000, 2000).overlaps(Interval('chr1', 500, 1000)))
        self.assertTrue(Interval('chr1', 1000, 2000).overlaps(Interval('chr1', 2000, 2500)))

    def test_parser(self):

        parser = Parser('tests/normalized_zscores.txt')

        deletion_interval = Interval('22', 18898402, 18913235)
        duplication_interval = Interval('22', 17071768, 17073440)

        parser.plot_interval(interval=deletion_interval, sample='HG00121', pdf_file='tests/deletion.pdf')
        parser.plot_interval(interval=duplication_interval, sample='HG00113', pdf_file='tests/duplication.pdf')
