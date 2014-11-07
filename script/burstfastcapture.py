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

#Written by ZhuYanbo

AD         = util.Adb()
tb         = util.TouchButton()
so         = util.SetOption()
sm         = util.SetCaptureMode()
modeNumber = util.ModeNumber['burst']

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        AD.setUpDevice(False)
        sm.switchCaptureMode('Burst','Fast')

    def tearDown(self):
        super(CameraTest,self).tearDown()
        AD.tearDownDevice()

    def testCaptureWithExposureAuto(self):
        '''
            Summary: Capture image with Exposure auto
            Steps  :  
                1.Launch burst activity and select Fast burst mode
                2.Check exposure setting icon ,set to auto
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        '''
        so.setCameraOption('Exposure','0',modeNumber)
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
        so.setCameraOption('Exposure','3',modeNumber)
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
        so.setCameraOption('Exposure','6',modeNumber)
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
        so.setCameraOption('Exposure','-3',modeNumber)
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
        so.setCameraOption('Exposure','-6',modeNumber)
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
        so.setCameraOption('Scenes','auto',modeNumber)
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
        so.setCameraOption('Scenes','sports',modeNumber)
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
        so.setCameraOption('Scenes','night',modeNumber)
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
        so.setCameraOption('Scenes','landscape',modeNumber)
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
        so.setCameraOption('Scenes','portrait',modeNumber)
        tb.captureAndCheckPicCount('single',3)

    #def testCapturePictureWithScenesNightPortrait(self):
        '''
            Summary: Capture image with Scene mode Night-portrait
            Steps  :  
                1.Launch burst activity and select Fast burst mode
                2.Check scence mode ,set mode to Night-portrait
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        '''
    #    so.setCameraOption('Scenes','night-portrait',modeNumber)
    #    tb.captureAndCheckPicCount('single',3)

    def testCapturePictureWithSizeWidescreen(self):
        '''
            Summary: Capture image with Photo size 6MP
            Steps  :  
                1.Launch burst activity and select Fast burst mode
                2.Check photo size ,set to 6MP
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        '''
        so.setCameraOption('Picture Size','WideScreen',modeNumber)
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
        so.setCameraOption('Picture Size','StandardScreen',modeNumber)
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
        so.setCameraOption('Geo Location','on',modeNumber)
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
        so.setCameraOption('Geo Location','off',modeNumber)
        tb.captureAndCheckPicCount('single',3)
