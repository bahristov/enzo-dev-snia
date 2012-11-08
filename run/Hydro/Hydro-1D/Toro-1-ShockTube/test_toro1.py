from yt.mods import *
from yt.funcs import *
from yt.testing import *
from yt.utilities.answer_testing.framework import \
    requires_outputlog, \
    ShockTubeTest
import os

_data_file = 'DD0001/data0001'
_solution_file = 'Toro-1-ShockTube_t=0.2_exact.txt'
_fields = ['Density','x-velocity','Pressure','ThermalEnergy']
_les = [0.0]
_res = [1.0]
_rtol = 1.0e-1
_atol = 1.0e-7

# Verifies that OutputLog exists
@requires_outputlog(os.path.dirname(__file__), "Toro-1-ShockTube.enzo")
def test_toro1():
    test = ShockTubeTest(_data_file, _solution_file, _fields, 
                         _les, _res, _rtol, _atol)
    return test()