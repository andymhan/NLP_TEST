import sys
import os
import time

__author__ = 'andymhan'
# Output example: [=======   ] 75%
# width defines bar width
# percent defines current percentage

def progress(width, percent):
    linestr = "\r%s %d%%\r"%(('%%-%ds' % width) % (int(width * percent/100) * '='), percent)
    os.write(1,bytes(linestr, 'UTF-8'))
    sys.stdout.flush()
    if percent >= 100:
        print
        sys.stdout.flush()


# Simulate doing something ...
# for i in range(100):
#     progress(100, (i + 1))
#     time.sleep(0.1) # Slow it down for demo


def hamming_distance(hash1, hash2):
    hashbits = 64
    x = (int(hash1) ^ int(hash2)) & ((1 << hashbits) - 1)
    tot = 0
    while x:
        tot += 1
        x &= x-1
    return tot

hash1 = 15907347255682217840
hash2 = 15907347667999076208
t = hamming_distance(hash1,hash2)
print(t)

class data2db_proc():
    def __init__(self):
        self.data_eventdb_map = {"strEventID":'Res.Event.uiEventID',
            "strSendTime":'Res.Event.uiSendTime',
            "strCity":'Res.Event.strCity',
            "strContentTime":'Res.Event.strContentTime',
            "strContentCity": 'Res.Event.strContentCity',
            "uiHot":'Res.Event.uiHot',
            "uiEvilScore": 'Res.Event.uiEvilScore',
            "strEventInfo": 'Res.Event.strEventInfo',
            "struiGuaidianTime":'Res.Event.uiGuaidianTime',
            "strAcceleratedSpeed":'Res.Event.uiAcceleratedSpeed',
            "strStep1Time":'Res.Event.uiStep1Time',
            "strStep2Time":'Res.Event.uiStep2Time',
            "strStep3Time":'Res.Event.uiStep3Time',
            "strStep4Time":'Res.Event.uiStep4Time',
            "uiMsgNum":'Res.Msg.uiMsgNum'}

        self.data_msgdb_map = {"strEventID":'Res.Event.uiEventID',
            "uiAppID":'Comm.uiAppID',
            "uiSpecialClass":'Comm.uiSpecialClass',
            "uiOtherClass":'Comm.uiOtherClass',
            "ullUin":'Comm.ullUin',
            "uiSendIP":'Comm.uiSendIP',
            "strSendTime":'Comm.uiSendTime',
            "strContentID":'ID.strContentID',
            "strTitle":'Content.strTitle',
            "strContent":'Content.strContent',
            "uiImgNum":'Content.uiImgNum',
            "uiVideoNum":'Content.uiVideoNum',
            "strContentUrl":'Content.strContentUrl',
            "strBuInfo":'Content.strBuInfo',
            "strCountry":'Content.strCountry',
            "strProvince":'Content.strProvince',
            "strCity":'Content.strCity',
            "uiHotLevel":'Content.uiHotLevel',
            "uiContentStyle":'Content.uiContentStyle',
            "ullTtitleSimHash":'Content.ullTtitleSimHash',
            "ullContentSimHash":'Content.ullContentSimHash',
            "strSplitWords":'Content.strSplitWords',
            "uiEvilScore":'Res.Event.uiEvilScore'}

        self.evt_data = []
        self.msg_data = []

        self.evt_db_item  = self.data_eventdb_map.keys()
        self.msg_db_item =  self.data_msgdb_map.keys()

        self.evt_db_item_str = ','.join(self.evt_db_item)

t = data2db_proc()
print(t.evt_db_item_str)
print(type(t.evt_db_item_str))

import xlrd
import  datetime
data = xlrd.open_workbook('f://tencent//test.xls')
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
row = table.row_values(0)
print(row[0])
type(row[0])
if isinstance(row[0],basestring):
    print(row[0])
    commit_date = datetime.datetime.strptime(row[0].strip(),"%Y/%m/%d")
else:
    commit_date = xlrd.xldate.xldate_as_datetime(row[0],0)
    print(commit_date)
    commit_date_str = commit_date.strftime("%Y-%m-%d")
    print(commit_date_str)