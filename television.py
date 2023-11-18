class Television:
    """Class that represents Television"""

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Creates TV object with default values"""

        self.status: bool = False
        self.muted: bool = False
        self.volume: int = self.MIN_VOLUME
        self.channel: int = self.MIN_CHANNEL
        self.saved_volume: None = None  # added this instance variable to remember the volume while muted

    def power(self) -> bool:
        """This method toggles the tv on or off"""

        self.status = not self.status
        return self.status

    def mute(self) -> None:
        """This method mutes or unmutes the tv"""

        if self.status:
            if not self.muted:
                self.saved_volume = self.volume
                self.volume = self.MIN_VOLUME
            else:
                if self.saved_volume is not None:
                    self.volume = self.saved_volume

            self.muted = not self.muted

    def channel_up(self) -> int:
        """Increases the channel on the TV"""

        if self.status:
            if self.channel < self.MAX_CHANNEL:
                self.channel += 1
                return self.channel
            else:
                self.channel = self.MIN_CHANNEL
                return self.channel

    def channel_down(self) -> int:
        """Decreases the channel on the TV"""

        if self.status:
            if self.channel > self.MIN_CHANNEL:
                self.channel -= 1
                return self.channel
            else:
                self.channel = self.MAX_CHANNEL
                return self.channel

    def volume_up(self) -> int:
        """Increases the volume on the TV"""

        if self.status:
            if self.muted:
                self.mute()
            if self.volume < self.MAX_VOLUME:
                self.volume += 1
                return self.volume

    def volume_down(self) -> int:
        """Decreases the volume on the TV"""

        if self.status:
            if self.muted:
                self.mute()
            if self.volume > self.MIN_VOLUME:
                self.volume -= 1
                return self.volume

    def __str__(self) -> str:
        """Returns and prints the status of a TV object's Power, Channel, and Volume"""

        return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}'
