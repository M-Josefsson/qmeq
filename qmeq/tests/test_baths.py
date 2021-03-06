from numpy.linalg import norm
from qmeq.indexing import StateIndexing
from qmeq.baths import *

from qmeq.tests.test_leadstun import ParametersDoubleDotSpinful

EPS = 1e-14


class ParametersDoubleDotSpinfulElPh(ParametersDoubleDotSpinful):

    def __init__(self):
        ParametersDoubleDotSpinful.__init__(self)
        self.nbaths = 2
        self.velph = {
            (0,0,0):1, (0,1,1):2, (0,0,1):1j, (0,1,0):1j, # bath 1, spin up
            (1,0,0):3, (1,1,1):4, (1,0,1):2j, (1,1,0):2j, # bath 2, spin up
            (0,2,2):1, (0,3,3):2, (0,2,3):1j, (0,3,2):1j, # bath 1, spin down
            (1,2,2):3, (1,3,3):4, (1,2,3):2j, (1,3,2):2j, # bath 2, spin down
        }


def test_construct_Vbbp():
    data = {'Lin':    [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 1j, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1j, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0, 1j, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 4, 1j, 0, 0, 1j, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1j, 3, 0, 0, 0, 1j, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 1j, 0, 0, 0, 0], [0, 0, 0, 0, 1j, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1j, 0, 0, 0, 3, 1j, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1j, 0, 0, 1j, 2, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1j, 0, 0, 0, 4, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1j, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1j, 4, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6]], [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 4, 2j, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2j, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 4, 0, 0, 0, 2j, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 8, 2j, 0, 0, 2j, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2j, 7, 0, 0, 0, 2j, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 2j, 0, 0, 0, 0], [0, 0, 0, 0, 2j, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2j, 0, 0, 0, 7, 2j, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2j, 0, 0, 2j, 6, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 2j, 0, 0, 0, 10, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 2j, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2j, 10, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14]]],
            'charge': [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 1j, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1j, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 1j, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1j, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 1j, 1j, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1j, 3, 0, 1j, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1j, 0, 3, 1j, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1j, 1j, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1j, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1j, 4, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1j, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1j, 4, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6]], [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 4, 2j, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2j, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 4, 2j, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2j, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 8, 2j, 2j, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2j, 7, 0, 2j, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2j, 0, 7, 2j, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 2j, 2j, 6, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 2j, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2j, 10, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 2j, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2j, 10, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14]]],
            'sz':     [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 1j, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1j, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 1j, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1j, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 1j, 1j, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1j, 3, 0, 1j, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1j, 0, 3, 1j, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1j, 1j, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1j, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1j, 4, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1j, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1j, 4, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6]], [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 4, 2j, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2j, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 4, 2j, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2j, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 8, 2j, 2j, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2j, 7, 0, 2j, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2j, 0, 7, 2j, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 2j, 2j, 6, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 2j, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2j, 10, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 2j, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2j, 10, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14]]],
            'ssq':    [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 1j, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1j, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 1j, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1j, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 1j, 1j, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1j, 3, 0, 1j, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1j, 0, 3, 1j, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1j, 1j, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1j, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1j, 4, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1j, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1j, 4, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6]], [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 4, 2j, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2j, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 4, 2j, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2j, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 8, 2j, 2j, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2j, 7, 0, 2j, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2j, 0, 7, 2j, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 2j, 2j, 6, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 2j, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2j, 10, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 2j, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2j, 10, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14]]]}
    p = ParametersDoubleDotSpinfulElPh()
    for indexing in ['Lin', 'charge', 'sz', 'ssq']:
        si = StateIndexing(4, indexing=indexing)
        baths = PhononBaths(p.nbaths, {}, si, {}, {}, {})
        Vbbp = elph_construct_Vbbp(baths, p.velph)
        assert norm(Vbbp - data[indexing]) < EPS


