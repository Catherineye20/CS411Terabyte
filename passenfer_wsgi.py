import sys, os

INTERP = "/home/cs411terabyte/python_test/bin/python"
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

from python_test import app as application
