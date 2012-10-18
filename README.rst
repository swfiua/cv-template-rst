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
:literal:`rst2pdf` is available in the system PATH, do ::

    rst2pdf --config=rst2pdfconfig cv.rst
    
This should generate :literal:`cv.pdf`.
