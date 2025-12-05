#!/usr/bin/env python3
"""Test script for the Tint Shop Manager CLI"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.cli import cli

if __name__ == '__main__':
    cli()