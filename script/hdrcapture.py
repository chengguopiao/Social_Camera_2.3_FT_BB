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

a          = util.Adb()
sm         = util.SetCaptureMode()
so         = util.SetOption()
tb         = util.TouchButton()
modeNumber = util.ModeNumber['hdr']
confirmMode = util.ConfirmMode

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        a.setUpDevice()
        sm.switchCaptureMode('Single','HDR')
        tb.confirmCameraMode(confirmMode['Single'])

    def tearDown(self):
    	#a.cmd('pm','com.intel.camera22') #Force reset the camera settings to default
        super(CameraTest,self).tearDown()
        #self._pressBack(4)
        a.tearDownDevice()

    def testCapturePictureWithFDOn(self):
        '''
            Summary: Capture image with FD/FR ON
            Steps  : 
                1.Launch HDR capture activity
                2.Set FD/FR ON
                3.Touch shutter button to capture picture
                4.Exit activity
        '''
        so.setCameraOption('Face Detection','on')
        tb.confirmSettingMode('Face Detection','on',modeNumber)
        tb.captureAndCheckPicCount('single')

    def testCapturePictureWithFDOff(self):
        '''
            Summary: Capture image with FD/FR OFF
            Steps  : 
                1.Launch HDR capture activity
                2.Set FD/FR OFF
                3.Touch shutter button to capture picture
                4.Exit  activity
        '''
        so.setCameraOption('Face Detection','off')
        tb.confirmSettingMode('Face Detection','off',modeNumber)
        tb.captureAndCheckPicCount('single')

    def testCapturePictureWithPictureSizeStandard(self):
        '''
            Summary: Capture image with Photo size 13MP
            Steps  : 
                1.Launch HDR capture activity
                2.Set photo size 13MP
                3.Touch shutter button to capture picture
                4.Exit  activity
        '''
        so.setCameraOption('Picture Size','StandardScreen')
        tb.confirmSettingMode('Picture Size','StandardScreen',modeNumber)
        tb.captureAndCheckPicCount('single')

    def testCaptureWithPictureSizeWidesreen(self):
        '''
            Summary: Capture image with Photo size 6MP
            Steps  : 
                1.Launch HDR capture activity
                2.Set photo size 6MP
                3.Touch shutter button to capture picture
                4.Exit  activity
        '''
        so.setCameraOption('Picture Size','WideScreen')
        tb.confirmSettingMode('Picture Size','WideScreen',modeNumber)
        tb.captureAndCheckPicCount('single')

    def testCapturepictureWithGeoLocationOn(self):
        '''
            Summary: Capture image with Geo-tag ON
            Steps  : 
                1.Launch HDR capture activity
                2.Set photo Geo-tag ON
                3.Touch shutter button to capture picture
                4.Exit  activity
        '''
        so.setCameraOption('Geo Location','on')
        tb.confirmSettingMode('Geo Location','on',modeNumber)
        tb.captureAndCheckPicCount('single')

    def testCapturepictureWithGeoLocationOff(self):
        """
        Summary: Capture image with Geo-tag OFF
        Steps  :  1.Launch HDR capture activity
                2.Set photo Geo-tag OFF
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('Geo Location','off')
        tb.confirmSettingMode('Geo Location','off',modeNumber)
        tb.captureAndCheckPicCount('single')

    def testCapturePictureWithSelfTimerOff(self):
        """
        Summary: Capture image with Self-timer off
        Steps  :  1.Launch HDR capture activity
                2.Set Self-timer off
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('Self Timer','0')
        tb.confirmSettingMode('Self Timer','0',modeNumber)
        tb.captureAndCheckPicCount('single')

    def testCapturePictureWithThreeSec(self):
        """
        Summary: Capture image with Self-timer 3s
        Steps  :  1.Launch HDR capture activity
                2.Set Self-timer 3s
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('Self Timer','3')
        tb.confirmSettingMode('Self Timer','3',modeNumber)
        tb.captureAndCheckPicCount('single',10)

    def testCapturePictureWithFiveSec(self):
        """
        Summary: Capture image with Self-timer 5s
        Steps  :  1.Launch HDR capture activity
                2.Set Self-timer 5s
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('Self Timer','5')
        tb.confirmSettingMode('Self Timer','5',modeNumber)
        tb.captureAndCheckPicCount('single',10)

    def testCapturePictureWithTenSec(self):
        """
        Summary: Capture image with Self-timer 10s
        Steps  :  1.Launch HDR capture activity
                2.Set Self-timer 10s
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('Self Timer','10')
        tb.confirmSettingMode('Self Timer','10',modeNumber)
        tb.captureAndCheckPicCount('single',11)
