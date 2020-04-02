"""
time_helpers - some utilities to handle time more user-friendly

2020-0329 PP new
"""
import time


# 2019-0801 added from @Jumpero
# https://forum.micropython.org/viewtopic.php?f=2&t=4034
#   Micropython esp8266
#   This code returns the Central European Time (CET) including daylight saving
#   Winter (CET) is UTC+1H Summer (CEST) is UTC+2H
#   Changes happen last Sundays of March (CEST) and October (CET) at 01:00 UTC
#   Ref. formulas : http://www.webexhibits.org/daylightsaving/i.html
#        Since 1996, valid through 2099
def cettime():
    """cettime() - returns localtime in Central European Time (CET)
       including daylight saving. """
    year = time.localtime()[0]       # get current year
    # Time of March change to CEST
    # HHMarch = time.mktime((year, 3, (31-(int(5*year/4+4))%7),1,0,0,0,0,0))
    HHMarch = time.mktime((year, 3, (29-(int(5*year/4+4))%7),1,0,0,0,0,0))
    HHOctober = time.mktime((year, 10, (31-(int(5*year/4+1))%7),1,0,0,0,0,0)) #Time of October change to CET
    now = time.time()
    if now < HHMarch:               # we are before last sunday of march
        cet = time.localtime(now+3600)  # CET:  UTC+1H
    elif now < HHOctober:           # we are before last sunday of october
        cet = time.localtime(now+7200)  # CEST: UTC+2H
    else:                            # we are after last sunday of october
        cet = time.localtime(now+3600)  # CET:  UTC+1H
    return(cet)


def timerecord():
    """ timerecord(): returns user-friendly localtime for CES)T timezone.
        example: '2019-08-03, 17:09:26' """
    t = cettime()
    now_string = "{:04d}-{:02d}-{:02d},{:02d}:{:02d}:{:02d}"
    now = now_string.format(t[0], t[1], t[2], t[3], t[4], t[5])
    return now
