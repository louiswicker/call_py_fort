#!/usr/bin/env python

import sys
import os
import glob
import string
from optparse import OptionParser
subfolders = ['./']
# append path to the folder
sys.path.extend(subfolders)

parser = OptionParser()
parser.add_option("-f","--file",dest="file",type="string", help = "fortran file to be compiled - if not supplied, all fortran files are!")
parser.add_option("-a","--all",dest="all",default=False,help = "Boolean flag to compile all files (default=False)", action="store_true")
parser.add_option("-c","--compiler",dest="compiler",type="string",default=None,help = "compiler to use with f2py3")

(options, args) = parser.parse_args()

if options.all:
    fortran_files = glob.glob("*.f")
    fortran_files = fortran_files + glob.glob("*.f77")
    fortran_files = fortran_files + glob.glob("*.f90")

if options.file != None:
    prefix = options.file.split(".")[0]
    fortran_files = glob.glob(prefix + ".f90")
    fortran_files = fortran_files + glob.glob(prefix+".f")

if options.compiler == None:
    compiler = "gfortran"
else:
    compiler = options.compiler

includeDirs  = "-I/usr/local/include"
libraryDirs  = "-L/usr/local/lib"
systemLib    = "-L/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/lib"
libraryRPath = "-Wl,-rpath,/Users/Louis.Wicker/miniconda3/lib"

# go through all the folders, make the python module and run the program
#   f2py_module_list = []
#   run_module_list = []
#
# Get all the fortran files
#
objects = ''

for item in fortran_files:
    prefix = item.split(".")[0]
    print("\n=====================================================\n")
    print("  Attempting to compile file: %s " % item)
    print("\n=====================================================")
    ret = os.system("gfortran -O2 %s -c %s" % (includeDirs, item))
    if ret == 0:
        print("\n=====================================================\n")
        print("   Successfully created file: %s.o " % prefix)
        print("\n======================================================")

    objects = ("%s %s.o" % (objects, prefix))

ret = os.system("gfortran -o run.exe %s %s %s %s -lcallpy %s" % (objects, libraryRPath, includeDirs, libraryDirs, systemLib))
if ret == 0:
    print("\n=====================================================\n")
    print("   Successfully created executable file: %s " % ("run.exe"))
    print("\n======================================================")
