Readme
======
This is the template I used for generating my CV. 

The CV itself is written in plain text using the reStructuredText(ReST) syntax.

Requirements
------------
* Python - http://python.org/download/
* rst2pdf - http://rst2pdf.ralsina.com.ar/
  use package manager or ``pip install rst2pdf`` or ``easy_install rst2pdf``
  
How to generate the PDF
-----------------------
Modify the included :literal:`rst2pdfconfig` if necessary. Assuming 
:literal:`rst2pdf` is available in the system PATH, run ::

   python updatecv.py

Alternatively, run rst2pdf directly ::

   rst2pdf --config=rst2pdfconfig cv.rst

Either of these steps should generate :literal:`cv.pdf`.

Change log
----------
0.2
...
* Styles moved to the "styles" subdirectory.
* The updatecv.py script can be used to generate or update the CV in PDF format.

0.1
...
* New style using Open Sans font.
* Fonts now included in the repo.
