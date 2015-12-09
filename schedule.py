#!/usr/bin/env python3
from datetime import date, timedelta
import holidays

ch = holidays.UnitedStates()
ch.update({ "2016-02-07": "Super Bowl Sunday", "2016-02-14": "Valentine's Day",
            "2016-03-27": "Easter Sunday", "2016-05-08": "Mother's Day",
            "2016-06-19": "Father's Day", "2016-07-03": "4th of July Weekend",
            "2016-10-02": "Rosh Hashanah (begins at sundown)", "2016-11-27":
            "Thanksgiving Weekend"})

def secondsundays(d):
    while d.year == 2016:
        yield d
        d += timedelta(days = 14)

start1 = date(2016, 1, 3)
start2 = date(2016, 1, 10)
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
