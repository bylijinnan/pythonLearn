#! /usr/bin/env python
# -*- coding: utf-8 -*-
# FileName is serverXMLParser.py

# parse database info from tomcat's server.xml
# output format:
#   database    -hhost  -Pport  -uuser  -ppassword

import re
import sys
import xml.etree.cElementTree as ET

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) != 2:
        print "please enter file path"
        print "usage:"
        print " python serverXMLParser.py [filePath]"
        print " e.g. python serverXMLParser.py /usr/local/tomcat6-8083/conf/server.xml"
    else:

        filePath = argv[1]
        parser = ET.XMLParser(encoding="utf-8")
        tree = ET.ElementTree().parse(filePath, parser=parser)

        for ctx in tree.iter("Context"):
            print "#" + ctx.get("path")

            for resource in ctx.iter("Resource"):
                jdbcUrl = resource.get("jdbcUrl") if resource.get("jdbcUrl") else resource.get("url")
                m = re.match(r"\w+:\w+://([^:]+):(\d+)/([^?]+)\?", jdbcUrl)
                host = m.group(1)
                port = m.group(2)
                database = m.group(3) 
                user = resource.get("user") if resource.get("user") else resource.get("username")
                pwd = resource.get("password")
                
                print database + "\t-h" + host + "\t-P" + port + "\t-u" + user + "\t-p" + pwd

            print "\n"


"""
example:
>>>input file

server.xml:

<?xml version='1.0' encoding='utf-8'?>

<Server>

<Context path="/ljnngcdjx" docBase="/usr/local/ljngame/admin-htdocs/LJNNGCDJXWeb" debug="0" reloadable="false" crossContext="true">
        <Resource name="jdbc/ljnngowpp" auth="Container"
                        type="com.mchange.v2.c3p0.ComboPooledDataSource" maxPoolSize="150"
                        minPoolSize="1" initialPoolSize="5" acquireIncrement="2"
                        idleConnectionTestPeriod="60" maxIdleTime="1200"
                        driverClass="com.mysql.jdbc.Driver" user="root"
                        password="password"
                        jdbcUrl="jdbc:mysql://192.168.10.10:3306/ljnngowpp?useUnicode=true&amp;characterEncoding=utf8"
                        factory="org.apache.naming.factory.BeanFactory"/>
        <Resource name="jdbc/ljngame_dnf" auth="Container"
			type="com.mchange.v2.c3p0.ComboPooledDataSource" maxPoolSize="150"
                        minPoolSize="1" initialPoolSize="5" acquireIncrement="2"
                        idleConnectionTestPeriod="60" maxIdleTime="1200"
                        driverClass="com.mysql.jdbc.Driver" user="root"
                        password="password"
                        jdbcUrl="jdbc:mysql://192.168.10.10:3306/ljngame_dnf?useUnicode=true&amp;characterEncoding=utf8"
                         factory="org.apache.naming.factory.BeanFactory"/>
</Context>

</Server>

<<<output:

#/ljnngcdjx
ljnngowpp       -h192.168.10.10    -P3306  -uroot  -ppassword
ljngame_dnf     -h192.168.10.10    -P3306  -uroot  -ppassword

"""
