#!/usr/bin/env python
#from uiautomatorplug.android import device as d
from uiautomatorplug.android import device as d
import time
import unittest
import commands
import util
import string

a           = util.Adb()
sm          = util.SetCaptureMode()
so          = util.SetOption()
tb          = util.TouchButton()
confirmMode = util.ConfirmMode

class CameraTest(unittest.TestCase):

    def setUp(self):
        super(CameraTest,self).setUp()
        a.setUpDevice()
        sm.switchCaptureMode('Single')
        #tb.confirmCameraMode(confirmMode['Single'])

    def tearDown(self):
        super(CameraTest,self).tearDown()
        a.tearDownDevice()


    # Testcase 1
    # def testCaptureSingleImageWithFlashOn(self):
    #     """
    #     Summary:Capture image with Flash ON.
    #     Step:
    #     1.Launch single capture activity
    #     2.Set flash ON
    #     3.Touch shutter button to capture picture
    #     4.Exit  activity
    #     """
    #     # Step 2 Set flash ON
    #     so.setCameraOption('')
    #     self._confirmSettingMode('flash','on')
    #     # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
    #     tb.captureAndCheckPicCount('single')

    # # Testcase 2
    # def testCaptureSingleImageWithFlashOff(self):
    #     """
    #     Summary:Capture image with Flash OFF.
    #     Step:
    #     1.Launch single capture activity
    #     2.Set flash OFF
    #     3.Touch shutter button to capture picture
    #     4.Exit  activity
    #     """
    #     # Step 2 Set flash OFF
    #     SM.setCameraSetting('single','flash','off')
    #     self._confirmSettingMode('flash','off')
    #     # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
    #     tb.captureAndCheckPicCount('single')

    # # Testcase 3
    # def testCaptureSingleImageWithFlashAuto(self):
    #     """
    #     Summary:Capture image with Flash AUTO.
    #     Step:
    #     1.Launch single capture activity
    #     2.Set flash to AUTO mode
    #     3.Touch shutter button to capture picture
    #     4.Exit  activity
    #     """
    #     # Step 2 Set flash AUTO
    #     SM.setCameraSetting('single','flash','auto')
    #     self._confirmSettingMode('flash','auto')
    #     # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
    #     tb.captureAndCheckPicCount('single')

    # Testcase 4
    def testCaptureSingleImageWithExposureAuto(self):
        """
        Summary:Capture image with Exposure auto.
        Step:
        1.Launch single capture activity
        2.Set exposure auto
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set exposure auto
        so.setCameraOption('Exposure','0')
        #tb.confirmSettingMode('Exposure','0')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 5
    def testCaptureSingleImageWithExposurePlusOne(self):
        """
        Summary:Capture image with Exposure 1.
        Step:
        1.Launch single capture activity
        2.Set exposure 1
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set exposure 1
        so.setCameraOption('Exposure','3')
        #tb.confirmSettingMode('Exposure','3')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 6
    def testCaptureSingleImageWithExposurePlusTwo(self):
        """
        Summary:Capture image with Exposure 2.
        Step:
        1.Launch single capture activity
        2.Set exposure 2
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set exposure 2
        so.setCameraOption('Exposure','6')
        #tb.confirmSettingMode('Exposure','6')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 7
    def testCaptureSingleImageWithExposureRedOne(self):
        """
        Summary:Capture image with Exposure -1.
        Step:
        1.Launch single capture activity
        2.Set exposure -1
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set exposure -1
        so.setCameraOption('Exposure','-3')
        #tb.confirmSettingMode('Exposure','-3')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 8
    def testCaptureSingleImageWithExposureRedTwo(self):
        """
        Summary:Capture image with Exposure -2.
        Step:
        1.Launch single capture activity
        2.Set exposure -2
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set exposure -2
        so.setCameraOption('Exposure','-6')
        #tb.confirmSettingMode('Exposure','-6')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 9
    def testCaptureSingleImageWithSceneAuto(self):
        """
        Summary:Capture image with Scene mode AUTO.
        Step:
        1.Launch single capture activity
        2.Set scene mode AUTO
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set scene mode AUTO
        so.setCameraOption('Scenes','auto')
        #tb.confirmSettingMode('Scenes','auto')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 10
    def testCaptureSingleImageWithSceneSports(self):
        """
        Summary:Capture image with Scene mode Sports.
        Step:
        1.Launch single capture activity
        2.Set scene mode Sports
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set scene mode Sports
        so.setCameraOption('Scenes','sports')
        #tb.confirmSettingMode('Scenes','sports')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 11
    def testCaptureSingleImageWithSceneNight(self):
        """
        Summary:Capture image with Scene mode Night.
        Step:
        1.Launch single capture activity
        2.Set scene mode Night
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set scene mode Night
        so.setCameraOption('Scenes','night')
        #tb.confirmSettingMode('Scenes','night')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 12
    def testCaptureSingleImageWithSceneLandscape(self):
        """
        Summary:Capture image with Scene mode Landscape.
        Step:
        1.Launch single capture activity
        2.Set scene mode Landscape
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set scene mode Landscape
        so.setCameraOption('Scenes','landscape')
        #tb.confirmSettingMode('Scenes','landscape')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 13
    def testCaptureSingleImageWithScenePortrait(self):
        """
        Summary:Capture image with Scene mode Portrait.
        Step:
        1.Launch single capture activity
        2.Set scene mode Portrait
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set scene mode Portrait
        so.setCameraOption('Scenes','portrait')
        #tb.confirmSettingMode('Scenes','portrait')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 14
    #def testCaptureSingleImageWithSceneNightPortrait(self):
        """
        Summary:Capture image with Scene mode NightPortrait.
        Step:
        1.Launch single capture activity
        2.Set scene mode NightPortrait
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set scene mode NightPortrait
     #   so.setCameraOption('Scenes','night-portrait')
        #tb.confirmSettingMode('scenemode','night-portrait')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
    #    tb.captureAndCheckPicCount('single')

    # # Testcase 15
    # def testCaptureSingleImageWithSceneBarcode(self):
    #     """
    #     Summary:Capture image with Scene mode barcode.
    #     Step:
    #     1.Launch single capture activity
    #     2.Set scene mode barcode
    #     3.Touch shutter button to capture picture
    #     4.Exit  activity
    #     """
    #     # Step 2  Set scene mode barcode
    #     so.setCameraOption('Scenes','barcode')
    #     #tb.confirmSettingMode('scenemode','night-portrait')
    #     # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
    #     tb.captureAndCheckPicCount('single')

    # Testcase 16
    def testCaptureSingleImageWithFDFROn(self):
        """
        Summary:Capture image with FD/FR ON.
        Step:
        1.Launch single capture activity
        2.Set FD/FR ON
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set FD/FR ON, confirm fdfr is 'on'.
        so.setCameraOption('Face Detection','on')
        #tb.confirmSettingMode('Face Detection','on')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 17
    def testCaptureSingleImageWithFDFROff(self):
        """
        Summary:Capture image with FD/FR Off.
        Step:
        1.Launch single capture activity
        2.Set FD/FR Off
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set FD/FR Off, confirm fdfr is 'off'
        so.setCameraOption('Face Detection','off')
        #tb.confirmSettingMode('Face Detection','off')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 18
    def testCaptureSingleImageWithPictureSizeWidescreen(self):
        """
        Summary:Capture image with Photo size 6M.
        Step:
        1.Launch single capture activity
        2.Set photo size 6M
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set photo size 6M
        so.setCameraOption('Picture Size','WideScreen')
        #tb.confirmSettingMode('Picture Size','WideScreen')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 19
    def testCaptureSingleImageWithPictureSizeStandardScreen(self):
        """
        Summary:Capture image with Scene mode barcode.
        Step:
        1.Launch single capture activity
        2.Set photo size 13M
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set photo size 13M
        so.setCameraOption('Picture Size','StandardScreen')
        #tb.confirmSettingMode('Picture Size','StandardScreen')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 20
    def testCaptureSingleImageWithHitsOn(self):
        """
        Summary:Capture image with Hints ON.
        Step:
        1.Launch single capture activity
        2.Set Hints ON
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set Hints ON
        so.setCameraOption('Hints','on')
        #tb.confirmSettingMode('Hints','on')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 21
    def testCaptureSingleImageWithHitsOff(self):
        """
        Summary:Capture image with Hints OFF.
        Step:
        1.Launch single capture activity
        2.Set Hints OFF
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set Hints OFF
        so.setCameraOption('Hints','off')
        #tb.confirmSettingMode('Hints','off')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 22
    def testCaptureSingleImageWithSelfTimerOff(self):
        """
        Summary:Capture image with Self-timer off.
        Step:
        1.Launch single capture activity
        2.Set Self-timer off
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set Self-timer off
        so.setCameraOption('Self Timer','0')
        #tb.confirmSettingMode('Self Timer','0')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 23
    def testCaptureSingleImageWithSelfTimerThree(self):
        """
        Summary:Capture image with Self-timer 3s.
        Step:
        1.Launch single capture activity
        2.Set Self-timer 3s
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set Self-timer 3s
        so.setCameraOption('Self Timer','3')
        #tb.confirmSettingMode('Self Timer','3')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',5)

    # Testcase 24
    def testCaptureSingleImageWithSelfTimerFive(self):
        """
        Summary:Capture image with Self-timer 5s.
        Step:
        1.Launch single capture activity
        2.Set Self-timer 5s
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set Self-timer 5s
        so.setCameraOption('Self Timer','5')
        #tb.confirmSettingMode('Self Timer','5')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',7)

    # Testcase 25
    def testCaptureSingleImageWithSelfTimerTen(self):
        """
        Summary:Capture image with Self-timer 10s.
        Step:
        1.Launch single capture activity
        2.Set Self-timer 10s
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set Self-timer 10s
        so.setCameraOption('Self Timer','10')
        #tb.confirmSettingMode('Self Timer','10')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',12)

    # Testcase 26
    def testCaptureSingleImageWithISOAuto(self):
        """
        Summary:Capture image with ISO Setting Auto.
        Step:
        1.Launch single capture activity
        2.Set ISO Setting Auto
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set ISO Setting Auto
        so.setCameraOption('ISO','iso-auto')
        #tb.confirmSettingMode('ISO','iso-auto')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 27
    def testCaptureSingleImageWithISOOneH(self):
        """
        Summary:Capture image with ISO Setting 100.
        Step:
        1.Launch single capture activity
        2.Set ISO Setting 100
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set ISO Setting 100
        so.setCameraOption('ISO','iso-100')
        #tb.confirmSettingMode('ISO','iso-100')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 28
    def testCaptureSingleImageWithISOTwoH(self):
        """
        Summary:Capture image with ISO Setting 200.
        Step:
        1.Launch single capture activity
        2.Set ISO Setting 200
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set ISO Setting 200
        so.setCameraOption('ISO','iso-200')
        #tb.confirmSettingMode('ISO','iso-200')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 29
    def testCaptureSingleImageWithISOFourH(self):
        """
        Summary:Capture image with ISO Setting 400.
        Step:
        1.Launch single capture activity
        2.Set ISO Setting 400
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set ISO Setting 400
        so.setCameraOption('ISO','iso-400')
        #tb.confirmSettingMode('ISO','iso-400')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 30
    def testCaptureSingleImageWithISOEightH(self):
        """
        Summary:Capture image with ISO Setting 800.
        Step:
        1.Launch single capture activity
        2.Set ISO Setting 800
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set ISO Setting 800
        so.setCameraOption('ISO','iso-800')
        #tb.confirmSettingMode('ISO','iso-800')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 31
    def testCaptureSingleImageWithWBAuto(self):
        """
        Summary:Capture image with White Balance Auto.
        Step:
        1.Launch single capture activity
        2.Set White Balance Auto
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Capture image with White Balance Auto.
        so.setCameraOption('White Balance','auto')
        #tb.confirmSettingMode('White Balance','auto')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 32
    def testCaptureSingleImageWithWBIncandescent(self):
        """
        Summary:Capture image with White Balance Incandescent.
        Step:
        1.Launch single capture activity
        2.Set White Balance Incandescent
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Capture image with White Balance Incandescent.
        so.setCameraOption('White Balance','incandescent')
        #tb.confirmSettingMode('White Balance','incandescent')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 33
    def testCaptureSingleImageWithWBDaylight(self):
        """
        Summary:Capture image with White Balance Daylight.
        Step:
        1.Launch single capture activity
        2.Set White Balance Daylight
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Capture image with White Balance Daylight.
        so.setCameraOption('White Balance','daylight')
        #tb.confirmSettingMode('White Balance','daylight')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single')

    # Testcase 34
    def testCaptureSingleImageWithWBFluorescent(self):
        """
        Summary:Capture image with White Balance Fluorescent.
        Step:
        1.Launch single capture activity
        2.Set White Balance Fluorescent
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Capture image with White Balance Fluorescent.
        so.setCameraOption('White Balance','fluorescent')
        #tb.confirmSettingMode('White Balance','fluorescent')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)  

    # Testcase 35
    def testCaptureSingleImageWithWBCloudy(self):
        """
        Summary:Capture image with White Balance Cloudy.
        Step:
        1.Launch single capture activity
        2.Set White Balance Cloudy
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Capture image with White Balance Cloudy.
        so.setCameraOption('White Balance','cloudy-daylight')
        #tb.confirmSettingMode('White Balance','cloudy-daylight')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)  

    # Testcase 36
    def testCaptureSingleImageWithLocationOn(self):
        """
        Summary:Capture image with Geo location on.
        Step:
        1.Launch single capture activity
        2.Set location on.
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 
        so.setCameraOption('Geo Location','on')
        #tb.confirmSettingMode('Geo Location','on')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 37
    def testCaptureSingleImageWithLocationOff(self):
        """
        Summary:Capture image with Geo location off.
        Step:
        1.Launch single capture activity
        2.Set location off.
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 
        so.setCameraOption('Geo Location','off')
        #tb.confirmSettingMode('Geo Location','off')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single',2)

    # Testcase 38
    def testFrontCaptureSingleImageWithLocationOn(self):
        """
        Summary:Capture image with Geo location on front camera.
        Step:
        1.Launch single capture activity
        3.Switch to front camera
        3.Set location on.
        4.Touch shutter button to capture picture
        5.Exit  activity
        """
        # Step 2 Switch to front camera and confirm with the xml file.
        so.setCameraOption('Switch Camera','1')
        #tb.confirmSettingMode('Switch Camera','1')
        # Step 3
        so.setCameraOption('Geo Location','on')
        #tb.confirmSettingMode('Geo Location','on')
        # Step 4 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single')

    # Testcase 39
    def testFrontCaptureSingleImageWithLocationOff(self):
        """
        Summary:Capture image with Geo location off front camera.
        Step:
        1.Launch single capture activity
        3.Switch to front camera
        3.Set location off.
        4.Touch shutter button to capture picture
        5.Exit  activity
        """
        # Step 2 Switch to front camera and confirm with the xml file.
        so.setCameraOption('Switch Camera','1')
        #tb.confirmSettingMode('Switch Camera','1')
        # Step 3
        so.setCameraOption('Geo Location','off')
       # tb.confirmSettingMode('Geo Location','off')
        # Step 4 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single')

    # Testcase 40
    def testFrontCaptureSingleImageWithFDFROn(self):
        """
        Summary:Capture image with FD/FR on front camera.
        Step:
        1.Launch single capture activity
        3.Switch to front camera
        3.Set FD/FR on.
        4.Touch shutter button to capture picture
        5.Exit  activity
        """
        # Step 2 Switch to front camera and confirm with the xml file.
        so.setCameraOption('Switch Camera','1')
       # tb.confirmSettingMode('Switch Camera','1')
        # Step 3
        so.setCameraOption('Face Detection','on')
        #tb.confirmSettingMode('Face Detection','on')
        # Step 4 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single')

    # Testcase 41
    def testFrontCaptureSingleImageWithFDFROff(self):
        """
        Summary:Capture image with FD/FR off front camera.
        Step:
        1.Launch single capture activity
        3.Switch to front camera
        3.Set FD/FR off.
        4.Touch shutter button to capture picture
        5.Exit  activity
        """
        # Step 2 Switch to front camera and confirm with the xml file.
        so.setCameraOption('Switch Camera','1')
        #tb.confirmSettingMode('Switch Camera','1')
        # Step 3
        so.setCameraOption('Face Detection','off')
        #tb.confirmSettingMode('Face Detection','off')
        # Step 4 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('single')
        
    # Testcase 42
    def testSwitchDepthModeAndSingleMode(self):
        """
        Summary:Switch Depth Mode And Single Mode.
        Step:
        1.Launch single capture activity
        3.Switch to depth mode with single mode
        """
        sm.switchCaptureMode('Depth Snapshot')
        time.sleep(5)
        tb.captureAndCheckPicCount('single') 
        time.sleep(1)
        sm.switchCaptureMode('Single')
        time.sleep(5)
        tb.captureAndCheckPicCount('single')
        time.sleep(1)
        sm.switchCaptureMode('Depth Snapshot')
        time.sleep(5)
        tb.captureAndCheckPicCount('single')                    
        
        
    # Testcase 43
    def testSwitchDepthModeCapture(self):
        """
        Summary:Capture image depth mode .
        Step:
        1.Launch single capture activity
        3.Switch to depth mode.
        3.capture image.
        """
        sm.switchCaptureMode('Depth Snapshot')
        time.sleep(10)
        tb.captureAndCheckPicCount('single')        
