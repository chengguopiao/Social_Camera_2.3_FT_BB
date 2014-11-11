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

a           = util.Adb()
sm          = util.SetCaptureMode()
tb          = util.TouchButton()
so          = util.SetOption()
confirmMode = util.ConfirmMode

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        a.setUpDevice()

    def tearDown(self):
        super(CameraTest,self).tearDown()
        a.tearDownDevice()

# Quick Switch 6

# Test case 1
    def testQuickSwitchtoSinglemode(self):
        """
        Summary:testQuickSwitchtoSinglemode: Quick Switch to Single mode
        Steps:  1.Launch single capture activity
                2.press change mode and then press Video icon to enter video
                3.press change mode icon then choose camera group 
        """    
        # steps 2
        sm.switchCaptureMode('Video')      # change video mode
        time.sleep(1)
        tb.confirmCameraMode(confirmMode['Video'])
        # steps 3
        sm.switchCaptureMode('Single')  # change camera mode
        time.sleep(1)
        tb.confirmCameraMode(confirmMode['Single'])

# Test case 2
    def testQuickSwitchtoHDRmode(self):
        """
        Summary:testQuickSwitchtoHDRmode: Quick Switch to HDR mode
        Steps:  1.Launch HDR capture activity
                2.press change mode and then press Video icon to enter video
                3.press change mode icon then choose camera group  
        """
        # step 1  
        sm.switchCaptureMode('Single','HDR')    # change hdr mode
        time.sleep(1)
        tb.confirmCameraMode(confirmMode['Single'])
        # step 2
        sm.switchCaptureMode('Video')   # change video mode
        time.sleep(1)
        tb.confirmCameraMode(confirmMode['Video'])
        # step 3
        sm.switchCaptureMode('Single')     # change camera mode
        # check camera mode
        time.sleep(1)
        tb.confirmCameraMode(confirmMode['Single'])

# Test case 3
    def testQuickSwitchtoSmileCammode(self):
        """
        Summary:testQuickSwitchtoSmileCammode: Quick Switch to SmileCam mode
        Steps:  1.Launch SmileCam capture activity
                2.press change mode and then press Video icon to enter video
                3.press change mode icon then choose camera group  
        """  
        # step 1  
        sm.switchCaptureMode('Single','Smile')    # change smile mode
        time.sleep(1)
        tb.confirmCameraMode(confirmMode['Single'])
        # step 2
        sm.switchCaptureMode('Video')   # change video mode
        time.sleep(1)
        tb.confirmCameraMode(confirmMode['Video'])
        # step 3
        sm.switchCaptureMode('Single','Smile')     # change camera mod
        time.sleep(1)
        tb.confirmCameraMode(confirmMode['Single'])

# Test case 4
    def testQuickSwitchtoBurstmode(self):
        """
        Summary:testQuickSwitchtoBurstmode: Quick Switch to Burst mode
        Steps:  1.Launch Burst capture activity
                2.press change mode and then press panorama icon to enter panorama
                3.press change mode icon then choose Multi group  
        """  
        # step 1  
        sm.switchCaptureMode('Burst')    # change burst mode
        time.sleep(3)
        tb.confirmCameraMode(confirmMode['Burst'])
        # step 2
        sm.switchCaptureMode('Panorama')   # change panorama mode
        time.sleep(1)
        tb.confirmCameraMode(confirmMode['Panorama'])
        # step 3
        sm.switchCaptureMode('Burst')     # change burst mode
        time.sleep(1)
        tb.confirmCameraMode(confirmMode['Burst'])
        # check camera mode
        sm.switchCaptureMode('Single')
        time.sleep(1)
        tb.confirmCameraMode(confirmMode['Single'])

# Test case 5    
    def testQuickSwitchtoPerfectShotmode(self):
        """
        Summary:testQuickSwitchtoPerfectShotmode: Quick Switch to Perfect Shot mode 
        Steps:  1.Launch Perfect capture activity
                2.press change mode and then press panorama icon to enter panorama
                3.press change mode icon then choose Multi group  
        """ 
        # step 1
        sm.switchCaptureMode('Perfect Shot')    # change perfectshot mode
        time.sleep(1) 
        tb.confirmCameraMode(confirmMode['Perfect Shot'])
        # step 2
        sm.switchCaptureMode('Panorama')   # change panorama mode
        time.sleep(1)
        tb.confirmCameraMode(confirmMode['Panorama'])
        # step 3
        sm.switchCaptureMode('Perfect Shot')    # change perfectshot mode
        time.sleep(1)
        tb.confirmCameraMode(confirmMode['Perfect Shot'])

# Test case 6
    def testQuickSwitchtoGallery(self):
        """
        Summary:testQuickSwitchtoGallery: Quick Switch to gallery 
        Steps:  1. Launch camera 
                2. Touch shutter button to capture a picture
                3. Touch the thubnail icon to view it in gallery 
        """ 
        # step 2
        time.sleep(1)
        tb.captureAndCheckPicCount('single',2)  # capture picture
        time.sleep(1)                                    
        d(resourceId = 'com.intel.camera22:id/thumbnail').click.wait()   # enter gallery
        time.sleep(2)
        # step 2
        d.click(1200,800)
        time.sleep(1)
        assert d(resourceId = 'android:id/home').wait.exists(timeout = 3000)
