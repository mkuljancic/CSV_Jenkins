__author__ = 'Mirza Kuljancic'

# Dieses Programm liest mehrere CSV-Dateien mit unterschiedlichen Dialekten
# ein und schreibt die Daten aus beiden Dateien in ein weiteres CSV-File.

import csv

# Zuerst definieren wir drei CSV-Dialekte:

# Komma-getrennt
csv.register_dialect('komma', delimiter=',', quotechar='"')

# Semikolon-getrennt
csv.register_dialect('semikolon', delimiter=';', quotechar='"')

# Leerzeichen-getrennt
csv.register_dialect('space', delimiter=' ', quotechar='"')

# Nun legen wir unsere Ein- und Ausgabedateien und die zu benutzenden Dialekte fest:
def eingabe(file1,file2):
  infiles = [[file1, 'komma'],
             [file2, 'semikolon']]

  outfile = ['outfile.csv', 'space']

  # Wir erzeugen eine Liste, in der die Eingabezeilen gespeichert werden.

  rows = []

  # Nun iterieren wir ueber alle Eingabedateien und speichern deren Zeilen in der Liste.

  for infile in infiles:
    with open(infile[0], 'rt') as csvfile:
      myreader = csv.reader(csvfile, infile[1])
      for row in myreader:
        rows.append(row)

  # Die Liste schreiben wir nun in die Ausgabedatei.

  with open(outfile[0], 'wt') as csvfile:
    mywriter = csv.writer(csvfile, outfile[1])
    for row in rows:
      mywriter.writerow(row)

eingabe('infile1.csv','infile2.csv')