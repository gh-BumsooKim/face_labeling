import sys
import cv2

"""
import face_recognition
import cv2
import numpy as np
import os
from tkinter import *
from tkinter import ttk
import threading
import time
"""
# Python Version Dependency
if sys.version_info[:2] < (3, 6):
    msg = (
    "This auto_labeling package is dependencies upper than Python 3.6"
    )
    raise RuntimeError(msg)
    
# System Dependency for directory path
if 'win' in sys.platform.lower():
    pass
else:
    msg = """
        This auto_labeling package is supported
        Only Windows Platform
        Officially Not Support Platform : Linux
        """
    raise RuntimeError(msg)

try:
    from .save_annotation_file import *
    from .label_format import *
    from .class_info_interface import *
    from .cap_init import *
    from .version import version as __version__
except ImportError as e:
    print("Subpackage is not imported\n"
        "with ImportError :", e)
