import pytest
from television import *


def test_init_values():
    tv = Television()

    assert tv.status is False
    assert tv.muted is False
    assert tv.volume == Television.MIN_VOLUME
    assert tv.saved_volume is None
    assert tv.channel == Television.MIN_CHANNEL

def test_power():
    tv1 = Television()
    tv1.power()
    tv1_details = str(tv1)
    assert "Power = True, Channel = 0, Volume = 0" in tv1_details

    tv2 = Television()
    tv2_details = str(tv2)
    assert "Power = False, Channel = 0, Volume = 0" in tv2_details



def test_mute():

    tv1 = Television()
    tv1.power()
    tv1.volume_up()
    tv1.mute()
    tv1_details = str(tv1)
    assert "Power = True, Channel = 0, Volume = 0" in tv1_details

    tv2 = Television()
    tv2.power()
    tv2.mute()
    tv2.mute()
    tv2_details = str(tv2)
    assert "Power = True, Channel = 0, Volume = 0" in tv2_details

    tv3 = Television()
    tv3.mute()
    tv3_details = str(tv3)
    assert "Power = False, Channel = 0, Volume = 0" in tv3_details

    tv4 = Television()
    tv4.mute()
    tv4.mute()
    tv4_details = str(tv4)
    assert "Power = False, Channel = 0, Volume = 0" in tv4_details


def test_channel_up():
    tv1 = Television()
    tv1.channel_up()
    tv1_details = str(tv1)
    assert "Power = False, Channel = 0, Volume = 0" in tv1_details

    tv2 = Television()
    tv2.power()
    tv2.channel_up()
    tv2_details = str(tv2)
    assert "Power = True, Channel = 1, Volume = 0" in tv2_details

    tv3 = Television()
    tv3.power()
    tv3.channel_up()
    tv3.channel_up()
    tv3.channel_up()
    tv3.channel_up()
    tv3_details = str(tv3)
    assert "Power = True, Channel = 0, Volume = 0" in tv3_details



def test_channel_down():
    tv1 = Television()
    tv1.channel_down()
    tv1_details = str(tv1)
    assert "Power = False, Channel = 0, Volume = 0" in tv1_details

    tv2 = Television()
    tv2.power()
    tv2.channel_down()
    tv2_details = str(tv2)
    assert "Power = True, Channel = 3, Volume = 0" in tv2_details


def test_volume_up():
    tv1 = Television()
    tv1.volume_up()
    tv1_details = str(tv1)
    assert "Power = False, Channel = 0, Volume = 0" in tv1_details

    tv2 = Television()
    tv2.power()
    tv2.volume_up()
    tv2_details = str(tv2)
    assert "Power = True, Channel = 0, Volume = 1" in tv2_details

    tv3 = Television()
    tv3.power()
    tv3.mute()
    tv3.volume_up()
    tv3_details = str(tv3)
    assert "Power = True, Channel = 0, Volume = 1" in tv3_details

    tv4 = Television()
    tv4.power()
    tv4.volume_up()
    tv4.volume_up()
    tv4.volume_up()
    tv4_details = str(tv4)
    assert "Power = True, Channel = 0, Volume = 2" in tv4_details


def test_volume_down():
    tv1 = Television()
    tv1.volume_down()
    tv1_details = str(tv1)
    assert "Power = False, Channel = 0, Volume = 0" in tv1_details

    tv2 = Television()
    tv2.power()
    tv2.volume_up()
    tv2.volume_up()
    tv2.volume_down()
    tv2_details = str(tv2)
    assert "Power = True, Channel = 0, Volume = 1" in tv2_details

    tv3 = Television()
    tv3.power()
    tv3.volume_up()
    tv3.volume_up()
    tv3.mute()
    tv3.volume_down()
    tv3_details = str(tv3)
    assert "Power = True, Channel = 0, Volume = 1" in tv3_details

    tv4 = Television()
    tv4.power()
    tv4.volume_down()
    tv4_details = str(tv4)
    assert "Power = True, Channel = 0, Volume = 0" in tv4_details


