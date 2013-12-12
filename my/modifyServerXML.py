#! /usr/bin/env python
# -*- coding: utf-8 -*-
# FileName is modifyServerXML.py

"""
modify "server.xml",  replace with new host, new username, new password
ouput in new file, will not change the old file
"""

import time
import re
import sys
import xml.etree.cElementTree as ET

#key=oldHost, value=(newHost, newUserName, newPassword)
DATA = {
    "192.168.1.1":("192.168.1.2", "lijinnan", "1234"),
}


def currentTimeMillis():
    return int(round(time.time() * 1000))

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) != 2:
        print "please enter file path"
        print "usage:"
        print " python modifyServerXML.py [filePath]"
        print " e.g. python modifyServerXML.py /usr/local/tomcat6-8083/conf/server.xml"
    else:

        filePath = argv[1]
        parser = ET.XMLParser(encoding="utf-8")
        tree = ET.parse(filePath, parser=parser)

        for ctx in tree.iter("Context"):

            for resource in ctx.iter("Resource"):
                jdbcUrlLabel = "jdbcUrl"
                jdbcUrl = resource.get("jdbcUrl") 
                if not jdbcUrl:
                    jdbcUrlLabel = "url"
                    jdbcUrl = resource.get(jdbcUrlLabel)
                
                userLabel = "user"
                user = resource.get(userLabel)
                if not user:
                    userLabel = "username"
                    user = resource.get(userLabel)

                pwd = resource.get("password")

                m = re.match(r"\w+:\w+://([^:]+):(\d+)/([^?]+)\?", jdbcUrl)
                host = m.group(1)
                port = m.group(2)
                database = m.group(3) 
                
                #print database + "\t-h" + host + "\t-P" + port + "\t-u" + user + "\t-p" + pwd
                
                #modify
                if host not in DATA:
                    continue
                jdbcUrl = jdbcUrl.replace(host, DATA[host][0])
                resource.set(jdbcUrlLabel, jdbcUrl)
                resource.set(userLabel, DATA[host][1])
                resource.set("password", DATA[host][2])

        newFilePath = filePath + str(currentTimeMillis()) 
        tree.write(newFilePath)
        print "success, check the new file:\n" + newFilePath
