# ------------------------------------------------------------------------------
# Standard Library Import
import  os

# ------------------------------------------------------------------------------
# Value Settings
WIDTH           = 640
HEIGHT          = 480

DATASET         = "dataset/"
FRAMES          = DATASET+"frames/"
CSV             = DATASET+"record.csv"
CSV_PRED        = DATASET+"predict.csv"
MODEL           = "model.h5"

TERM_SIZE       = os.get_terminal_size().columns - 2
VIDEO           = 0

STEERING_INIT   = 0.0
THROTTLE_INIT   = 0.0
STEERING_PARAM  = -1.5
THROTTLE_PARAM  = 1.0

STEERING_LEFT   = -0.57
STEERING_RIGHT  = 0.76
THROTTLE        = 0.3