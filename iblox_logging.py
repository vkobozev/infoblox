import sys
import logging
import logging.handlers

# define log name
log_filename = "/var/log/iblox.log"

# define log format
fmt = logging.Formatter('%(asctime)s %(levelname)s %(filename)s: %(message)s', datefmt='%a %b %d %Y %I:%M:%S%p')

# create log handler with rotation by time. Rotation every week on Sunday. Storing info for 4 weeks.
file_timed_rotation_handler = logging.handlers.TimedRotatingFileHandler(log_filename,
                                                                        when='W6',
                                                                        backupCount=4)
file_timed_rotation_handler.setFormatter(fmt)
file_timed_rotation_handler.setLevel("DEBUG")

# create log handler to print output to std.out when script is running
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setFormatter(fmt)
stdout_handler.setLevel("INFO")

# create log instance
log = logging.getLogger("iblox")
log.addHandler(file_timed_rotation_handler)
log.addHandler(stdout_handler)

