__author__ = 'Mark'
from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
import argparse
import os
import pprint

from lilo import Lilo, lilo_config


def main():
    # Set up our commang line arguments
    parser = argparse.ArgumentParser(
        description="Take in a folder of video and/or audio files and fingerprint them into"
                    "the DB.")
    parser.add_argument("DIR", type=str,
                        help="The folder containing your audio and video files, relative to the current directory.")
    args = parser.parse_args()

    # Get the files in our folder
    dir = os.path.expanduser(args.DIR)
    files = os.listdir(dir)

    alignment_data = {}

    # Iterate through the files
    for index, filename in enumerate(files):
        full_path = os.path.join(dir, filename)

        # For now we'll assume all the files are valid audio or video
        if (os.path.isfile(full_path)):

            lilo = Lilo(lilo_config.config, full_path, filename)

            print "Adding {0} to database...".format(filename)

            # Now let's add this song to the DB
            lilo.fingerprint_song()

            print "Fingerprinting of {0} complete.".format(filename)

    pprint.pprint(alignment_data)


if __name__ == '__main__':
    main()
