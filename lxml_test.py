import xml.etree.ElementTree as ET
import csv
import os
import fnmatch

from lxml import etree
from timeit import default_timer as timer

ElementListSearch = [
        'url', 
        'org_study_id', 
        'nct_id', 
        'brief_title', 
        'agency', 
        'overall_status', 
        'last_known_status', 
        'start_date', 
        'phase',
        'study_type',
        'condition',
        'intervention_type',
        'intervention_name',
        ]

MultiVarElemList = [
        'keyword',
        'mesh_term'
        ]

        
def NCT_file_getter():
    fileList = []
    for path,dirs,files in os.walk(r'C:\Users\Jordon\Desktop\master dataset\AllPublicXML'):
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
    # print(currentFile)
    return currentFile

def XML_stripper2(currentFile):
    tree = ET.parse(currentFile)
    root = tree.getroot()
    tag = root.tag
    att = root.attrib

    dataXML = []
    dataKeyword = []

    url = []
    org_study_id = []
    nct_id = []
    brief_title = []
    agency = []
    overall_status = []
    last_known_status = []
    start_date = []
    phase = []
    study_type = []
    condition = []
    intervention_type = []
    intervention_name = []

    for elem in root.iter():
        if elem.tag in MultiVarElemList:
            newData = str(elem.text).rstrip()
            dataKeyword.append(newData)
        if elem.tag == ElementListSearch[0]:
            url.append(elem.text.rstrip())
        if elem.tag == ElementListSearch[1]:
            org_study_id.append(elem.text.rstrip())
        if elem.tag == ElementListSearch[2]:
            nct_id.append(elem.text.rstrip())
        if elem.tag == ElementListSearch[3]:
            brief_title.append(elem.text.rstrip())
        if elem.tag == ElementListSearch[4]:
            agency.append(elem.text.rstrip())
        if elem.tag == ElementListSearch[5]:
            overall_status.append(elem.text.rstrip())
        if elem.tag == ElementListSearch[6]:
            last_known_status.append(elem.text.rstrip())
        if elem.tag == ElementListSearch[7]:
            start_date.append(elem.text.rstrip())
        if elem.tag == ElementListSearch[8]:
            phase.append(elem.text.rstrip())
        if elem.tag == ElementListSearch[9]:
            study_type.append(elem.text.rstrip())
        if elem.tag == ElementListSearch[10]:
            condition.append(elem.text.rstrip())
        if elem.tag == ElementListSearch[11]:
            intervention_type.append(elem.text.rstrip())
        if elem.tag == ElementListSearch[12]:
            intervention_name.append(elem.text.rstrip())

    url = list(dict.fromkeys(url))
    org_study_id = list(dict.fromkeys(org_study_id))
    nct_id = list(dict.fromkeys(nct_id))
    brief_title = list(dict.fromkeys(brief_title))
    agency = list(dict.fromkeys(agency))
    overall_status = list(dict.fromkeys(overall_status))
    last_known_status = list(dict.fromkeys(last_known_status))
    start_date = list(dict.fromkeys(start_date))

    condition = list(dict.fromkeys(condition))
    intervention_type = list(dict.fromkeys(intervention_type))
    intervention_name = list(dict.fromkeys(intervention_name))
    phase = list(dict.fromkeys(phase))
    study_type = list(dict.fromkeys(study_type))
    dataKeyword = list(dict.fromkeys(dataKeyword))

    if len(url) == 0:
        url = 'null'
        dataXML.append(url)
    elif len(url) == 1:
        dataXML.append(url[0])
    elif len(url) > 1:
        dataXML.append(url)

    if len(org_study_id) == 0:
        org_study_id = 'null'
        dataXML.append(org_study_id)
    elif len(org_study_id) == 1:
        dataXML.append(org_study_id[0])
    elif len(org_study_id) > 1:
        dataXML.append(org_study_id)

    if len(nct_id) == 0:
        nct_id = 'null'
        dataXML.append(nct_id)
    elif len(nct_id) == 1:
        dataXML.append(nct_id[0])
    elif len(nct_id) > 1:
        dataXML.append(nct_id)

    if len(brief_title) == 0:
        brief_title = 'null'
        dataXML.append(brief_title)
    elif len(brief_title) == 1:
        dataXML.append(brief_title[0])
    elif len(brief_title) > 1:
        dataXML.append(brief_title)

    if len(agency) == 0:
        agency = 'null'
        dataXML.append(agency)
    elif len(agency) == 1:
        dataXML.append(agency[0])
    elif len(agency) > 1:
        dataXML.append(agency)

    if len(overall_status) == 0:
        overall_status = 'null'
        dataXML.append(overall_status)
    elif len(overall_status) == 1:
        dataXML.append(overall_status[0])
    elif len(overall_status) > 1:
        dataXML.append(overall_status)

    if len(last_known_status) == 0:
        last_known_status = 'null'
        dataXML.append(last_known_status)
    elif len(last_known_status) == 1:
        dataXML.append(last_known_status[0])
    elif len(last_known_status) > 1:
        dataXML.append(last_known_status)

    if len(start_date) == 0:
        start_date = 'null'
        dataXML.append(start_date)
    elif len(start_date) == 1:
        dataXML.append(start_date[0])
    elif len(start_date) > 1:
        dataXML.append(start_date)

    if len(phase) == 0:
        phase = 'null'
        dataXML.append(phase)
    elif len(phase) == 1:
        dataXML.append(phase[0])
    elif len(phase) > 1:
        dataXML.append(phase)

    if len(study_type) == 0:
        study_type = 'null'
        dataXML.append(study_type)
    elif len(study_type) == 1:
        dataXML.append(study_type[0])
    elif len(study_type) > 1:
        dataXML.append(study_type)

    if len(condition) == 0:
        condition = 'null'
        dataXML.append(condition)
    elif len(condition) == 1:
        dataXML.append(condition[0])
    elif len(condition) > 1:
        dataXML.append(condition)

    if len(intervention_type) == 0:
        intervention_type = 'null'
        dataXML.append(intervention_type)
    elif len(intervention_type) == 1:
        dataXML.append(intervention_type[0])
    elif len(intervention_type) > 1:
        dataXML.append(intervention_type)

    if len(intervention_name) == 0:
        intervention_name = 'null'
        dataXML.append(intervention_name)
    elif len(intervention_name) == 1:
        dataXML.append(intervention_name[0])
    elif len(intervention_name) > 1:
        dataXML.append(intervention_name)

    dataXML.append(dataKeyword)

    return dataXML
    
def CSV_file_writer(masterList):
    masterList = masterList
    file = open(r'C:\Users\Jordon\Desktop\csv project\python script\newcsv.csv', 'w+', newline= '', encoding='utf-8')
    with file:
        write = csv.writer(file)
        write.writerows(masterList)



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
    # results = pool.map(testThreading, range(1))

    CSV_file_writer(masterList)
    end = timer()
    print ("DONE")
    print (str(round((end - start)/60,1)) + " minutes elapsed")



def testThreading(number):
    currentFile = GET_one_file(fileList,number)
    # currentFile = 'test2.xml'
    DataList = XML_stripper2(currentFile)
    masterList.append(DataList)



masterLoop()
