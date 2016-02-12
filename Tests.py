__author__ = 'Kuljancic'
import filecmp
from csvtest import eingabe
def test_eingabe_sollte_erfolgreich_sein():
    eingabe("infile1.csv","infile2.csv")
    assert filecmp.cmp('outfile_test_eingabe_erfolgreich_1_2.csv','outfile.csv')

