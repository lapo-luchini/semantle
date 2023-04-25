#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import psutil

from gensim.models.fasttext import FastTextKeyedVectors
from gensim.models import fasttext
from gensim.test.utils import datapath

def test():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    vector = "cc.it.300.bin"

    # model = fasttext.load_facebook_vectors(vector)
    # model.save(vector + ".nat")
    model = FastTextKeyedVectors.load(vector + '.nat', mmap='r')
    model.save_word2vec_format(vector + '.nat.txt', binary=False)

    for word in ["parola", "io", "minore"]:  # show wv logic changes
        print(word, "~", model.most_similar(word))

    # model2 = model.

    # print("Memory usage:", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    # print("Memory usage:", psutil.Process().memory_info().peak_wset)
    print("Memory usage:", psutil.Process().memory_full_info().uss)

if __name__ == '__main__':
    test()

# parola ~ [('frase', 0.7169997692108154), ('parolina', 0.688976526260376), ('parola.E', 0.6847797632217407), ('parola-', 0.664254367351532), ('parola.La', 0.6608023643493652), ('parola.', 0.6410355567932129), ('parola.Ma', 0.6377108097076416), ('non-parola', 0.6258244514465332), ('parola-per-parola', 0.622776448726654), ('Parola', 0.6223967671394348)]
# io ~ [('Io', 0.8708587884902954), ('ho', 0.7473310828208923), ('io.Io', 0.6997716426849365), ('so', 0.6866539120674133), ('.Io', 0.6813687086105347), ('no.Io', 0.6325652003288269), ('IO', 0.6211111545562744), ('ma', 0.615341067314148), ('me', 0.6153181195259094), ("anc'", 0.6120693683624268)]
# minore ~ [('maggiore', 0.7923381328582764), ('minore.', 0.6612551212310791), ('Minore', 0.6365795135498047), ('minor', 0.6280611157417297), ('minore.La', 0.6125938892364502), ('minori', 0.5779601335525513), ('inferiore', 0.564867377281189), ('fratello', 0.5504770278930664), ('uguale', 0.5464020371437073), ('maggiore-minore', 0.5371068716049194)]
# Memory usage: 8008241152

# parola ~ [('frase', 0.7169997692108154), ('parolina', 0.688976526260376), ('parola.E', 0.6847797632217407), ('parola-', 0.664254367351532), ('parola.La', 0.6608023643493652), ('parola.', 0.6410355567932129), ('parola.Ma', 0.6377108097076416), ('non-parola', 0.6258244514465332), ('parola-per-parola', 0.622776448726654), ('Parola', 0.6223967671394348)]
# io ~ [('Io', 0.8708587884902954), ('ho', 0.7473310828208923), ('io.Io', 0.6997716426849365), ('so', 0.6866539120674133), ('.Io', 0.6813687086105347), ('no.Io', 0.6325652003288269), ('IO', 0.6211111545562744), ('ma', 0.615341067314148), ('me', 0.6153181195259094), ("anc'", 0.6120693683624268)]
# minore ~ [('maggiore', 0.7923381328582764), ('minore.', 0.6612551212310791), ('Minore', 0.6365795135498047), ('minor', 0.6280611157417297), ('minore.La', 0.6125938892364502), ('minori', 0.5779601335525513), ('inferiore', 0.564867377281189), ('fratello', 0.5504770278930664), ('uguale', 0.5464020371437073), ('maggiore-minore', 0.5371068716049194)]
# Memory usage: 7908945920

# parola ~ [('frase', 0.7169997692108154), ('parolina', 0.688976526260376), ('parola.E', 0.6847797632217407), ('parola-', 0.664254367351532), ('parola.La', 0.6608023643493652), ('parola.', 0.6410355567932129), ('parola.Ma', 0.6377108097076416), ('non-parola', 0.6258244514465332), ('parola-per-parola', 0.622776448726654), ('Parola', 0.6223967671394348)]
# io ~ [('Io', 0.8708587884902954), ('ho', 0.7473310828208923), ('io.Io', 0.6997716426849365), ('so', 0.6866539120674133), ('.Io', 0.6813687086105347), ('no.Io', 0.6325652003288269), ('IO', 0.6211111545562744), ('ma', 0.615341067314148), ('me', 0.6153181195259094), ("anc'", 0.6120693683624268)]
# minore ~ [('maggiore', 0.7923381328582764), ('minore.', 0.6612551212310791), ('Minore', 0.6365795135498047), ('minor', 0.6280611157417297), ('minore.La', 0.6125938892364502), ('minori', 0.5779601335525513), ('inferiore', 0.564867377281189), ('fratello', 0.5504770278930664), ('uguale', 0.5464020371437073), ('maggiore-minore', 0.5371068716049194)]
# Memory usage: 3108937728
