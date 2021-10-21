import xml.etree.ElementTree as ET
import csv
import os
import fnmatch


def XML_stripper():
    #Flatten XML to TEXT
        for child in root:
            mainlevel = child.tag
            xmltocsv = ''
            for elem in root.iter():
                if elem.tag == root.tag:
                    continue
                if elem.tag == mainlevel:
                    xmltocsv = xmltocsv + '\n'
                xmltocsv = xmltocsv + str(elem.tag).rstrip() + str(elem.attrib).rstrip() + ';' + str(elem.text).rstrip() + ';'
        return xmltocsv

def DATA_listgenerator(xmltocsv):
    DataList = []
    multiElemList = []
    ElementListSearch = [
        'url{}', 
        'org_study_id{}', 
        'nct_id{}', 
        'brief_title{}', 
        'agency{}', 
        'overall_status{}', 
        'last_known_status{}', 
        'start_date{}', 
        """primary_completion_date{'type': 'Actual'}""",
        'phase{}',
        'study_type{}',
        'condition{}',
        'intervention_type{}',
        'intervention_name{}',
        """completion_date{'type': 'Anticipated'}""",
        ]
    ##'brief_summary{}'
    MultiVarElemList = [
        'keyword{}',
        'mesh_term{}'
        ]
    
    xmltocsv = xmltocsv
##    print(xmltocsv)
    xmlClean = xmltocsv.replace(';;',';')
##    print(xmlClean)
    xmlElementList = xmlClean.split(';')
##    print(xmlElementList)
    
    
    for element in range(len(ElementListSearch)):
        if (ElementListSearch[element] in xmlElementList):
            xmlIndex = xmlElementList.index(ElementListSearch[element])
            xmlElement = xmlElementList[xmlIndex+1]
            DataList.append(xmlElement)
        else:
            DataList.append('null')

            
    # xmlSummaryIndex = xmlElementList.index('brief_summary{}')
    # xmlSummaryElem = xmlElementList[xmlSummaryIndex+2]
    # DataList.append(xmlSummaryElem)

    for element in range(len(MultiVarElemList)):
        if (MultiVarElemList[element] in xmlElementList):
            xmlIndices = [i for i, x in enumerate(xmlElementList) if x == MultiVarElemList[element]]
            ##print(xmlIndices)
            multiElemList = []
            for index in range(len(xmlIndices)):
                xmlElement = xmlElementList[xmlIndices[index]+1]
                multiElemList.append(xmlElement)
            DataList.append(multiElemList)
        else:
            DataList.append('null')
    #print(DataList)
    return(DataList)


        
    
def NCT_file_getter():
    fileList = []
    for path,dirs,files in os.walk(r'C:\Users\Jordon\Desktop\master dataset\AllPublicXML\NCT0000xxxx'):
        for file in files:
            if fnmatch.fnmatch(file,'*.xml'):
                fullname = os.path.join(path,file)
                fileList.append(fullname)
    ##print(fileList)
    print("FILE LIST COMPLETE " + str(len(fileList)) + " items")

    return fileList

def GET_one_file(fileList, number):
    fileList = fileList
    iteration = number
    currentFile = fileList[iteration]
    #print(currentFile)
    return currentFile

def XML_stripper2(currentFile):
    tree = ET.parse(currentFile)
    root = tree.getroot()
    tag = root.tag
    att = root.attrib

    for child in root:
        mainlevel = child.tag
        xmltocsv = ''
        for elem in root.iter():
            if elem.tag == root.tag:
                continue
            if elem.tag == mainlevel:
                xmltocsv = xmltocsv + '\n'
            xmltocsv = xmltocsv + str(elem.tag).rstrip() + str(elem.attrib).rstrip() + ';' + str(elem.text).rstrip() + ';'
    print (xmltocsv)
    return xmltocsv

def CSV_file_writer(masterList):
    masterList = masterList
    file = open(r'C:\Users\Jordon\Desktop\csv project\python script\newcsv.csv', 'w+', newline= '')
    with file:
        write = csv.writer(file)
        write.writerows(masterList)
    


# fileList = NCT_file_getter()
# currentFile = GET_one_file(fileList,0)
# xmltocsv = XML_stripper2(currentFile)
# DATA_listgenerator(xmltocsv)



def testThreading(number):
    currentFile = GET_one_file(fileList,number)
    xmltocsv = XML_stripper2(currentFile)
    DataList = DATA_listgenerator(xmltocsv)
    masterList.append(DataList)

from multiprocessing.dummy import Pool as ThreadPool
from timeit import default_timer as timer
masterList = []
fileList = []

def masterLoop():
    start = timer()
    pool = ThreadPool(4)
    global masterList
    global fileList
    masterList = []
    # number = 0
    fileList = NCT_file_getter()
    # for i in range(len(fileList)):
    #     currentFile = GET_one_file(fileList,number)
    #     xmltocsv = XML_stripper2(currentFile)
    #     DataList = DATA_listgenerator(xmltocsv)
    #     masterList.append(DataList)
    #     number += 1
    results = pool.map(testThreading, range(len(fileList)))

    CSV_file_writer(masterList)
    end = timer()
    print ("DONE")
    print (str(round((end - start)/60,1)) + " minutes elapsed")
masterLoop()

