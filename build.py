#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
import sys

def run(command):
    status = os.system(command)
    if 0 != status:
        sys.exit(command)

def remove_sh_from_path():
    path = os.environ["PATH"]
    path = path.split(os.pathsep)
    for entry in path:
        if os.path.isfile(os.path.join(entry, "sh.exe")):
            path.remove(entry)
    path = os.pathsep.join(path)
    os.environ["PATH"] = path

def main():
    remove_sh_from_path()
    generator = os.environ["CMAKE_GENERATOR"]
    command = 'cmake . -G "%s"' % generator
    if "CMAKE_MAKE_PROGRAM" in os.environ:
        command += "-D%s" % os.environ["CMAKE_MAKE_PROGRAM"]
    run(command)
    run('cmake --build . --config Release')

if __name__ == '__main__':
    main()