def test_rotate_Vbbp():
    data = {'Lin':    [[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.5-1.0j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.5-1.0j, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 3.0-1.7888543819998315j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5257311121191336, 0.0, 0.8944271909999155j, 0.0, 0.0, 0.0], [0.0, 0.0, -0.5, 0.0, 1.5+1.0j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5-1.0j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 0.0], [0.0, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.5+1.0j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, -0.5257311121191336, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.8506508083520395, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5-1.0j, 0.0, -0.5, 0.0, 0.0], [0.0, 0.0, 0.0, 0.8944271909999156j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8506508083520395, 0.0, 3.0+1.7888543819998302j, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 0.0, 4.5+1.0j, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5+1.0j, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.0]], [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 3.5-2.0j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 3.5-2.0j, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 7.0-3.577708763999663j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5257311121191335, 0.0, 1.788854381999831j, 0.0, 0.0, 0.0], [0.0, 0.0, -0.5, 0.0, 3.5+2.0j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 7.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10.5-2.0j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 0.0], [0.0, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.5+2.0j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, -0.5257311121191336, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.0, 0.0, 0.8506508083520394, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10.5-2.0j, 0.0, -0.5, 0.0, 0.0], [0.0, 0.0, 0.0, 1.7888543819998313j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8506508083520391, 0.0, 7.0+3.5777087639996603j, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 0.0, 10.5+2.0j, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10.5+2.0j, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 14.0]]],
            'charge': [[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.5-1.0j, 0.0, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.5-1.0j, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, -0.5, 1.5+1.0j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, -0.5, 0.0, 0.0, 1.5+1.0j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 3.0-1.7888543819998315j, 0.0, 0.0, 0.0, -0.5257311121191336, 0.8944271909999155j, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, -0.5257311121191336, 0.0, 0.0, 0.0, 3.0, 0.8506508083520395, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.8944271909999156j, 0.0, 0.0, 0.0, 0.8506508083520395, 3.0+1.7888543819998302j, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5-1.0j, 0.0, 0.0, -0.5, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5-1.0j, -0.5, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 4.5+1.0j, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 0.0, 0.0, 4.5+1.0j, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.0]], [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 3.5-2.0j, 0.0, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 3.5-2.0j, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, -0.5, 3.5+2.0j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, -0.5, 0.0, 0.0, 3.5+2.0j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 7.0-3.577708763999663j, 0.0, 0.0, 0.0, -0.5257311121191335, 1.788854381999831j, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, -0.5257311121191336, 0.0, 0.0, 0.0, 7.0, 0.8506508083520394, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.7888543819998313j, 0.0, 0.0, 0.0, 0.8506508083520391, 7.0+3.5777087639996603j, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10.5-2.0j, 0.0, 0.0, -0.5, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10.5-2.0j, -0.5, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 10.5+2.0j, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 0.0, 0.0, 10.5+2.0j, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 14.0]]],
            'sz':     [[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.5-1.0j, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, -0.5, 1.5+1.0j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.5-1.0j, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, -0.5, 1.5+1.0j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0-1.7888543819998315j, 0.0, -0.5257311121191336, 0.8944271909999155j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5257311121191336, 0.0, 3.0, 0.8506508083520395, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8944271909999156j, 0.0, 0.8506508083520395, 3.0+1.7888543819998302j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5-1.0j, -0.5, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 4.5+1.0j, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5-1.0j, -0.5, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 4.5+1.0j, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.0]], [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 3.5-2.0j, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, -0.5, 3.5+2.0j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 3.5-2.0j, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, -0.5, 3.5+2.0j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 7.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.0-3.577708763999663j, 0.0, -0.5257311121191335, 1.788854381999831j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5257311121191336, 0.0, 7.0, 0.8506508083520394, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.7888543819998313j, 0.0, 0.8506508083520391, 7.0+3.5777087639996603j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10.5-2.0j, -0.5, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 10.5+2.0j, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10.5-2.0j, -0.5, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 10.5+2.0j, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 14.0]]],
            'ssq':    [[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.5-1.0j, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, -0.5, 1.5+1.0j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.5-1.0j, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, -0.5, 1.5+1.0j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0-1.7888543819998315j, -0.5257311121191329, 0.8944271909999164j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5257311121191329, 3.0, 0.8506508083520398, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8944271909999163j, 0.8506508083520398, 3.0+1.7888543819998317j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5-1.0j, -0.5, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 4.5+1.0j, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5-1.0j, -0.5, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 4.5+1.0j, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6+0j]], [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 3.5-2.0j, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, -0.5, 3.5+2.0j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 3.5-2.0j, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, -0.5, 3.5+2.0j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 7.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.0-3.577708763999662j, -0.5257311121191319, 1.7888543819998328j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.525731112119132, 7.0, 0.850650808352039, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.7888543819998326j, 0.8506508083520389, 7.0+3.5777087639996634j, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10.5-2.0j, -0.5, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 10.5+2.0j, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10.5-2.0j, -0.5, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 10.5+2.0j, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 14.0]]]}
    p = ParametersDoubleDotSpinfulElPh()
    for indexing in ['Lin', 'charge', 'sz', 'ssq']:
        si = StateIndexing(4, indexing=indexing)
        leads = PhononBaths(p.nbaths, {}, si, {}, {}, {})
        Tba0 = elph_construct_Vbbp(leads, p.velph)
        Tba = elph_rotate_Vbbp(Tba0, p.vecs[indexing], si)
        assert norm(Tba - data[indexing]) < EPS


