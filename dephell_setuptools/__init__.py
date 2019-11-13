"""Read metainfo from setup.py
"""
from ._cfg import CfgReader
from ._cmd import CommandReader
from ._constants import FIELDS
from ._manager import read_setup
from ._pkginfo import PkgInfoReader
from ._static import StaticReader


__version__ = '0.1.1'


__all__ = [
    'FIELDS',
    'read_setup',

    'CfgReader',
    'CommandReader',
    'PkgInfoReader',
    'StaticReader',
]
