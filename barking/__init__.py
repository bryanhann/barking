import sys
import os

sys.path.append( os.path.dirname(__file__) )

from util import warn, note

note( f'\n[{__package__}.__init__]:\n\tsys.path += [{sys.path[-1]}]')
