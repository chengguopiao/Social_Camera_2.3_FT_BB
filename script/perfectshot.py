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

#Written by ZhuYanbo

a          = util.Adb()
sm         = util.SetCaptureMode()
tb         = util.TouchButton()
so         = util.SetOption()
modeNumber = util.ModeNumber['perfectshot']

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        a.setUpDevice()
        sm.switchCaptureMode('Perfect Shot')   # change panorama mode

    def tearDown(self):
        super(CameraTest,self).tearDown()
        a.tearDownDevice()

# PerfectShot capture 14
# Test case 1
    def testPerfectShotCaptureWithExposureAuto(self):
        """
        Summary:testCaptureWithExposureZero: Take burst piture with exposure 0
        Steps:  1.Launch perfect shot activity
                2.Check exposure setting icon ,set to 0
                3.Touch shutter button to capture picture
        """
        

        # step 2
        so.setCameraOption('Exposure','0',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('single',2)

# Test case 2        
    def testPerfectShotCaptureWithExposurePlusOne(self):
        """
        Summary:testCaptureWithExposurePlusOne: Take burst piture with exposure +1
        Steps:  1.Launch perfect shot activity
                2.Check exposure setting icon ,set to +1
                3.Touch shutter button to capture picture
        """
        

        # step 2
        so.setCameraOption('Exposure','3',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('single',2)

# Test case 3    
    def testPerfectShotCaptureWithExposurePlusTwo(self):
        """
        Summary:testCapturePictureWithExposurePlusOne: Take burst piture with exposure +2
        Steps:  1.Launch perfect shot activity
                2.Check exposure setting icon ,set to +2
                3.Touch shutter button to capture picture
        """
        

        # step 2
        so.setCameraOption('Exposure','6',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('single',2)
# Test case 4
    def testPerfectShotCaptureWithExposureRedOne(self):
        """
        Summary:testCaptureWithExposureRedOne: Take burst piture with exposure -1
        Steps:  1.Launch perfect shot activity
                2.Check exposure setting icon ,set to -1
                3.Touch shutter button to capture picture
        """  
        

        # step 2
        # step 2
        so.setCameraOption('Exposure','-3',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('single',2)

# Test case 5
    def testPerfectShotCaptureWithExposureRedTwo(self):
        """
        Summary:testCaptureWithExposureRedTwo: Take burst piture with exposure -2
        Steps:  1.Launch perfect shot activity
                2.Check exposure setting icon ,set to -2
                3.Touch shutter button to capture picture
        """
        

        # step 2
        so.setCameraOption('Exposure','-6',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('single',2)

# Test case 6
    def testPerfectShotCapturePictureWithScenesAuto(self):
        """
        Summary:testCapturePictureWithScenesAuto: Take picture with set scenes to auto
        Steps:  1.Launch perfect shot activity
                2.Check scence mode ,set mode to auto
                3.Touch shutter button to capture picture
        """
        

        # step 2
        so.setCameraOption('Scenes','auto',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('single',2)

# Test case 7
    def testPerfectShotCapturePictureWithScenesSport(self):
        """
        Summary:testCapturePictureWithScenesSport: Take picture with set scenes to Sports
        Steps:  1Launch perfect shot activity
                2.Check scence mode ,set mode to Sports
                3.Touch shutter button to capture picture
        """
        

        # step 2
        so.setCameraOption('Scenes','sports',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('single',2)

# Test case 8
    #def testPerfectShotCapturePictureWithScenesNightPortrait(self):
        """
        Summary:testCapturePictureWithScenes NightPortrait: Capture image with Scene modeNightPortrait
        Steps:  1.Launch perfect shot activity
                2.Set Scene mode Night-portrait
                3.Touch shutter button to capture picture
        """
        

        # step 2
    #    so.setCameraOption('Scenes','night-portrait')
        # step 4~5
    #    tb.captureAndCheckPicCount('single',10)       

# Test case 9
    def testPerfectShotCapturePictureWithScenesLandscape(self):
        """
        Summary:testCapturePictureWithScenesLandscape: Take picture with set scenes to landscape
        Steps:  1.Launch perfect shot activity
                2.Check scence mode ,set mode to landscape
                3.Touch shutter button to capture picture
        """
        

        # step 2
        so.setCameraOption('Scenes','landscape',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('single',2)     

# Test case 10
    def testPerfectShotCapturePictureWithScenesPortrait(self):
        """
        Summary:testCapturePictureWithScenesSport: Take picture with set scenes to portrait
        Steps:  1.Launch perfect shot activity
                2.Check scence mode ,set mode to portrait
                3.Touch shutter button to capture picture
        """
        

        # step 2
        so.setCameraOption('Scenes','portrait',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('single',2)       

# Test case 11
    def testPerfectShotCapturePictureWithScenesNight(self):
        """
        Summary:testCapturePictureWithScenesNight: Take picture with set scenes to night
        Steps:  1.Launch perfect shot activity
                2.Check scence mode ,set mode to night
                3.Touch shutter button to capture picture
        """
        

        # step 2
        so.setCameraOption('Scenes','night',modeNumber)
        # step 4~5
        time.sleep(3)
        tb.captureAndCheckPicCount('single',10)  

# Test case 12
    #def testPerfectShotCapturePictureWithScenesBarcode(self):
        """
        Summary:testCapturePictureWithScenesBarcode: Capture image with Scene mode Barcode
        Steps:  1.Launch perfect shot activity
        2.Set Scene mode Barcode
        3.Touch shutter button to capture picture
        """
        

        # step 2
    #    so.setCameraOption('Scenes','barcode')
        # step 4~5
    #    tb.captureAndCheckPicCount('single',2) 

# Test case 13
    def testPerfectShotCapturepictureWithGeoLocationOn(self):
        """
        Summary:testCapturepictureWithGeoLocationOn: capture PerfectShot picture in geolocation on mode
        Steps:  1.Launch perfect shot activity
                2.Check geo-tag ,set to ON
                3.Touch shutter button to capture picture
        """ 
        

        # step 2
        so.setCameraOption('Geo Location','on',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('single',2)  

# Test case 14
    def testPerfectShotCapturepictureWithGeoLocationOff(self):
        """
        Summary:testCapturepictureWithGeoLocationOff: capture PerfectShot picture in geolocation off mode
        Steps:  1.Launch perfect shot activity
                2.Check geo-tag ,set to Off
                3.Touch shutter button to capture  picture
        """ 
        
        # step 2
        so.setCameraOption('Geo Location','off',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('single',2)  