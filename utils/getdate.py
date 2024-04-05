import datetime

def getdatesystem():
    actually_date = datetime.datetime.now()
    return actually_date.date()
