from package import *

def getStudentIDbyUUID(uuid):
    docs = tdb.collection(u'DeviceConnector').where(u'deviceID', u'==', uuid).stream()
    docs = list(docs)
    if(len(docs)>0):
        return(docs[0].to_dict())
    return None