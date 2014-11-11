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

a           = util.Adb()
sm          = util.SetCaptureMode()
tb          = util.TouchButton()
so          = util.SetOption()
modeNumber  = util.ModeNumber['panorama']
confirmMode = util.ConfirmMode

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        a.setUpDevice()
        sm.switchCaptureMode('Panorama')   # change panorama mode
        tb.confirmCameraMode(confirmMode['Panorama'])

    def tearDown(self):
        super(CameraTest,self).tearDown()
        a.tearDownDevice()

### Panorama capture 12 ###
# Test case 1
    def testPanoramaCaptureWithExposureAuto(self):
    	'''
        Summary:testPanoramaCapturepictureWithGeoLocationOn: capture Panorama picture in geolocation on mode
        Steps: 
    	1.Launch Panorama activity
        2.Touch Exposure Setting icon, set Exposure auto
        3.Touch shutter button
        4.Touch shutter button to capture picture
        '''
        # step 2
        so.setCameraOption('Exposure','0')
        tb.confirmSettingMode('Exposure','0',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('smile',2)

# Test case 2
    def testPanoramaCaptureWithExposurePlusOne(self):   
        '''
        Summary:testPanoramaCaptureWithExposurePlusOne:capture Panorama picture with Exposure +1
        Steps  :
        1.Launch Panorama activity
        2.Touch Exposure Setting icon, set Exposure 1
        3.Touch shutter button 
        4.Touch shutter button to capture picture
        '''

        # step 2
        so.setCameraOption('Exposure','3')
        tb.confirmSettingMode('Exposure','3',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('smile',2)

# Test case 3
    def testPanoramaCaptureWithExposurePlusTwo(self):
        '''
        Summary:testPanoramaCapturePictureWithExposurePlusOne: capture Panorama picture with Exposure +2
        Steps: 
        1.Launch Panorama activity
        2.Touch Exposure Setting icon, set Exposure 2
        3.Touch shutter button 
        4.Touch shutter button to capture picture
        '''

        # step 2
        so.setCameraOption('Exposure','6')
        tb.confirmSettingMode('Exposure','6',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('smile',2)

# Test case 4
    def testPanoramaCaptureWithExposureRedOne(self):
        '''
        Summary:testPanoramaCaptureWithExposureRedOne: capture Panorama picture with Exposure -1
        Steps:
        1.Launch Panorama activity
        2.Touch Exposure Setting icon, set Exposure -1
        3.Touch shutter button 
        4.Touch shutter button to capture picture
        '''   

        # step 2
        so.setCameraOption('Exposure','-3')
        tb.confirmSettingMode('Exposure','-3',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('smile',2)

# Test case 5    
    def testPanoramaCaptureWithExposureRedTwo(self):
        '''
        Summary:testPanoramaCaptureWithExposureRedTwo: capture Panorama picture with Exposure -2
        Steps:
        1.Launch Panorama activity
        2.Touch Exposure Setting icon, set Exposure -1
        3.Touch shutter button 
        4.Touch shutter button to capture picture
        '''   

        # step 2
        so.setCameraOption('Exposure','-6')
        tb.confirmSettingMode('Exposure','-6',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('smile',2)

# Test case 6
    def testPanoramaCapturepictureWithGeoLocationOn(self):
        """
        Summary:testPanoramaCapturepictureWithGeoLocationOn: capture Panorama picture in geolocation on mode
        Steps:  1.Launch Panorama activity
                2.Check geo-tag ,set to ON
                3.Touch shutter button to capture picture
        """ 
        # step 1

        # step 2
        so.setCameraOption('Geo Location','on')
        tb.confirmSettingMode('Geo Location','on',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('smile',2)

# Test case 7
    def testPanoramaCapturepictureWithGeoLocationOff(self):
        """
        Summary:testPanoramaCapturepictureWithGeoLocationOff: capture Panorama picture in geolocation off mode
        Steps:  1.Launch Panorama activity
                2.Check geo-tag ,set to Off
                3.Touch shutter button to capture picture
                4.Exit activity
        """ 


        # step 2
        so.setCameraOption('Geo Location','off')
        tb.confirmSettingMode('Geo Location','off',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('smile',2)

# Test case 8
    def testPanoramaCapturepictureWithISOSettingAuto(self):
        """
        Summary:testPanoramaCapturepictureWithISOSettingAuto: Capture image with ISO Setting Auto
        Steps:  1.Launch Panorama activity
                2.Touch Geo-tag setting  icon,Set Geo-tag OFF
                3.Touch shutter button
                4.Touch shutter button to capture picture
                5.Exit  activity 
        """

        # step 2
        so.setCameraOption('ISO','iso-auto')
        tb.confirmSettingMode('ISO','iso-auto',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('smile',2)

# Test case 9    
    def testPanoramaCapturepictureWithISOSetting100(self):
        """
        Summary:testPanoramaCapturepictureWithISOSetting100: Capture image with ISO Setting 100
        Steps:  1.Launch Panorama activity
        2.Set ISO Setting 100
        3.Touch shutter button
        4.Touch shutter button to capture picture
        """

        # step 2
        so.setCameraOption('ISO','iso-100')
        tb.confirmSettingMode('ISO','iso-100',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('smile',2)

# Test case 10
    def testPanoramaCapturepictureWithISOSetting200(self):
        """
        Summary:testPanoramaCapturepictureWithISOSetting200: Capture image with ISO Setting 200
        Steps:  1.Launch Panorama activity
        2.Set ISO Setting 200
        3.Touch shutter button
        4.Touch shutter button to capture picture  
        """

        # step 2
        so.setCameraOption('ISO','iso-200')
        tb.confirmSettingMode('ISO','iso-200',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('smile',2)

# Test case 11
    def testPanoramaCapturepictureWithISOSetting400(self):
        """
        Summary:testPanoramaCapturepictureWithISOSetting400: Capture image with ISO Setting 400
        Steps:  1.Launch Panorama activity
        2.Set ISO Setting 400
        3.Touch shutter button
        4.Touch shutter button to capture picture
        5.Exit  activity 
        """

        # step 2
        so.setCameraOption('ISO','iso-400')
        tb.confirmSettingMode('ISO','iso-400',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('smile',2)

# Test case 12
    def testPanoramaCapturepictureWithISOSetting800(self):
        """
        Summary:testPanoramaCapturepictureWithISOSetting800: Capture image with ISO Setting 800
        Steps:  1.Launch Panorama activity
        2.Set ISO Setting 800
        3.Touch shutter button
        4.Touch shutter button to capture picture
        """

        # step 2
        so.setCameraOption('ISO','iso-800')
        tb.confirmSettingMode('ISO','iso-800',modeNumber)
        # step 4~5
        tb.captureAndCheckPicCount('smile',2)  
