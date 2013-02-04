'''
Created on Feb 3, 2013

@author: justin

script for translating IB java code
'''

import os
import re

basePath = "../IBJts/java"


def translateFile(path, fileName):
    """
    path = directory path
    fileName = xxxx.java file
    
    will invoke j2py to perform the translation
    """
    
    source = fileName
    target = re.sub("\.java$", ".py", fileName)
    
    source = os.path.join(path, source)
    target = os.path.join(path, target)
    
    print "translating %s" % target
    os.system("j2py %s %s" % (source, target))
    
def translate(basePath):
    """
    basePath = base directory
    used to translate all java files
    """
    
    walkList = os.walk(basePath)
    
    for walkObject in walkList:
        path, folders, files = walkObject
        
        files = [f for f in files if re.search("\.java$", f)]
        for f in files:
            translateFile(path, f)

if __name__ == "__main__":
    translate(basePath)
