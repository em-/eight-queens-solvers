import sys
import os

path, file = os.path.split(__file__)

sys.path.append(os.path.join(path, 'networkx-0.29-py2.4.egg'))

from networkx import *

sys.path.pop()