def test_make_velph_dict():
    nsingle = 4
    nbaths = 2
    si = StateIndexing(nsingle)
    si.nbaths = nbaths
    #
    b1_cL, b1_cR, b1_oL, b1_oR = 7.0, 5.0, 2.0j, 1.0j
    b2_cL, b2_cR, b2_oL, b2_oR = 70.0, 50.0, 20.0j, 10.0j
    velph_dict = {(0,0,0): b1_cL, (0,2,2): b1_cL, (0,1,1): b1_cR, (0,3,3): b1_cR, (0,0,1): b1_oL, (0,1,0): b1_oR, (0,2,3): b1_oL, (0,3,2): b1_oR,
                  (1,0,0): b2_cL, (1,2,2): b2_cL, (1,1,1): b2_cR, (1,3,3): b2_cR, (1,0,1): b2_oL, (1,1,0): b2_oR, (1,2,3): b2_oL, (1,3,2): b2_oR}
    velph_list = [[0,0,0,b1_cL], [0,2,2,b1_cL], [0,1,1,b1_cR], [0,3,3,b1_cR], [0,0,1,b1_oL], [0,1,0,b1_oR], [0,2,3,b1_oL], [0,3,2,b1_oR],
                  [1,0,0,b2_cL], [1,2,2,b2_cL], [1,1,1,b2_cR], [1,3,3,b2_cR], [1,0,1,b2_oL], [1,1,0,b2_oR], [1,2,3,b2_oL], [1,3,2,b2_oR]]
    velph_mtr = [[[b1_cL, b1_oL, 0.0, 0.0], [b1_oR, b1_cR, 0.0, 0.0], [0.0, 0.0, b1_cL, b1_oL], [0.0, 0.0, b1_oR, b1_cR]],
                 [[b2_cL, b2_oL, 0.0, 0.0], [b2_oR, b2_cR, 0.0, 0.0], [0.0, 0.0, b2_cL, b2_oL], [0.0, 0.0, b2_oR, b2_cR]]]
    assert make_velph_dict(velph_list, si) == velph_dict
    assert make_velph_dict(velph_dict, si) == velph_dict
    assert make_velph_dict(np.array(velph_mtr), si) == velph_dict


