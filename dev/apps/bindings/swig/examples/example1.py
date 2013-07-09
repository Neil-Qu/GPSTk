# This is a python port of gpstk/dev/examples/example1.cpp

from gpstk import *

# In the GPSTk there are multiple classes to manage time, depending
# on the specific operation that we want to carry out. This modular
# approach eases handling the many different time systems used in the
# modern Global Navigation Satellite Systems.

# Note, however, that in the GPSTk the unifying class to do time
# Computations is the 'CommonTime' class.

# Read current time from system clock
systime = SystemTime()

# Convert to 'CommonTime', the standard way to handle time at GPSTk
comtime = systime.convertToCommonTime()

# This is the typical way to handle civil time
civtime = CivilTime(comtime)

# The YDSTime class is very useful for common GNSS tasks
ydstime = YDSTime(comtime)

# This is a typical class to handle time in GPS system
gpstime = GPSWeekSecond(comtime)

# Class to handle Modified Julian Date
mjd = MJD(comtime)

print "Hello world!"
print "   The current civil time is ", civtime 
print "   The current year is ", ydstime.year 
print "   The current day of year is ", ydstime.doy 
print "   The current second of day is ", ydstime.sod
print "   The current full GPS week is ", gpstime.week
print "   The current short GPS week is ", gpstime.getWeek10()
print "   The current day of GPS week is ", gpstime.getDayOfWeek()
print "   The current second of GPS week is ", gpstime.sow
print "   The current Modified Julian Date is ", mjd