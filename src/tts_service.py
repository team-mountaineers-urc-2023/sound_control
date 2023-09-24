#! /usr/bin/env python3

import rospy
from sound_play.libsoundplay import SoundClient
from sound_control.srv import tts_srv, tts_srvRequest, tts_srvResponse

class TTS_node:
    def __init__(self) -> None:
        rospy.init_node('tts_node')  
        self.soundhandle = SoundClient()
        self.voice = 'voice_kal_diphone'
        # self.voice = 'voice_rab_diphone'
        # self.voice = 'voice_ked_diphone'
        # self.voice = 'voice_don_diphone'
        # self.voice = 'voice_el_diphone'
        # self.voice = 'voice_gsw_diphone'
        # self.voice = 'voice_en1_mbrola'
        # self.voice = 'voice_us1_mbrola'
        self.volume = 1.0
        self.tts_srv = rospy.Service("tts", tts_srv, self.tts_cb)
        rospy.spin()

    def tts_cb(self, msg: tts_srvRequest):
        self.soundhandle.say(msg.text, self.voice, self.volume)
        return tts_srvResponse

if __name__ == '__main__':
    tts_node = TTS_node()