__author__ = 'Kuljancic'
import filecmp
from csvtest import eingabe
from nose.tools import assert_true
def test_eingabe_sollte_erfolgreich_sein():
    eingabe("infile1.csv","infile2.csv")
    assert_true(filecmp.cmp('outfile_test_eingabe_erfolgreich_1_2.csv','outfile.csv'))

def test_eingabe_bindestrich_fehler_im_dialekt():
    eingabe("infile1.csv","infile2_bindestrich.csv")
    assert_true(filecmp.cmp('outfile_test_eingabe_bindestrich_fehler_im_dialekt_1_2_fehlerhaft.csv','outfile.csv'))

def test_eingabe_punkt_fehler_im_dialekt():
    eingabe("infile1.csv","infile2_feherhaft_punkt.csv")
    assert_true(filecmp.cmp('outfile_test_eingabe_punkt_fehler_im_dialekt_1_2_fehlerhaft.csv','outfile.csv'))

def test_eingabe_buchstabe_fehler_im_dialekt():
    eingabe("infile1.csv","infile2_buchstabe.csv")
    assert_true(filecmp.cmp('outfile_test_eingabe_buchstabe_fehler_im_dialekt_1_2_fehlerhaft.csv','outfile.csv'))

def test_eingabe_leer():
    eingabe("infile1.csv","infile2_leer.csv")
    assert_true(filecmp.cmp('test_eingabe_leer_1_2_fehlerhaft.csv','outfile.csv'))