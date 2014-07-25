Readme
======
CV template in reStructuredText (rst). Generate PDF and optionally DOCX, ODT or 
Plain text formats (requires `Pandoc`_).

My CV is included as an example. 


Requirements
------------

#. Either:

    * (Recommended) Create a Python 2 virtualenv::

         mkvirtualenv -p /usr/bin/python2 cv

    * Install rst2pdf::
    
         pip install rst2pdf
     
    [OR]

    * Install Python and `rst2pdf <http://rst2pdf.ralsina.com.ar>`_.

#. (Optional) For ``docx`` output, install `Pandoc`_.
    
 
How to generate PDF
-------------------
Modify the included :literal:`rst2pdfconfig` if necessary. 

Assuming you are in the virtualenv created earlier (i.e., ``cv``) or :literal:`rst2pdf` is 
installed and available in the system PATH, run ::

   python updatecv.py

You can also call rst2pdf directly::

   rst2pdf --config=rst2pdfconfig cv.rst

Either of these steps should generate :literal:`cv.pdf`.

Modify styles
.............
You can customize styles in the generated PDF using a stylesheet. See ``styles/custom.style`` 
for an example. To list all styles that rst2pdf supports, use the command::

    rst2pdf --print-stylesheet


DOCX and other formats
----------------------

DOCX::

    pandoc -f rst -t docx cv.rst -o cv.docx

ODT::

    pandoc -f rst -t odt cv.rst -o cv.odt

Plain text (no hyperlinks)::

    pandoc -f rst -t plain cv.rst -o cv.txt


Change log
----------
0.3
...
* Custom style example.
* Add notes on using Pandoc for other formats.

0.2
...
* Styles moved to the "styles" subdirectory.
* The updatecv.py script can be used to generate or update the CV in PDF format.

0.1
...
* New style using Open Sans font.
* Fonts now included in the repo.


.. links

.. _Pandoc: http://johnmacfarlane.net/pandoc