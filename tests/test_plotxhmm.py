import unittest
from plotxhmm.plotxhmm import Interval

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
