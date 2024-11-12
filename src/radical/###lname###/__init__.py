
from ###lname###_module import *


# ------------------------------------------------------------------------------
#
import os as _os
import radical.utils as _ru


_root = _os.path.dirname(__file__)

version_short, version_detail, version_base, version_branch, \
        sdist_name, sdist_path = _ru.get_version(_root)
version = version_short


# ------------------------------------------------------------------------------

