#-----------------------------------------------------------------------------
# Copyright (c) 2016-2018, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

"""
python-PyCUDA: https://github.com/minrk/PyCUDA
"""

from PyInstaller.utils.hooks import copy_metadata 

datas  = copy_metadata('pycuda')