def test_PhononBaths():
    nsingle = 2
    nbaths = 2
    b1_elph_d, b1_elph_o = 1.0, 2.0
    b2_elph_d, b2_elph_o = 3.0, 4.0
    temp_ph, dband_ph_min, dband_ph_max = 1.0, 0.1, 60.0
    dband_ph = [dband_ph_min, dband_ph_max]
    tlst_ph  = {0: temp_ph, 1: temp_ph}
    dlst_ph  = {0: dband_ph, 1: dband_ph}
    velph = np.array([[[b1_elph_d,b1_elph_o], [b1_elph_o,b1_elph_d]],
                      [[b2_elph_d,b2_elph_o], [b2_elph_o,b2_elph_d]]])
    si = StateIndexing(nsingle)
    baths = PhononBaths(nbaths, velph, si, tlst_ph, dlst_ph)
    #
    velph_dict = {(0,0,0):b1_elph_d, (0,1,1):b1_elph_d, (0,0,1):b1_elph_o, (0,1,0):b1_elph_o,
                  (1,0,0):b2_elph_d, (1,1,1):b2_elph_d, (1,0,1):b2_elph_o, (1,1,0):b2_elph_o}
    assert baths.velph == velph_dict
    assert baths.si.nbaths == 2
    assert baths.tlst_ph.tolist() == [temp_ph, temp_ph]
    assert baths.dlst_ph.tolist() == [dband_ph, dband_ph]
    #
    baths.add(velph={(0,0,0):1.0, (0,1,1):2.0, (0,0,1):3.0, (0,1,0):4.0,
                     (1,0,0):5.0, (1,1,1):6.0, (1,0,1):7.0, (1,1,0):8.0},
              tlst_ph={0:1.0, 1:2.0},
              dlst_ph={0:[1.0,2.0], 1:[3.0,4.0]})
    assert baths.velph == {(0,0,0):b1_elph_d+1.0, (0,1,1):b1_elph_d+2.0, (0,0,1):b1_elph_o+3.0, (0,1,0):b1_elph_o+4.0,
                           (1,0,0):b2_elph_d+5.0, (1,1,1):b2_elph_d+6.0, (1,0,1):b2_elph_o+7.0, (1,1,0):b2_elph_o+8.0}
    assert baths.tlst_ph.tolist() == [temp_ph+1.0, temp_ph+2.0]
    assert baths.dlst_ph.tolist() == [[dband_ph_min+1.0,dband_ph_max+2.0], [dband_ph_min+3.0,dband_ph_max+4.0]]
    #
    baths.change(velph=velph_dict,
                 tlst_ph=[temp_ph, temp_ph],
                 dlst_ph=[dband_ph, dband_ph])
    assert baths.velph == velph_dict
    assert baths.tlst_ph.tolist() == [temp_ph, temp_ph]
    assert baths.dlst_ph.tolist() == [dband_ph, dband_ph]
    #
    baths.change(tlst_ph={1: 2.13}, dlst_ph={1: [3.21,3.22]})
    assert baths.tlst_ph.tolist() == [temp_ph, 2.13]
    assert baths.dlst_ph.tolist() == [[dband_ph_min,dband_ph_max], [3.21,3.22]]
    baths.add(tlst_ph={1: 2.13}, dlst_ph={1: [3.21,3.22]})
    assert baths.tlst_ph.tolist() == [temp_ph, 2*2.13]
    assert baths.dlst_ph.tolist() == [[dband_ph_min,dband_ph_max], [2*3.21,2*3.22]]
    #
    baths.change(tlst_ph=2)
    assert baths.tlst_ph.tolist() == [2, 2]
    baths.change(tlst_ph=tlst_ph)
    baths.add(tlst_ph=2)
    assert baths.tlst_ph.tolist() == [temp_ph+2, temp_ph+2]
    #
    Tba_tmp = np.array(baths.Vbbp)
    baths.Vbbp = None
    baths.use_Vbbp0()
    assert norm(baths.Vbbp - Tba_tmp) < EPS


