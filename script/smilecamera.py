#!/usr/bin/env python
#from uiautomatorplug.android import device as d
from uiautomatorplug.android import device as d
import time
import unittest
import commands
import util
import string

a  = util.Adb()
sm = util.SetCaptureMode()
so = util.SetOption()
tb = util.TouchButton()


class CameraTest(unittest.TestCase):

    def setUp(self):
        super(CameraTest,self).setUp()
        # rm DCIM folder and refresh from adb shell
        a.cmd('rm','/sdcard/DCIM/100ANDRO')
        a.cmd('refresh','/sdcard/DCIM/100ANDRO')
        #Because default camera after launching is single mode, so we set this step in setUp().
        #Step 1. Launch single capture activity
        a.cmd('launch','com.intel.camera22/.Camera')
        time.sleep(2)
        if  d(text = 'OK').wait.exists(timeout = 3000):
            d(text = 'OK').click.wait()
        assert d(resourceId = 'com.intel.camera22:id/shutter_button'),'Launch camera failed!!'
        sm.switchCaptureMode('smile')

    def tearDown(self):
        super(CameraTest,self).tearDown()
        #4.Exit  activity
        self._pressBack(4)
        a.cmd('pm','com.intel.camera22')

    # # Testcase 1
    # def testCaptureSmileImageWithFlashOn(self):
    #     """
    #     Summary:Capture image with Flash ON.
    #     Step:
    #     1.Launch smile capture activity
    #     2.Set flash ON
    #     3.Touch shutter button to capture picture
    #     4.Exit  activity
    #     """
    #     # Step 2 Set flash ON
    #     SM.setCameraSetting('smile','flash','on')
    #     self._confirmSettingMode('flash','on')
    #     # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
    #     self._capturePictureAndConfirm(2)

    # # Testcase 2
    # def testCaptureSmileImageWithFlashOff(self):
    #     """
    #     Summary:Capture image with Flash OFF.
    #     Step:
    #     1.Launch smile capture activity
    #     2.Set flash OFF
    #     3.Touch shutter button to capture picture
    #     4.Exit  activity
    #     """
    #     # Step 2 Set flash OFF
    #     SM.setCameraSetting('smile','flash','off')
    #     self._confirmSettingMode('flash','off')
    #     # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
    #     self._capturePictureAndConfirm(2)

    # # Testcase 3
    # def testCaptureSmileImageWithFlashAuto(self):
    #     """
    #     Summary:Capture image with Flash AUTO.
    #     Step:
    #     1.Launch smile capture activity
    #     2.Set flash to AUTO mode
    #     3.Touch shutter button to capture picture
    #     4.Exit  activity
    #     """
    #     # Step 2 Set flash AUTO
    #     SM.setCameraSetting('smile','flash','auto')
    #     self._confirmSettingMode('flash','auto')
    #     # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
    #     self._capturePictureAndConfirm(2)

    # Testcase 4
    def testCaptureSmileImageWithExposureAuto(self):
        """
        Summary:Capture image with Exposure auto.
        Step:
        1.Launch smile capture activity
        2.Set exposure auto
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set exposure auto
        so.setCameraOption('Exposure','0')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 5
    def testCaptureSmileImageWithExposurePlusOne(self):
        """
        Summary:Capture image with Exposure 1.
        Step:
        1.Launch smile capture activity
        2.Set exposure 1
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set exposure 1
        so.setCameraOption('Exposure','3')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 6
    def testCaptureSmileImageWithExposurePlusTwo(self):
        """
        Summary:Capture image with Exposure 2.
        Step:
        1.Launch smile capture activity
        2.Set exposure 2
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set exposure 2
        so.setCameraOption('Exposure','6')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 7
    def testCaptureSmileImageWithExposureRedOne(self):
        """
        Summary:Capture image with Exposure -1.
        Step:
        1.Launch smile capture activity
        2.Set exposure -1
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set exposure -1
        so.setCameraOption('Exposure','-3')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 8
    def testCaptureSmileImageWithExposureRedTwo(self):
        """
        Summary:Capture image with Exposure -2.
        Step:
        1.Launch smile capture activity
        2.Set exposure -2
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set exposure -2
        so.setCameraOption('Exposure','-6')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 9
    def testCaptureSmileImageWithSceneAuto(self):
        """
        Summary:Capture image with Scene mode AUTO.
        Step:
        1.Launch smile capture activity
        2.Set scene mode AUTO
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set Set scene mode auto
        so.setCameraOption('Scenes','auto')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 10
    def testCaptureSmileImageWithSceneSports(self):
        """
        Summary:Capture image with Scene mode Sports.
        Step:
        1.Launch smile capture activity
        2.Set scene mode Sports
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set scene mode Sports
        so.setCameraOption('Scenes','sports')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 11
    def testCaptureSmileImageWithSceneNight(self):
        """
        Summary:Capture image with Scene mode Night.
        Step:
        1.Launch smile capture activity
        2.Set scene mode Night
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set scene mode Night
        so.setCameraOption('Scenes','night')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 12
    def testCaptureSmileImageWithSceneLandscape(self):
        """
        Summary:Capture image with Scene mode Landscape.
        Step:
        1.Launch smile capture activity
        2.Set scene mode Landscape
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set scene mode Landscape
        so.setCameraOption('Scenes','landscape')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 13
    def testCaptureSmileImageWithScenePortrait(self):
        """
        Summary:Capture image with Scene mode Portrait.
        Step:
        1.Launch smile capture activity
        2.Set scene mode Portrait
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set scene mode Portrait
        so.setCameraOption('Scenes','portrait')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 14
    def testCaptureSmileImageWithSceneNightPortrait(self):
        """
        Summary:Capture image with Scene mode NightPortrait.
        Step:
        1.Launch smile capture activity
        2.Set scene mode NightPortrait
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set scene mode NightPortrait
        so.setCameraOption('Scenes','night-portrait')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # # Testcase 15
    # def testCaptureSmileImageWithSceneBarcode(self):
    #     """
    #     Summary:Capture image with Scene mode barcode.
    #     Step:
    #     1.Launch smile capture activity
    #     2.Set scene mode barcode
    #     3.Touch shutter button to capture picture
    #     4.Exit  activity
    #     """
    #     # Step 2  Set scene mode barcode
    #     SM.setCameraSetting('smile',3,1)
    #     self._confirmSettingMode('scenemode','barcode')
    #     # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
    #     self._capturePictureAndConfirm(2)

    # Testcase 16
    def testCaptureSmileImageWithPictureSizeWidescreen(self):
        """
        Summary:Capture image with Photo size 6M.
        Step:
        1.Launch smile capture activity
        2.Set photo size 6M
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set photo size 6M
        so.setCameraOption('Picture Size','WideScreen')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 17
    def testCaptureSmileImageWithPictureSizeStandardScreen(self):
        """
        Summary:Capture image with Scene mode barcode.
        Step:
        1.Launch smile capture activity
        2.Set photo size 13M
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2  Set photo size 13M
        so.setCameraOption('Picture Size','StandardScreen')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 18
    def testCaptureSmileImageWithLocationOn(self):
        """
        Summary:Capture image with Geo-tag ON.
        Step:
        1.Launch smile capture activity
        2.Set Ge0-tag ON
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set Ge0-tag ON.
        so.setCameraOption('Geo Location','on')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 19
    def testCaptureSmileImageWithLocationOff(self):
        """
        Summary:Capture image with Geo-tag OFF by front Face camera.
        Step:
        1.Launch smile capture activity
        2.Set Ge0-tag OFF
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set Ge0-tag OFF.
        so.setCameraOption('Geo Location','off')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 20
    def testCaptureSmileImageWithISOAuto(self):
        """
        Summary:Capture image with ISO Setting Auto.
        Step:
        1.Launch smile capture activity
        2.Set ISO Setting Auto
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set ISO Setting Auto
        so.setCameraOption('ISO','iso-auto')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 21
    def testCaptureSmileImageWithISOOneH(self):
        """
        Summary:Capture image with ISO Setting 100.
        Step:
        1.Launch smile capture activity
        2.Set ISO Setting 100
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set ISO Setting 100
        so.setCameraOption('ISO','iso-100')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 22
    def testCaptureSmileImageWithISOTwoH(self):
        """
        Summary:Capture image with ISO Setting 200.
        Step:
        1.Launch smile capture activity
        2.Set ISO Setting 200
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set ISO Setting 200
        so.setCameraOption('ISO','iso-200')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 23
    def testCaptureSmileImageWithISOFourH(self):
        """
        Summary:Capture image with ISO Setting 400.
        Step:
        1.Launch smile capture activity
        2.Set ISO Setting 400
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set ISO Setting 400
        so.setCameraOption('ISO','iso-400')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 24
    def testCaptureSmileImageWithISOEightH(self):
        """
        Summary:Capture image with ISO Setting 800.
        Step:
        1.Launch smile capture activity
        2.Set ISO Setting 800
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Set ISO Setting 800
        so.setCameraOption('ISO','iso-800')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 25
    def testCaptureSmileImageWithWBAuto(self):
        """
        Summary:Capture image with White Balance Auto.
        Step:
        1.Launch smile capture activity
        2.Set White Balance Auto
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Capture image with White Balance Auto.
        so.setCameraOption('White Balance','auto')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 26
    def testCaptureSmileImageWithWBIncandescent(self):
        """
        Summary:Capture image with White Balance Incandescent.
        Step:
        1.Launch smile capture activity
        2.Set White Balance Incandescent
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Capture image with White Balance Incandescent.
        so.setCameraOption('White Balance','incandescent')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 27
    def testCaptureSmileImageWithWBDaylight(self):
        """
        Summary:Capture image with White Balance Daylight.
        Step:
        1.Launch smile capture activity
        2.Set White Balance Daylight
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Capture image with White Balance Daylight.
        so.setCameraOption('White Balance','daylight')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 28
    def testCaptureSmileImageWithWBFluorescent(self):
        """
        Summary:Capture image with White Balance Fluorescent.
        Step:
        1.Launch smile capture activity
        2.Set White Balance Fluorescent
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Capture image with White Balance Fluorescent.
        so.setCameraOption('White Balance','fluorescent')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    # Testcase 29
    def testCaptureSmileImageWithWBCloudy(self):
        """
        Summary:Capture image with White Balance Cloudy.
        Step:
        1.Launch smile capture activity
        2.Set White Balance Cloudy
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        # Step 2 Capture image with White Balance Cloudy.
        so.setCameraOption('White Balance','cloudy-daylight')
        # Step 3 Touch shutter button to capture picture and confirm picture count + 1.
        tb.captureAndCheckPicCount('smile')

    def _pressBack(self,touchtimes):
        for i in range(1,touchtimes+1):
            d.press('back')

    def _confirmSettingMode(self,sub_mode,option):
        if sub_mode == 'location':
            result = a.cmd('cat','/data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml | grep '+ sub_mode)
            if result.find(option) == -1:
                self.fail('set camera setting ' + sub_mode + ' to ' + option + ' failed')
        else:
            result = a.cmd('cat','/data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep ' + sub_mode)
            if result.find(option) == -1:
                self.fail('set camera setting ' + sub_mode + ' to ' + option + ' failed')

    def _capturePictureAndConfirm(self,timer=0):
        beforeC = a.cmd('ls','/sdcard/DCIM/100ANDRO')
        TB.takePicture('smile')
        time.sleep(timer)       
        afterC  = a.cmd('ls','/sdcard/DCIM/100ANDRO')
        if afterC == beforeC:
            self.fail('take picture failed !!')