#!/usr/bin/env python
#_*_encoding:utf-8_*_
import ConfigParser
conf=ConfigParser.ConfigParser()
conf.read('conf')
sections=conf.sections()
print 'sections:',sections
options=conf.options('sec_a')
print 'options:',options
kvs=conf.items('sec_a')
print 'sec_a:',kvs
str_val = conf.get('sec_a','a_key1')
int_val=conf.getint('sec_a','a_key2')
print str_val
print int_val



