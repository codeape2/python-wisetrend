"""
Use WiseTREND OCR cloud from Python.

Example:

import wisetrend
import time

joburl = wisetrend.submit("API-KEY", "http://url/to/the/document")
while True:
    time.sleep(5)
    status, downloads = wisetrend.getstatus(joburl)
    print status
    if status == "Finished":
        for outputtype, url in downloads.iteritems():
            print outputtype, url
        break

"""
import urllib2
from xml.etree import ElementTree as E

class SubmitError(Exception):
    pass

URL = "http://svc.webservius.com/v1/wisetrend/wiseocr/submit?wsvKey="

def submit(key, inputurl):
    """Returns the job url"""
    job_element = E.Element("Job")
    E.SubElement(job_element, "InputURL").text = inputurl
    
    request = urllib2.Request(URL + key, data=E.tostring(job_element), headers={
        "Content-Type": "text/xml"
        })
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        raise SubmitError(e.read())
    else:
        jobstatus = E.fromstring(response.read())
        if jobstatus.find("Status").text == "Submitted":
            return jobstatus.find("JobURL").text
        else:
            raise SubmitError(E.tostring(jobstatus))

def getstatus(joburl):
    """Returns a tuple (Status, {"OutputType": downloaduri})
    
    If the status is not Finished, returns (Status, {})
    """
    jobstatus = E.fromstring(urllib2.urlopen(joburl).read())
    if jobstatus.find("Status").text == "Finished":
        return "Finished", dict((file_element.find("OutputType").text, file_element.find("Uri").text) 
                                for file_element in jobstatus.findall("Download/File"))
    else:
        return jobstatus.find("Status").text, {}

if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser(usage="\n1. %prog submit --key secretkey --inputurl inputurl\n2. %prog getstatus --joburl joburl")
    parser.add_option("--key")
    parser.add_option("--inputurl")
    parser.add_option("--joburl")
    opts, args = parser.parse_args()
    if len(args) != 1:
        parser.error("Specify submit or getstatus")
    if args[0] == "submit":
        joburl = submit(opts.key, opts.inputurl)
        print "Job URL:", joburl
    if args[0] == "getstatus":
        status, downloads = getstatus(opts.joburl)
        print "Status:", status
        for outputtype, url in downloads.iteritems():
            print outputtype, url
