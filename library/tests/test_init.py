# noqa D100
import sys
import mock


def test_st7567_init():
    """Test that the ST7567 initialises correctly."""
    from tools import GPIO
    gpio = GPIO()
    sys.modules['RPi'] = mock.Mock()
    sys.modules['RPi'].GPIO = gpio
    sys.modules['RPi.GPIO'] = gpio
    sys.modules['spidev'] = mock.MagicMock()
    from gfxhat import lcd
    lcd.st7567.setup()

    assert gpio.pin_modes[5] == gpio.OUT
    assert gpio.pin_modes[6] == gpio.OUT
