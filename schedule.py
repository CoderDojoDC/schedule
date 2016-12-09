#!/usr/bin/env python3
from datetime import date, timedelta
import holidays

ch = holidays.UnitedStates()
ch.update({ "2017-02-05": "Super Bowl Sunday", "2017-02-14": "Valentine's Day",
            "2017-04-16": "Easter Sunday", "2017-05-14": "Mother's Day",
            "2017-06-18": "Father's Day", "2017-07-02": "4th of July Weekend",
            "2017-09-22": "Rosh Hashanah (begins at sundown)", "2017-11-26":
            "Thanksgiving Weekend"})

def secondsundays(d):
    while d.year == 2017:
        yield d
        d += timedelta(days = 14)

start1 = date(2017, 1, 8)
start2 = date(2017, 1, 15)
schedule1 = [d.strftime('%Y-%m-%d') for d in secondsundays(start1)]
schedule2 = [d.strftime('%Y-%m-%d') for d in secondsundays(start2)]

for s in (schedule1, schedule2):
    heading = "\nStart on {0}".format(s[0])
    print("\n".join([heading, "=" * (len(heading)-1)]))
    for d in s:
        if d in ch:
            print(d, ch.get(d))
        else:
            print(d)
