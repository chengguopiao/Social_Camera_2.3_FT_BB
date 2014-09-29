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

a  = util.Adb()
sm = util.SetCaptureMode()
so = util.SetOption()
tb = util.TouchButton()

#Written by XuGuanjun

PACKAGE_NAME  = 'com.intel.camera22'
ACTIVITY_NAME = PACKAGE_NAME + '/.Camera'

#All setting info of camera could be cat in the folder
PATH_XML       = '/data/data/com.intel.camera22/shared_prefs/'

#FDFR / GEO / BACK&FROUNT xml file in com.intelcamera22_preferences_0.xml
PATH_0XML      = PATH_XML + 'com.intel.camera22_preferences_0.xml'

#PICSIZE / EXPROSURE / TIMER / WHITEBALANCE / ISO / HITS / VIDEOSIZE in com.intel.camera22_preferences_0_0.xml
PATH_0_0XML    = PATH_XML + 'com.intel.camera22_preferences_0_0.xml'

#####                                    #####
#### Below is the specific settings' info ####
###                                        ###
##                                          ##
#                                            #

#FD/FR states check point
FDFR_STATE      = PATH_0XML   + ' | grep pref_fdfr_key'

#Geo state check point
GEO_STATE       = PATH_0XML   + ' | grep pref_camera_geo_location_key'

#Pic size state check point
PICSIZE_STATE   = PATH_0_0XML + ' | grep pref_camera_picture_size_key'

#Exposure state check point 
EXPOSURE_STATE  = PATH_0_0XML + ' | grep pref_camera_exposure_key'

#Timer state check point
TIMER_STATE     = PATH_0_0XML + ' | grep pref_camera_delay_shooting_key'

#Video Size state check point
VIDEOSIZE_STATE = PATH_0_0XML + ' | grep pref_video_quality_key'

#White balance state check point
WBALANCE_STATE  = PATH_0_0XML + ' | grep pref_camera_whitebalance_key'

#SCENE state check point
SCENE_STATE     = PATH_0_0XML + ' | grep pref_camera_scenemode_key'

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        #Delete all image/video files captured before
        a.cmd('rm','/sdcard/DCIM/*')
        #Refresh media after delete files
        a.cmd('refresh','/sdcard/DCIM/*')
        #Launch social camera
        self._launchCamera()
        sm.switchCaptureMode('Single','HDR')

    def tearDown(self):
    	a.cmd('pm','com.intel.camera22') #Force reset the camera settings to default
        super(CameraTest,self).tearDown()
        self._pressBack(4)

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
        tb.captureAndCheckPicCount('single',3)

    def testCapturePictureWithFiveSec(self):
        """
        Summary: Capture image with Self-timer 5s
        Steps  :  1.Launch HDR capture activity
                2.Set Self-timer 5s
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('Self Timer','5')
        tb.captureAndCheckPicCount('single',5)

    def testCapturePictureWithTenSec(self):
        """
        Summary: Capture image with Self-timer 10s
        Steps  :  1.Launch HDR capture activity
                2.Set Self-timer 10s
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        so.setCameraOption('Self Timer','10')
        tb.captureAndCheckPicCount('single',10)

    def _launchCamera(self):
        d.start_activity(component = ACTIVITY_NAME)
        #When it is the first time to launch camera there will be a dialog to ask user 'remember location', so need to check
        if d(text = 'Skip').wait.exists(timeout = 3000):
            d(text = 'Skip').click.wait()          
        try:
            assert d(text = 'OK').wait.exists(timeout = 2000)
            d(text = 'OK').click.wait()
            
        except:
            pass
        assert d(resourceId = 'com.intel.camera22:id/mode_button').wait.exists(timeout = 3000), 'Launch camera failed in 3s'

    def _pressBack(self,touchtimes):
        for i in range(0,touchtimes):
            d.press('back')
