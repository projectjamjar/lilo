__author__ = 'JamJar'
from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
import argparse
import os

import lilo_config as config

class Lilo():
    """
    The class for JamJar which will be used to identify video matches and add fingerprints to the database
    """

    def __init__(self, filename, video_id):
        """
        usage:
            fingerprinter = Lilo('/path/to/video/file','unique_video_id')
        """
        self.djv = Dejavu(config.config)
        self.filename = filename
        self.video_id = video_id

        # self.recognize_track()
        # self.fingerprint_song()

    def recognize_track(self):
        # Try to match the song to the existing database
        songs = self.djv.recognize(FileRecognizer, self.filename)

        return songs

    def fingerprint_song(self):
        # Now let's add this song to the DB
        self.djv.fingerprint_file(self.filename, song_name=self.video_id)