def test_PhononBaths_spin():
    nsingle = 4
    nbaths = 2
    b1_elph_d, b1_elph_o = 1.0, 2.0
    b2_elph_d, b2_elph_o = 3.0, 4.0
    temp_ph, dband_ph_min, dband_ph_max = 1.0, 0.1, 60.0
    dband_ph = [dband_ph_min, dband_ph_max]
    tlst_ph  = {0: temp_ph, 1: temp_ph}
    dlst_ph  = {0: dband_ph, 1: dband_ph}
    velph = np.array([[[b1_elph_d,b1_elph_o], [b1_elph_o,b1_elph_d]],
                      [[b2_elph_d,b2_elph_o], [b2_elph_o,b2_elph_d]]])
    si = StateIndexing(nsingle, symmetry='spin')
    baths = PhononBaths(nbaths, velph, si, tlst_ph, dlst_ph)
    #
    velph_dict_no_spin = {(0,0,0):b1_elph_d, (0,1,1):b1_elph_d, (0,0,1):b1_elph_o, (0,1,0):b1_elph_o,
                          (1,0,0):b2_elph_d, (1,1,1):b2_elph_d, (1,0,1):b2_elph_o, (1,1,0):b2_elph_o}
    velph_dict = {(0,0,0):b1_elph_d, (0,1,1):b1_elph_d, (0,0,1):b1_elph_o, (0,1,0):b1_elph_o,
                  (1,0,0):b2_elph_d, (1,1,1):b2_elph_d, (1,0,1):b2_elph_o, (1,1,0):b2_elph_o,
                  (0,2,2):b1_elph_d, (0,3,3):b1_elph_d, (0,2,3):b1_elph_o, (0,3,2):b1_elph_o,
                  (1,2,2):b2_elph_d, (1,3,3):b2_elph_d, (1,2,3):b2_elph_o, (1,3,2):b2_elph_o}
    assert baths.velph == velph_dict
    assert baths.si.nbaths == 2
    assert baths.tlst_ph.tolist() == [temp_ph, temp_ph]
    assert baths.dlst_ph.tolist() == [dband_ph, dband_ph]
    #
    baths.add(velph={(0,0,0):1.0, (0,1,1):2.0, (0,0,1):3.0, (0,1,0):4.0,
                     (1,0,0):5.0, (1,1,1):6.0, (1,0,1):7.0, (1,1,0):8.0},
              tlst_ph={0:1.0, 1:2.0},
              dlst_ph={0:[1.0,2.0], 1:[3.0,4.0]})
    assert baths.velph == {(0,0,0):b1_elph_d+1.0, (0,1,1):b1_elph_d+2.0, (0,0,1):b1_elph_o+3.0, (0,1,0):b1_elph_o+4.0,
                           (1,0,0):b2_elph_d+5.0, (1,1,1):b2_elph_d+6.0, (1,0,1):b2_elph_o+7.0, (1,1,0):b2_elph_o+8.0,
                           (0,2,2):b1_elph_d+1.0, (0,3,3):b1_elph_d+2.0, (0,2,3):b1_elph_o+3.0, (0,3,2):b1_elph_o+4.0,
                           (1,2,2):b2_elph_d+5.0, (1,3,3):b2_elph_d+6.0, (1,2,3):b2_elph_o+7.0, (1,3,2):b2_elph_o+8.0}
    assert baths.tlst_ph.tolist() == [temp_ph+1.0, temp_ph+2.0]
    assert baths.dlst_ph.tolist() == [[dband_ph_min+1.0,dband_ph_max+2.0], [dband_ph_min+3.0,dband_ph_max+4.0]]
    #
    baths.change(velph=velph_dict_no_spin,
                 tlst_ph=[temp_ph, temp_ph],
                 dlst_ph=[dband_ph, dband_ph])
    assert baths.velph == velph_dict
    assert baths.tlst_ph.tolist() == [temp_ph, temp_ph]
    assert baths.dlst_ph.tolist() == [dband_ph, dband_ph]
    #
    baths.change(tlst_ph={1: 2.13}, dlst_ph={1: [3.21,3.22]})
    assert baths.tlst_ph.tolist() == [temp_ph, 2.13]
    assert baths.dlst_ph.tolist() == [[dband_ph_min,dband_ph_max], [3.21,3.22]]
    baths.add(tlst_ph={1: 2.13}, dlst_ph={1: [3.21,3.22]})
    assert baths.tlst_ph.tolist() == [temp_ph, 2*2.13]
    assert baths.dlst_ph.tolist() == [[dband_ph_min,dband_ph_max], [2*3.21,2*3.22]]
    #
    baths.change(tlst_ph=2)
    assert baths.tlst_ph.tolist() == [2, 2]
    baths.change(tlst_ph=tlst_ph)
    baths.add(tlst_ph=2)
    assert baths.tlst_ph.tolist() == [temp_ph+2, temp_ph+2]
    #
    Tba_tmp = np.array(baths.Vbbp)
    baths.Vbbp = None
    baths.use_Vbbp0()
    assert norm(baths.Vbbp - Tba_tmp) < EPS
