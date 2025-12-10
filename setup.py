#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CyberSuite - A Comprehensive Python-Based Cybersecurity Toolkit
"""

from setuptools import setup, find_packages
import os

# Read the long description from README
def read_file(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

# Read requirements
def read_requirements():
    filepath = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name='cybersuite-tools',
    version='1.0.0',
    description='A comprehensive Python-based cybersecurity toolkit with 9 integrated security tools',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    
    # Author information
    author='Naman Goyal',
    author_email='your.email@example.com',  # Update with your email
    
    # Project URLs
    url='https://github.com/Codeguruu03/CyberSuite',
    project_urls={
        'Bug Tracker': 'https://github.com/Codeguruu03/CyberSuite/issues',
        'Documentation': 'https://github.com/Codeguruu03/CyberSuite#readme',
        'Source Code': 'https://github.com/Codeguruu03/CyberSuite',
    },
    
    # License
    license='MIT',
    
    # Package discovery
    packages=find_packages(),
    
    # Package data
    include_package_data=True,
    
    # Python version requirement
    python_requires='>=3.7',
    
    # Dependencies
    install_requires=read_requirements(),
    
    # Optional dependencies
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov>=2.0',
            'black>=21.0',
            'flake8>=3.9',
        ],
        'wifi': [
            'pywifi>=1.1.12',
        ],
    },
    
    # Entry points for command-line scripts
    entry_points={
        'console_scripts': [
            'cybersuite=cybersuite.cli:main',
            'guardgenie=cybersuite.tools.guardgenie:main',
            'steggenie=cybersuite.tools.steggenie:main',
            'scangenie=cybersuite.tools.scangenie:main',
            'hashgenie=cybersuite.tools.hashgenie:main',
            'sqlgenie=cybersuite.tools.sqlgenie:main',
            'wifigenie=cybersuite.tools.wifigenie:main',
            'webgenie=cybersuite.tools.webgenie:main',
            'crackgenie=cybersuite.tools.crackgenie:main',
            'netgenie=cybersuite.tools.netgenie:main',
        ],
    },
    
    # PyPI classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Security',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
        'Environment :: Console',
    ],
    
    # Keywords for PyPI search
    keywords=[
        'cybersecurity',
        'security',
        'penetration-testing',
        'hacking',
        'network-security',
        'password-cracker',
        'steganography',
        'nmap',
        'security-tools',
        'pentesting',
    ],
    
    # Project maturity
    zip_safe=False,
)
