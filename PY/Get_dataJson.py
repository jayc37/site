import requests 
from datetime import datetime
import re
from analize import analize
from formatdatatable import format
class sendRequest:
    def __init__(self,URL):
        self.url = URL
        self._head = {}
        self._content = {}
        self.dataSet = {}
        self.index = []
        self.Makerequest()


    def Makerequest(self):
        try:
            URL = self.url
            rq = requests.get(url = URL, params = None)
            var = self.Variable(rq.json())
            if var:
                _h = self._head
                _c = self._content
                index,dataSet = analize(_c)
                data = format(index,dataSet)
                self.dataSet = data
            else:
                writelog("GET Request failed !")
        except Exception as e:
            writelog(str(e))

    def Variable(self,dj):
        try:
            _h = self._head
            _c = self._content
            t = dj
            _h['signal'] = t['success']
            if t['success']:
                _h['trace'] = t['timestamp']
                _h['location'] = t['base']
                _h['Datatime'] = t['date']
                _c['rates'] = t['rates']
                return True
        except Exception as e:
            writelog(str(e))


def writelog(string):
    dt = get_datetime()
    with open('tempProlog', 'a', encoding="utf-8") as f:
        f.write(dt + " : " + string)
        logging.error(dt + " : " + string)

def get_datetime():
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

