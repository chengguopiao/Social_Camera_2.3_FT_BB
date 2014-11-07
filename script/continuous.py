#!/usr/bin/python
# coding:utf-8

from uiautomatorplug.android import device as d
import commands
import re
import subprocess
import os
import string
import time
import sys
import util 
import unittest

a  = util.Adb()
sm = util.SetCaptureMode()
tb = util.TouchButton()
so = util.SetOption()

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        a.setUpDevice()
        sm.switchCaptureMode('Single')


    def tearDown(self):
        super(CameraTest,self).tearDown()
        a.tearDownDevice()



### Continuous capture(merge into single capture mode) 40 ###
# Test case 1
    #def testContinuousCapturePictureWithFlashOn(self):
        """
        Summary:testCapturePictureWithFlashOn: Take a picture with flash on
        Steps:  1.Launch single capture activity
                2.Set flash ON
                3.Touch shutter button to capture picture
        """
        # step 2
    #    so.setCameraOption('Flash','on')
        # step 4~5
    #    tb.captureAndCheckPicCount('longclick',3)          

# Test case 2
    #def testContinuousCapturePictureWithFlashOff(self):
        """
        Summary:testCapturePictureWithFlashOn: Take a picture with flash on
        Steps:  1.Launch single capture activity
                2.Set flash off
                3.Touch shutter button to capture picture
        """
        # step 2
    #    so.setCameraOption('Flash','off')
        # step 4~5
    #    tb.captureAndCheckPicCount('longclick',3)  

# Test case 3
    #def testContinuousCapturePictureWithFlashAuto(self):
        """
        Summary:testCapturePictureWithFlashAuto: Take a picture with flash auto
        Steps:  1.Launch single capture activity
                2.Set flash auto
                3.Touch shutter button to capture picture
        """
        # step 2
    #    so.setCameraOption('Flash','auto')
        # step 4~5
    #    tb.captureAndCheckPicCount('longclick',3)  

# Test case 4
    def testContinuousCaptureWithExposureAuto(self):
        """
        Summary:testCaptureWithExposureZero: Take a picture with Exposure 0
        Steps: 1.Launch single capture activity
               2.Set exposure 0
               3.Touch shutter button to capture picture

        """
        # step 2
        so.setCameraOption('Exposure','0')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)    

# Test case 5    
    def testContinuousCaptureWithExposurePlusOne(self):
        """
        Summary:testCaptureWithExposurePlusOne: Take a picture with Exposure +1
        Steps: 1.Launch single capture activity
               2.Set exposure +1
               3.Touch shutter button to capture picture
        """
        # step 2
        so.setCameraOption('Exposure','3')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3) 

# Test case 6
    def testContinuousCaptureWithExposurePlusTwo(self):
        """
        Summary:testCaptureWithExposurePlusTwo: Take a picture with Exposure +2
        Steps: 1.Launch single capture activity
               2.Set exposure +2
               3.Touch shutter button to capture picture
        """
        # step 2
        so.setCameraOption('Exposure','6')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)         

# Test case 7
    def testContinuousCaptureWithExposureRedOne(self):
        """
        Summary:testCaptureWithExposureRedOne: Take a picture with Exposure -1
        Steps: 1.Launch single capture activity
               2.Set exposure -1
               3.Touch shutter button to capture picture
               4.Exit  activity
        """
        # step 2
        so.setCameraOption('Exposure','-3')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)       

# Test case 8
    def testContinuousCaptureWithExposureRedTwo(self):
        """
        Summary:testCaptureWithExposureRedOne: Take a picture with Exposure -2
        Steps: 1.Launch single capture activity
               2.Set exposure -2
               3.Touch shutter button to capture picture
               4.Exit  activity
        """
        # step 2
        so.setCameraOption('Exposure','-6')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)

# Test case 9
    def testContinuousCapturePictureWithScenesAuto(self):
        """
        Summary:testCapturePictureWithScenesAuto: Take a picture with set scenes to Auto
        Steps:  1.Launch single capture activity
                2.Set scene mode Auto
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        # step 2
        so.setCameraOption('Exposure','0')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3) 

# Test case 10
    def testContinuousCapturePictureWithScenesSport(self):
        """
        Summary:testCapturePictureWithScenesSport: Take a picture with set scenes to Sports
        Steps:  1.Launch single capture activity
                2.Set scene mode Sports
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        # step 2
        so.setCameraOption('Scenes','sports')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)   

# Test case 11
    #def testContinuousCapturePictureWithScenesNightportrait(self):
        """
        Summary:testCapturePictureWithScenesNightportrait: Capture image with Scene mode Night-portrait
        Steps:  1.Launch single capture activity
                2.Set scene mode night-portrait
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        # step 2
    #    so.setCameraOption('Scenes','night-portrait')
        # step 4~5
    #    tb.captureAndCheckPicCount('longclick',3) 

# Test case 12
    def testContinuousCapturePictureWithScenesPortrait(self):
        """
        Summary:testCapturePictureWithScenesPortrait: Take a picture with set scenes to Portrait
        Steps:  1.Launch single capture activity
                2.Set scene mode Portrait
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        # step 2
        so.setCameraOption('Scenes','portrait')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3) 

