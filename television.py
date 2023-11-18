

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

    def power(self):
        self.status = not self.status

    def mute(self):
        self.muted = not self.muted

    def channel_up(self):
        if self.status:
            if self.channel < self.MAX_CHANNEL:
                self.channel += 1
            else:
                self.channel = self.MIN_CHANNEL

    def channel_down(self):
        if self.status:
            if self.channel > self.MIN_CHANNEL:
                self.channel -= 1
            else:
                self.channel = self.MAX_CHANNEL

    def volume_up(self):
        if self.status:
            if self.volume < self.MAX_VOLUME:
                self.volume += 1
            else:
                self.volume = self.MAX_VOLUME

    def volume_down(self):
        if self.status:
            if self.volume > self.MIN_VOLUME:
                self.volume -= 1
            else:
                self.volume = self.MIN_VOLUME

    def __str__(self):
        return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}'
    

