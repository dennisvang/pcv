About PCV
---------

PCV creates a printable resume (CV) in HTML format, based on data stored in JSON.

YAML would be easier to write, but we don't want the extra dependency required (e.g. PyYAML).

Instead of using a Python package to handle PDF creation (e.g. ReportLab or PyQT), the HTML output includes a print style, so we can print to PDF using the browser.

Disclaimer
----------

This project is intended for personal use, so it is not production-ready.

There are many similar projects out there that are much more complete.
