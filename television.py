
class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = self.MIN_VOLUME
        self.channel = self.MIN_CHANNEL
        self.saved_volume = None

    def power(self):
        self.status = not self.status
        return self.status

    def mute(self):
        if self.status:
            if not self.muted:
                self.saved_volume = self.volume
                self.volume = self.MIN_VOLUME
            else:
                if self.saved_volume is not None:
                    self.volume = self.saved_volume

            self.muted = not self.muted

    def channel_up(self):
        if self.status:
            if self.channel < self.MAX_CHANNEL:
                self.channel += 1
                return self.channel
            else:
                self.channel = self.MIN_CHANNEL
                return self.channel

    def channel_down(self):
        if self.status:
            if self.channel > self.MIN_CHANNEL:
                self.channel -= 1
                return self.channel
            else:
                self.channel = self.MAX_CHANNEL
                return self.channel

    def volume_up(self):
        if self.status:
            if self.muted:
                self.mute()
            if self.volume < self.MAX_VOLUME:
                self.volume += 1
                return self.volume

    def volume_down(self):
        if self.status:
            if self.muted:
                self.mute()
            if self.volume > self.MIN_VOLUME:
                self.volume -= 1
                return self.volume

    def __str__(self):
        return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}'
