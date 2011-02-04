============
wisetrend.py
============

``wisetrend.py`` is a module for using `WiseTREND OCR Cloud <http://www.wisetrend.com/wisetrend_ocr_cloud.shtml>`_.

Getting started
===============

* Sign up for the Web API from the WiseTREND OCR Cloud web page and get your API key.
* Upload a document to somewhere the WiseTREND service can access it
* Use the ``submit`` function to submit a OCR job
* Use the ``getstatus`` function to check the status of a submitted job

Example commandline usage
=========================

::

    [~/wisetrend]
    $ python2.7 wisetrend.py submit --key your-secret-key --inputurl http://url.to/the/document
    Job URL: http://api.ocr-it.com/ocr/v2/getStatus/...
    [~/wisetrend]
    $ python2.7 wisetrend.py getstatus --joburl http://api.ocr-it.com/ocr/v2/getStatus/...
    Status: Finished
    PDF http://api.ocr-it.com/ocr/v2/download/....PDF
    TXT http://api.ocr-it.com/ocr/v2/download/....TXT
