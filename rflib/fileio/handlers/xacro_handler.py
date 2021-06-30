"""
A handler to parse and convert Xacro file to other useful formats:
1. urdf

This file only deals with format conversion and has nothing to do with the 3D computing.

Author: Wenqiang Xu
"""

from .base import BaseFileHandler

class XacroHandler(BaseFileHandler):
    def load_from_fileobj(self, file, **kwargs):
        raise NotImplementedError

    def dump_to_fileobj(self, obj, file, **kwargs):
        raise NotImplementedError

    def dump_to_str(self, obj, **kwargs):
        raise NotImplementedError

    def load_from_path(self, filepath, mode='r', **kwargs):
        with open(filepath, mode) as f:
            return self.load_from_fileobj(f, **kwargs)

    def dump_to_path(self, obj, filepath, mode='w', **kwargs):
        with open(filepath, mode) as f:
            self.dump_to_fileobj(obj, f, **kwargs)
        
    def to_urdf(self):
        pass