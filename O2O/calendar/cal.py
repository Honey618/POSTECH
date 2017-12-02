from dateutil import parser
from datetime import datetime



def dcal(s):
    return parser.parse(s).strftime('%Y/%m/%d')    


#register()
