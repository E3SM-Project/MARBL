#!/usr/bin/env python

from sys import path
import os

path.insert(0, os.path.join('..', '..', 'python_for_tests'))
from marbl_testing_class import MARBL_testcase

mt = MARBL_testcase()

mt.parse_args(desc='Run set_surface_forcing and set_interior_forcing', RequireNetCDF=True)

mt.build_exe()

mt.run_exe()
