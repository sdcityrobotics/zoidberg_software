# Standard output to use for testing mission
#
# Each vision output will look like:
# timestamp, ID, center_x, center_y, width, height, ID, ... repeat
#
#  Example Image
#   -----------> x
#  |  ..........................................  
#  |  ..........................................  
#  |  ..........................................  
#  |  ..........................................  
#  v  ...........<----w---->....................
#  y  ..........................................  
#     .......^...-----------....................
#     .......|...|.........|....................
#     .......h...|....C....|....................
#     .......|...|.........|....................
#     .......v...-----------....................
#     ..........................................  
#     ..........................................  
#  
# timestamp format: 2012-12-15 11:15:24.984000
# 

import time
import datetime
count = 0
output = []

def object_001():
   return ['001','463', '432', '34', '56']
def object_002():
   return ['002', '23', '123', '347', '21']
def object_003():
   return ['003', '765', '1002', '745', '102']

while(1):
   sTimeStamp = str(datetime.datetime.now()) #string timestamp
   if (count == 0):
      output.append(object_001())
   if (count == 1):
      output.append(object_001())
      output.append(object_002())
   if (count == 2):
      output.append(object_001())
      output.append(object_002())
      output.append(object_003())
     
   print(sTimeStamp, end='', flush=True) #not setting end='' is a Python 3 thing
   for iD, cx, cy, w, h in output:
      print(', ' + iD + ', ' + cx + ', ' + cy + ', ' + w + ', ' + h, end='', flush=True)
   print()
   
   count = (count + 1) % 3
   time.sleep(1)
   output = []
       

