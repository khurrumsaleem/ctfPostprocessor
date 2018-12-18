'''
Created on Dec 13, 2018

@author: alptezbasaran
'''

import math
import os
import sys
import matplotlib.pyplot as py

# Unit conversion factors
# These following conversion factors have been implemented in CTF Code previously.
# There is no need to add them again
t_in_m=0.0254
t_BTU_kJ=1.05506
t_MJ_kJ=1000.0
t_kJ_MJ=1/t_MJ_kJ
t_hr_s=3600.0
t_ft_m=0.3048


class channelData:
  '''
  Reads data from specified file
  '''
  def __init__(self, channelsOutputFileName):
    '''
    '''
    self.channelsOutputFile = channelsOutputFileName
    print('ayakChannels')
#    print(self.channelsOutputFile)

class majorData:
  '''
  Reads data from *.ctf.out
  Converts British units to SI if asked
  '''
  def __init__(self,majorOutputFileName):
    '''
    @In - major putput file name
    '''
    self.majorOutputFile = majorOutputFileName
    print('ayakMajor')
#    print(self.majorOutputFile)
    

    self.lines = open(majorOutputFileName).readlines()
    # To invoke information in each time step reader functions are invoked
    # But first time information should be extracted
    # A default option to extract data at the last step must be added



# To run as a script
if __name__ == "__main__":

  inputName = 'ctfM_0_dropletInjection'
  channel = channelData(inputName + '.ctf.channels.out')
  major   = majorData(inputName + '.ctf.out')
