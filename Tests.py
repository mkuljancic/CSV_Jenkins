import filecmp
from csvtest import eingabe
from nose.tools import assert_false,assert_raises
def test_eingabe_sollte_erfolgreich_sein():
    assert_raises(IOError, eingabe("xsxs.csv","rrfr.csv"))

def test_eingabe_bindestrich_fehler_im_dialekt():
    eingabe("infile1.csv","infile2_bindestrich.csv")
    assert_false(filecmp.cmp('outfile_test_eingabe_erfolgreich_1_2.csv','outfile.csv'))

def test_eingabe_punkt_fehler_im_dialekt():
    eingabe("infile1.csv","infile2_fehlerhaft_punkt.csv")
    assert_false(filecmp.cmp('outfile_test_eingabe_erfolgreich_1_2.csv','outfile.csv'))

def test_eingabe_buchstabe_fehler_im_dialekt():
    eingabe("infile1.csv","infile2_buchstabe.csv")
    assert_false(filecmp.cmp('outfile_test_eingabe_erfolgreich_1_2.csv','outfile.csv'))

def test_eingabe_leer():
    eingabe("infile1.csv","infile2_leer.csv")
    assert_false(filecmp.cmp('outfile_test_eingabe_erfolgreich_1_2.csv','outfile.csv'))