#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
import sys

def run(command)
    status = os.system(command)
    if 0 != status:
        sys.exit(command)

def main():
    generator = os.environ["CMAKE_GENERATOR"]
    run('cmake . -G "%s"' % generator)
    run('cmake --build . --config Release')

if __name__ == '__main__':
    main()
