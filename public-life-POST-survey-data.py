import os
from gps import *
from time import *
import json
import geojson
from geojson import Polygon
import time
import threading
import urllib
import urllib2
import requests
         
gpsd = None #seting the global variable


url = 'https://municipal.systems/v1/data?key=keyData' #keyData= is your Data Source Key. Generate this on the Source Page.

         
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
            while True:
              #It may take a second or two to get good data
         
              os.system('clear')
	     
              location_geometry = geojson.Polygon([[(-73.92534951531934, 40.702820344078994), (-73.92385284268903, 40.70436163484376), 
                (-73.92238299214887,40.7035604934359), (-73.92388502919721, 40.7020029168249), (-73.92534951531934,40.702820344078994)]])
              study_title = 'Maria Hernandez Test Study'
              survey_time_start = '2017-06-01'
              survey_time_stop = '2017-06-30'
              posture_sitting_formal = '20' #Use ISO 8601 syntax YYYY-MM-DD
              id = 'MHTest-062017'

         	
              print
              print ' GPS reading'
              print '----------------------------------------'
              print 'study_title ' , 'Flushing Meadows Corona Park Unisphere Study'
              print 'survey_time_start ' , '2017-06-01'
              print 'survey_time_stop  ' , '2017-06-30'


              payload = {'location_geometry':location_geometry, 'study_title':study_title, 'survey_time_start':survey_time_start, 
              'survey_time_stop':survey_time_stop, 'posture_sitting_formal':posture_sitting_formal, 'id':id}

              r = requests.post(url, json=payload)
              print r.content #200 = successful http request. 400 = bad request; check your syntax.  500 = server error, check stae status page.  
         
              time.sleep(20) #default value will send GPS data every 10 seconds. use faster speeds for faster or right-of-way vehicles.
         
          except (KeyboardInterrupt, SystemExit): #press ctrl+c to stop the program
            print "\nStopping GPS program..."
            gpsp.running = False
            gpsp.join() # wait for the thread to finish what it's doing
          print "Done.\nExiting."
