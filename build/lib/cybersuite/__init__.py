#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CyberSuite - A Comprehensive Python-Based Cybersecurity Toolkit

Copyright (c) 2024 Naman Goyal
Licensed under the MIT License
"""

__version__ = '1.0.0'
__author__ = 'Naman Goyal'
__email__ = 'your.email@example.com'
__license__ = 'MIT'

# Package metadata
__all__ = [
    '__version__',
    '__author__',
    '__email__',
    '__license__',
]

# Import utils for convenience
from cybersuite.utils import (
    validate_ip,
    validate_hostname,
    validate_ip_or_hostname,
    validate_file_path,
    validate_image_file,
    validate_url,
    print_error,
    print_success,
    print_warning,
    print_info,
    clear_screen,
    return_to_main,
    export_results,
    setup_logging,
)

# Tool imports for convenience
from cybersuite.tools import (
    guardgenie,
    steggenie,
    scangenie,
    hashgenie,
    sqlgenie,
    wifigenie,
    webgenie,
    crackgenie,
    netgenie,
)
