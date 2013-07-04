"""Generate or update cv.pdf

* Check if rst2pdf exists
* Run rst2pdf with options. If successful, print message and exit
"""
import sys
import subprocess

try:
    version = subprocess.check_output(["rst2pdf", "--version"])
except OSError as e:
    print ("Could not execute rst2pdf. Please check if rst2pdf is "
           "installed and available in the system PATH.\n{0}".format(str(e)))
    sys.exit()
else:
    print "Found rst2pdf version {0}".format(version.strip())

command = ["rst2pdf", "--config=rst2pdfconfig", "--raw-html", "cv.rst"]

try:
    print "Generating PDF..."
    subprocess.call(command)
except subprocess.CalledProcessError as e:
    print "Command:\n{0}\n".format(e.cmd)
    print "Error:\n{0}\n".format(e.output)
else:
    print "Finished!"
