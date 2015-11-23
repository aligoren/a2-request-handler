#!/usr/bin/python3

import time
import re
import sys

p = re.compile(r'(.*?) (.*?) \[(.*?)\] \"(.*?)\" (.*?) (.*?) (.*?) \"(.*?)\"')
ret = ''
start_do = ''
req_date = ''
req_parse = ''
req_status = ''
req_path = ''
req_user_agent = ''

def rtfile(file):
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    access_log_file = open("/var/log/apache2/access.log","r")
    access_loglines = rtfile(access_log_file)
    print("Monitoring...\n")
    for line in access_loglines:
        outstr = line
        ret = re.search(p, outstr)
        start_do = ret.group(1)
        req_date = ret.group(3)
        req_parse = ret.group(4)
        req_status = ret.group(5)
        if ret.group(7) != '"-"':
            req_path = ret.group(7)
        else:
            req_path = '"/"'
        req_user_agent = ret.group(8)
        print("IP/Domain: {0}\nRequest Date: {1}\nRequest Method: {2} \
        \nRequest Status: {3}\nPath: {4}\nUser Agent: {5}".format(start_do, req_date, req_parse, req_status, req_path, req_user_agent))
        print("-".strip(' ')*45, end='\n\n')
