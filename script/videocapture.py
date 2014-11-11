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

AD          = util.Adb()
tb          = util.TouchButton()
so          = util.SetOption()
sm          = util.SetCaptureMode()
modeNumber  = util.ModeNumber['video']
confirmMode = util.ConfirmMode

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        AD.setUpDevice(False)
        sm.switchCaptureMode('Video')
        tb.confirmCameraMode(confirmMode['Video'])

    def tearDown(self):
        super(CameraTest,self).tearDown()
        AD.tearDownDevice()

    def testRecordVideoCaptureVideoWithBalanceAuto(self):
        '''
            Summary: Capture video with White Balance Auto
            Steps  :  
                1.Launch video activity
                2.Set White Balance Auto
                3.Touch shutter button to capture 30s video
                4.Exit  activity
        '''
        so.setCameraOption('White Balance','auto')
        tb.confirmSettingMode('White Balance','auto',modeNumber)
        tb.captureAndCheckPicCount('video',5)

    def testRecordVideoCaptureVideoWithBalanceIncandescent(self):
        '''
            Summary: Capture video with White Balance Incandescent
            Steps  :  
                1.Launch video activity
                2.Set White Balance Incandescent
                3.Touch shutter button to capture 30s video
                4.Exit  activity
        '''
        so.setCameraOption('White Balance','incandescent')
        tb.confirmSettingMode('White Balance','incandescent',modeNumber)
        tb.captureAndCheckPicCount('video',5)

    def testRecordVideoCaptureVideoWithBalanceDaylight(self):
        '''
            Summary: Capture video with White Balance Daylight
            Steps  :  
                1.Launch video activity
                2.Set White Balance Daylight
                3.Touch shutter button to capture 30s video
                4.Exit  activity
        '''

        so.setCameraOption('White Balance','daylight')
        tb.confirmSettingMode('White Balance','daylight',modeNumber)
        tb.captureAndCheckPicCount('video',5)

    def testRecordVideoCaptureVideoWithBalanceFluorescent(self):
        '''
            Summary: Capture video with White Balance Fluorescent
            Steps  :  
                1.Launch video activity
                2.Set White Balance Fluorescent
                3.Touch shutter button to capture 30s video
                4.Exit  activity
        '''

        so.setCameraOption('White Balance','fluorescent')
        tb.confirmSettingMode('White Balance','fluorescent',modeNumber)
        tb.captureAndCheckPicCount('video',5)

    def testRecordVideoCaptureVideoWithBalanceCloudy(self):
        '''
            Summary: Capture video with White Balance Cloudy
            Steps  :  
                1.Launch video activity
                2.Set White Balance Cloudy
                3.Touch shutter button to capture 30s video
                4.Exit  activity
        '''
        so.setCameraOption('White Balance','cloudy-daylight')
        tb.confirmSettingMode('White Balance','cloudy-daylight',modeNumber)
        tb.captureAndCheckPicCount('video',5)

    def testRecordVideoCaptureVideoWithExposureAuto(self):
        '''
            Summary: Capture video with Exposure auto
            Steps  :  
                1.Launch Video activity
                2.Touch Exposure Setting icon, set Exposure auto
                3.Touch shutter button
                4.Touch shutter button to capture picture
                5.Exit  activity
        '''
        so.setCameraOption('Exposure','0')
        tb.confirmSettingMode('Exposure','0',modeNumber)
        tb.captureAndCheckPicCount('video',5)

    def testRecordVideoCaptureVideoWithExposure1(self):
        '''
            Summary: Capture video with Exposure 1
            Steps  :  
                1.Launch Video activity
                2.Touch Exposure Setting icon, set Exposure 1
                3.Touch shutter button
                4.Touch shutter button to capture picture
                5.Exit  activity
        '''
        so.setCameraOption('Exposure','3')
        tb.confirmSettingMode('Exposure','3',modeNumber)
        tb.captureAndCheckPicCount('video',5)

    def testRecordVideoCaptureVideoWithExposure2(self):
        '''
            Summary: Capture video with Exposure 2
            Steps  :  
                1.Launch Video activity
                2.Touch Exposure Setting icon, set Exposure 2
                3.Touch shutter button
                4.Touch shutter button to capture picture
                5.Exit  activity
        '''
        so.setCameraOption('Exposure','6')
        tb.confirmSettingMode('Exposure','6',modeNumber)
        tb.captureAndCheckPicCount('video',5)

    def testRecordVideoCaptureVideoWithExposureRed1(self):
        '''
            Summary: Capture video with Exposure -1
            Steps  :  
                1.Launch Video activity
                2.Touch Exposure Setting icon, set Exposure -1
                3.Touch shutter button
                4.Touch shutter button to capture picture
                5.Exit  activity
        '''
        so.setCameraOption('Exposure','-3')
        tb.confirmSettingMode('Exposure','-3',modeNumber)
        tb.captureAndCheckPicCount('video',5)

    def testRecordVideoCaptureVideoWithExposureRed2(self):
        '''
            Summary: Capture video with Exposure -2
            Steps  :  
                1.Launch Video activity
                2.Touch Exposure Setting icon, set Exposure -2
                3.Touch shutter button
                4.Touch shutter button to capture picture
                5.Exit  activity
        '''
        so.setCameraOption('Exposure','-6')
        tb.confirmSettingMode('Exposure','-6',modeNumber)
        tb.captureAndCheckPicCount('video',5)

    def testRecordVideoCaptureVideoWithHSSize(self):
        '''
            Summary: Capture video with HS size
            Steps  :  
                1.Launch video activity
                2.Check video size ,set to HS
                3.Touch shutter button to capture 30s video
                4.Exit  activity 
        '''
        so.setCameraOption('Video Size',['true','5'])
        tb.confirmSettingMode('Video Size',['true','5'],modeNumber)
        tb.captureAndCheckPicCount('video',5)

    def testRecordVideoCaptureVideoWithHDSize(self):
        '''
            Summary: Capture video with HD size
            Steps  :  
                1.Launch video activity
                2.Check video size ,set to HD
                3.Touch shutter button to capture 30s video
                4.Exit  activity 
        '''
        so.setCameraOption('Video Size',['false','5'])
        tb.confirmSettingMode('Video Size',['false','5'],modeNumber)
        tb.captureAndCheckPicCount('video',5)

    def testRecordVideoCaptureVideoWithSDSize(self):
        '''
            Summary: Capture video with SD size
            Steps  :  
                1.Launch video activity
                2.Check video size ,set to SD
                3.Touch shutter button to capture 30s video
                4.Exit  activity 
        '''
        so.setCameraOption('Video Size',['false','4'])
        tb.confirmSettingMode('Video Size',['false','4'],modeNumber)
        tb.captureAndCheckPicCount('video',5)

    def testRecordVideoCaptureVideoWithFHDSize(self):
        '''
            Summary: Capture video with FHD size
            Steps  :  
                1.Launch video activity
                2.Check video size ,set to FHD
                3.Touch shutter button to capture 30s video
                4.Exit  activity 
        '''
        so.setCameraOption('Video Size',['false','6'])
        tb.confirmSettingMode('Video Size',['false','6'],modeNumber)
        tb.captureAndCheckPicCount('video',5)

    def testRecordVideoCaptureVideoWithFHSSize(self):
        '''
            Summary: Capture video with FHS size
            Steps  :  
                1.Launch video activity
                2.Check video size ,set to FHS
                3.Touch shutter button to capture 30s video
                4.Exit  activity 
        '''
        so.setCameraOption('Video Size',['true','6'])
        tb.confirmSettingMode('Video Size',['true','6'],modeNumber)
        tb.captureAndCheckPicCount('video',5)

    def testRecordVideoWithGeoLocationOn(self):
        '''
            Summary: Record an video in GeoLocation On
            Steps  :  
                1.Launch video activity
                2.Check geo-tag ,set to ON
                3.Touch shutter button to capture 30s video
                4.Exit  activity 
        '''
        so.setCameraOption('Geo Location','on')
        tb.confirmSettingMode('Geo Location','on',modeNumber)
        tb.captureAndCheckPicCount('video',5)

    def testRecordVideoWithGeoLocationOff(self):
        '''
            Summary: Record an video in GeoLocation Off
            Steps  :  
                1.Launch video activity
                2.Check geo-tag ,set to Off
                3.Touch shutter button to capture 30s video
                4.Exit  activity 
        '''
        so.setCameraOption('Geo Location','off')
        tb.confirmSettingMode('Geo Location','off',modeNumber)
        tb.captureAndCheckPicCount('video',5)
