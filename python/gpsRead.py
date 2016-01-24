#! /usr/bin/python
# Written by Dan Mandle http://dan.mandle.me September 2012
# License: GPL 2.0
# Hacked about by Linsey !
 
import os
from gps import *
from time import *
import time
import threading
import rangeSensorLib as rsl
 
gpsd = None #seting the global variable
 
os.system('clear') #clear the terminal (optional)
 
class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
 
if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    rsl.setDefaults()
    rsl.setup()
    outFile = open('output.txt', 'w')
    print "Sensor settling"
    time.sleep(2)
    count = 0
    while (count < 30):
      #It may take a second or two to get good data
      #print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc
 
      # Build up our logging string
      distance = rsl.measureDistance()
      print(distance)
      stringToWrite=str(gpsd.utc) + ',' + str(gpsd.fix.latitude) + ',' + str(gpsd.fix.longitude) + ',' + str(distance)
      print stringToWrite
      outFile.write(stringToWrite + '\n')
 
      count = count + 1 
      print 'count is ' , count
      time.sleep(1) #set to whatever

    # Stop the thread and wait nicely.
    print 'Exiting Nicely'
    gpsp.running=False
    gpsp.join() 
    rsl.cleanup()
    outFile.close()

  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
