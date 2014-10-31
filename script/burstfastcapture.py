#!/usr/bin/python
# coding:utf-8

from uiautomatorplug.android import device as d
import unittest
import commands
import re
import subprocess
import os
import string
import time
import sys
import util 
import string

AD = util.Adb()
tb = util.TouchButton()
so = util.SetOption()
sm = util.SetCaptureMode()

#Written by XuGuanjun

PACKAGE_NAME  = 'com.intel.camera22'
ACTIVITY_NAME = PACKAGE_NAME + '/.Camera'

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        self._launchCamera()
        time.sleep(2)
        if d(text = 'Yes').wait.exists(timeout = 3000):
            d(text = 'Yes').click.wait()
        if d(text = 'Skip').wait.exists(timeout = 3000):
            d(text = 'Skip').click.wait() 
        sm.switchCaptureMode('Burst','Fast')

    def tearDown(self):
        super(CameraTest,self).tearDown()
        self._pressBack(4)
        AD.cmd('pm','com.intel.camera22') #Force reset the camera settings to default
        time.sleep(2)

    def testCaptureWithExposureAuto(self):
        '''
            Summary: Capture image with Exposure auto
            Steps  :  
                1.Launch burst activity and select Fast burst mode
                2.Check exposure setting icon ,set to auto
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        '''
        so.setCameraOption('Exposure','0')
        tb.captureAndCheckPicCount('single',3)

    def testCaptureWithExposurePlugOne(self):
        '''
            Summary: Capture image with Exposure plug one
            Steps  :  
                1.Launch burst activity and select Fast burst mode
                2.Check exposure setting icon ,set to plug one
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        '''
        so.setCameraOption('Exposure','3')
        tb.captureAndCheckPicCount('single',3)

    def testCaptureWithExposurePlugTwo(self):
        '''
            Summary: Capture image with Exposure plug two
            Steps  :  
                1.Launch burst activity and select Fast burst mode
                2.Check exposure setting icon ,set to plug two
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        '''
        so.setCameraOption('Exposure','6')
        tb.captureAndCheckPicCount('single',3)

    def testCaptureWithExposureRedOne(self):
        '''
            Summary: Capture image with Exposure red one
            Steps  :  
                1.Launch burst activity and select Fast burst mode
                2.Check exposure setting icon ,set to red one
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        '''
        so.setCameraOption('Exposure','-3')
        tb.captureAndCheckPicCount('single',3)

    def testCaptureWithExposureRedTwo(self):
        '''
            Summary: Capture image with Exposure red two
            Steps  :  
                1.Launch burst activity and select Fast burst mode
                2.Check exposure setting icon ,set to red two
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        '''
        so.setCameraOption('Exposure','-6')
        tb.captureAndCheckPicCount('single',3)

    def testCapturePictureWithScenesAuto(self):
        '''
            Summary: Capture image with Scene mode AUTO
            Steps  :  
                1.Launch burst activity and select Fast burst mode
                2.Check scence mode ,set mode to AUTO
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        '''
        so.setCameraOption('Scenes','auto')
        tb.captureAndCheckPicCount('single',3)

    def testCapturePictureWithScenesSports(self):
        '''
            Summary: Capture image with Scene mode Sports
            Steps  :  
                1.Launch burst activity and select Fast burst mode
                2.Check scence mode ,set mode to Sports
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        '''
        so.setCameraOption('Scenes','sports')
        tb.captureAndCheckPicCount('single',3)

    def testCapturePictureWithScenesNight(self):
        '''
            Summary: Capture image with Scene mode Night
            Steps  :  
                1.Launch burst activity and select Fast burst mode
                2.Check scence mode ,set mode to Night
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        '''
        so.setCameraOption('Scenes','night')
        tb.captureAndCheckPicCount('single',3)

    def testCapturePictureWithScenesLandscape(self):
        '''
            Summary: Capture image with Scene mode Landscape
            Steps  :  
                1.Launch burst activity and select Fast burst mode
                2.Check scence mode ,set mode to Landscape
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        '''
        so.setCameraOption('Scenes','landscape')
        tb.captureAndCheckPicCount('single',3)

    def testCapturePictureWithScenesPortrait(self):
        '''
            Summary: Capture image with Scene mode Portrait
            Steps  :  
                1.Launch burst activity and select Fast burst mode
                2.Check scence mode ,set mode to Portrait
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        '''
        so.setCameraOption('Scenes','portrait')
        tb.captureAndCheckPicCount('single',3)

    def testCapturePictureWithScenesNightPortrait(self):
        '''
            Summary: Capture image with Scene mode Night-portrait
            Steps  :  
                1.Launch burst activity and select Fast burst mode
                2.Check scence mode ,set mode to Night-portrait
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        '''
        so.setCameraOption('Scenes','night-portrait')
        tb.captureAndCheckPicCount('single',3)

    def testCapturePictureWithSizeWidescreen(self):
        '''
            Summary: Capture image with Photo size 6MP
            Steps  :  
                1.Launch burst activity and select Fast burst mode
                2.Check photo size ,set to 6MP
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        '''
        so.setCameraOption('Picture Size','WideScreen')
        tb.captureAndCheckPicCount('single',3)

    def testCapturePictureWithSizeStandard(self):
        '''
            Summary: Capture image with Photo size 13MP
            Steps  : 
                1.Launch burst activity and select Fast burst mode
                2.Check photo size ,set to 13MP
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        '''
        so.setCameraOption('Picture Size','StandardScreen')
        tb.captureAndCheckPicCount('single',3)
    
    def testCapturepictureWithGeoLocationOn(self):
        '''
            Summary: Capture image with Geo-tag ON
            Steps  : 
                1.Launch burst activity and select Fast burst mode
                2.Check geo-tag ,set to ON
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        '''
        so.setCameraOption('Geo Location','on')
        tb.captureAndCheckPicCount('single',3)

    def testCapturepictureWithGeoLocationOff(self):
        '''
            Summary: Capture image with Geo-tag Off
            Steps  : 
                1.Launch burst activity and select Fast burst mode
                2.Check geo-tag ,set to Off
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        '''
        so.setCameraOption('Geo Location','off')
        tb.captureAndCheckPicCount('single',3)

    def _captureAndCheckPicCount(self,capturemode,delaytime):
        beforeNo = AD.cmd('ls','/sdcard/DCIM/100ANDRO') #Get count before capturing
        TB.takePicture(capturemode)
        time.sleep(delaytime) #Sleep a few seconds for file saving
        afterNo = AD.cmd('ls','/sdcard/DCIM/100ANDRO') #Get count after taking picture
        if beforeNo != afterNo - 10: #If the count does not raise up after capturing, case failed
            self.fail('Taking picture failed!')

    def _launchCamera(self):
        d.start_activity(component = ACTIVITY_NAME)
        time.sleep(2)
        #When it is the first time to launch camera there will be a dialog to ask user 'remember location', so need to check
        #if d(text = 'OK').wait.exists(timeout = 2000):
        #    d(text = 'OK').click.wait()
        #assert d(resourceId = 'com.intel.camera22:id/shutter_button').wait.exists(timeout = 3000), 'Launch camera failed in 3s'

    def _pressBack(self,touchtimes):
        for i in range(0,touchtimes):
            d.press('back')