# Test case  13
    #def testContinuousCapturePictureWithScenesBarcode(self):
        """
        Summary:testCapturePictureWithScenesBarcode: Capture image with Scene mode barcode
        Steps:  1.Launch single capture activity
                2.Set scene mode barcode
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        # step 2
    #    so.setCameraOption('Scenes','barcode')
        # step 4~5
    #    tb.captureAndCheckPicCount('longclick',3) 

# Test case 14
    def testContinuousCapturePictureWithScenesLandscape(self):
        """
        Summary:testCapturePictureWithScenesLandscape: Take a picture with set scenes to Landscape
        Steps:  1.Launch single capture activity
                2.Set scene mode Landscape
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        # step 2
        so.setCameraOption('Scenes','landscape')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3) 

# Test case 15
    def testContinuousCapturePictureWithScenesNight(self):
        """
        Summary:testCapturePictureWithScenesNight: Take a picture with set scenes to Night
        Steps:  1.Launch single capture activity
                2.Set scene mode Night
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        # step 2
        so.setCameraOption('Scenes','night')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3) 

# Test case 16
    def testContinuousCapturePictureWithFDON(self):
        """
        Summary:testCapturePictureWithFDON: Take a picture with set FD/FR on
        Steps:  1.Launch single capture activity
                2.Set FD/FR ON
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        # step 2
        so.setCameraOption('Face Detection','on')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)     

# Test case 17
    def testContinuousCaptureWithPictureSizeWidesreen(self):
        """
        Summary:testCaptureWithSize6M: Take a picture with  picture size is Widesreen
        Steps:  1.Launch single capture activity
                2.Set picture size is Widesreen
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        # step 2
        so.setCameraOption('Picture Size','WideScreen')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)

# Test case 18
    def testContinuousCapturePictureWithPictureSizeStandard(self):
        """
        Summary:testCapturePictureWithPictureSizeStandard: Take a picture with picture size is standard
        Steps:  1.Launch single capture activity
                2.Set picture size is standard
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        # step 2
        so.setCameraOption('Picture Size','StandardScreen')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3) 

# Test case 19
    def testContinuousCapturepictureWithGeoLocationOn(self):
        """
        Summary:testCapturepictureWithGeoLocationOn:Take a picture with  geolocation is on
        Steps:  1.Launch camera app
                2.Set geo location on 
                3.Touch shutter button to capture picture
                4.Exit  activity
        """ 
        # step 2
        so.setCameraOption('Geo Location','on')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)         

# Test case 20
    def testContinuousCapturepictureWithGeoLocationOff(self):
        """
        Summary:testCapturepictureWithGeoLocationOff: Take a picture with  geolocation is off
        Steps:  1.Launch camera app
                2.Set geo location off 
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        # step 2
        so.setCameraOption('Geo Location','off')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)  

# Test case 21
    def testContinuousCapturepictureWithHintsOn(self):
        """
        Summary:testCapturepictureWithHintsOn: Take a picture with  hints is on
        Steps:  1.Launch camera app
                2.Set hints on
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('Hints','on')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)          

# Test case 22
    def testContinuousCapturepictureWithHintsOff(self):
        """
        Summary:testCapturepictureWithHintsOff: Take a picture with  hints is off
        Steps:  1.Launch camera app
                2.Set hints off
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('Hints','off')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)     

# Test case 23
    def testContinuousCapturepictureWithSelfTimerOff(self):
        """
        Summary:testCapturepictureWithSelfTimerOff: Capture image with Self-timer off
        Steps:  1.Launch single capture activity
                2.Set Self-timer off
                3.Touch shutter button to capture picture
                4.Exi
        """
        so.setCameraOption('Self Timer','0')
        # step 4~5
        tb.captureAndCheckPicCount('single',3)  

# Test case 24
    def testContinuousCapturepictureWithSelfTimerThreeSec(self):
        """
        Summary:testCapturepictureWithSelfTimerThreeSec: Capture image with Self-timer 3s
        Steps:  1.Launch single capture activity
                2.Set Self-timer 3s
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('Self Timer','3')
        # step 4~5
        tb.captureAndCheckPicCount('single',3)

# Test case 25
    def testContinuousCapturepictureWithSelfTimerFiveSec(self):
        """
        Summary:testCapturepictureWithSelfTimerFiveSec: Capture image with Self-timer 5s
        Steps:  1.Launch single capture activity
                2.Set Self-timer 5s
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('Self Timer','5')
        # step 4~5
        tb.captureAndCheckPicCount('single',3)

# Test case 26
    def testContinuousCapturepictureWithSelfTimerTenSec(self):
        """
        Summary:testCapturepictureWithSelfTimerTenSec: Capture image with Self-timer 10s
        Steps:  1.Launch single capture activity
                2.Set Self-timer 10s
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('Self Timer','10')
        # step 4~5
        tb.captureAndCheckPicCount('single',3)

