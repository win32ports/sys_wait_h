#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os

def main():
    generator = os.environ["CMAKE_GENERATOR"]
    os.system('cmake . -G "%s"' % generator)
    os.system('cmake --build . --config Release')

if __name__ == '__main__':
    main()
