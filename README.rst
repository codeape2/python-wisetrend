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

The ``wisetrend.py`` docstring has a complete example.


Example command line usage
==========================

``wisetrend.py`` can also be invoked on the command line for testing.

::

    [~/wisetrend]
    $ python2.7 wisetrend.py --help
    Usage: 
    1. wisetrend.py submit --key secretkey --inputurl inputurl
    2. wisetrend.py getstatus --joburl joburl

    Options:
      -h, --help           show this help message and exit
      --key=KEY            
      --inputurl=INPUTURL  
      --joburl=JOBURL      
    [~/wisetrend]
    $ python2.7 wisetrend.py submit --key your-secret-key --inputurl http://url.to/the/document
    Job URL: http://api.ocr-it.com/ocr/v2/getStatus/...
    [~/wisetrend]
    $ python2.7 wisetrend.py getstatus --joburl http://api.ocr-it.com/ocr/v2/getStatus/...
    Status: Finished
    PDF http://api.ocr-it.com/ocr/v2/download/....PDF
    TXT http://api.ocr-it.com/ocr/v2/download/....TXT