# Test case 27
    def testContinuousCapturepictureWithISOAuto(self):
        """
        Summary:testCapturepictureWithISOAuto: Capture image with ISO Setting Auto
        Steps:  1.Launch single capture activity
                2.Set ISO Setting Auto
                3.Touch shutter button to capture picture
                4.Exit  activity
        """    
        so.setCameraOption('ISO','iso-auto')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)

# Test case 28
    def testContinuousCapturepictureWithISOHundred(self):
        """
        Summary:testCapturepictureWithISOHundred: Capture image with ISO Setting 100
        Steps:  1.Launch single capture activity
                2.Set ISO Setting 100
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('ISO','iso-100')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)

# Test case 29
    def testContinuousCapturepictureWithISOTwoHundred(self):
        """
        Summary:testCapturepictureWithISOTwoHundred: Capture image with ISO Setting 200
        Steps:  1.Launch single capture activity
                2.Set ISO Setting 200
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('ISO','iso-200')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)

# Test case 30
    def testContinuousCapturepictureWithISOFourHundred(self):
        """
        Summary:testCapturepictureWithISOFourHundred: Capture image with ISO Setting 400
        Steps:  1.Launch single capture activity
                2.Set ISO Setting 400
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('ISO','iso-400')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)

# Test case 31
    def testContinuousCapturepictureWithISOEightHundred(self):
        """
        Summary:testCapturepictureWithISOEightHundred: Capture image with ISO Setting 800
        Steps:  1.Launch single capture activity
                2.Set ISO Setting 800
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('ISO','iso-800')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)

# Test case 32
    def testContinuousCapturepictureWithWhiteBalanceAuto(self):
        """
        Summary:testCapturepictureWithWhiteBalanceAuto: Capture image with White Balance Auto
        Steps:  1.Launch single capture activity
                2.Set White Balance Auto
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('White Balance','auto')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)      

# Test case 33
    def testContinuousCapturepictureWithWhiteBalanceIncandescent(self):
        """
        Summary:testCapturepictureWithWhiteBalanceIncandescent: Capture image with White Balance Incandescent
        Steps:  1.Launch single capture activity
                2.Set White Balance Incandescent
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('White Balance','incandescent')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)   

# Test case 34
    def testContinuousCapturepictureWithWhiteBalanceDaylight(self):
        """
        Summary:testCapturepictureWithWhiteBalanceDaylight: Capture image with White Balance Daylight
        Steps:  1.Launch single capture activity
                2.Set White Balance Daylight
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('White Balance','daylight')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3) 

# Test case 35
    def testContinuousCapturepictureWithWhiteBalanceFluorescent(self):
        """
        Summary:testCapturepictureWithWhiteBalanceFluorescent: Capture image with White Balance Fluorescent
        Steps:  1.Launch single capture activity
                2.Set White Balance Fluorescent
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('White Balance','fluorescent')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)

# Test case 36
    def testCapturepictureWithWhiteBalanceCloudy(self):
        """
        Summary:testCapturepictureWithWhiteBalanceCloudy: Capture image with White Balance Cloudy
        Steps:  1.Launch single capture activity
                2.Set White Balance Cloudy
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('White Balance','cloudy-daylight')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)

# Test case 37
    def testFrontCapturePictureWithFDOff(self):
        """
        Summary:testCapturePictureWithFDOff: Take a picture with set FD/FR off
        Steps:  1.Launch single capture activity
                2.Set FD/FR Off
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        tb.switchBackOrFrontCamera('front')
        so.setCameraOption('Face Detection','off')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3) 

# Test case 38
    def testFrontCapturePictureWithFDON(self):
        """
        Summary:testCapturePictureWithFDON: Take a picture with set FD/FR on
        Steps:  1.Launch single capture activity
                2.Set FD/FR ON
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        tb.switchBackOrFrontCamera('front')
        so.setCameraOption('Face Detection','on')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)    

# Test case 39
    def testFrontCapturepictureWithGeoLocationOn(self):
        """
        Summary:testCapturepictureWithGeoLocationOn:Take a picture with  geolocation is on
        Steps:  1.Launch camera app
                2.Set geo location on 
                3.Touch shutter button to capture picture
                4.Exit  activity
        """ 
        tb.switchBackOrFrontCamera('front')
        so.setCameraOption('Geo Location','on')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3) 

# Test case 40
    def testFrontCapturepictureWithGeoLocationOff(self):
        """
        Summary:testCapturepictureWithGeoLocationOff: Take a picture with  geolocation is off
        Steps:  1.Launch camera app
                2.Set geo location off 
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        tb.switchBackOrFrontCamera('front')
        so.setCameraOption('Geo Location','off')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3) 

# Test case 41
    def testCapturePictureWithFDOff(self):
        """
        Summary:testCapturePictureWithFDOff: Take a picture with set FD/FR off
        Steps:  1.Launch single capture activity
                2.Set FD/FR Off
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('Face Detection','off')
        # step 4~5
        tb.captureAndCheckPicCount('longclick',3)
# Test case 