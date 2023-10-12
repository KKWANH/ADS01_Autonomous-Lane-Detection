# - import python library
import os
import time
import traceback

# - import color variables
from util.color import *

# - variables
CSVFILE = "dataset/record.csv"
TERM_SIZE = os.get_terminal_size().columns
THROTTLE_PARAM = 0.6
STEERING_PARAM = 1.3

# - automat run program
def run_action_order(vehicle, throttle, steering):
    vehicle.set_throttle_percent(throttle * THROTTLE_PARAM)
    vehicle.set_steering_percent(steering * STEERING_PARAM)
    with open(CSVFILE, "a") as csv_file:
        csv_file.write(f"{time.time()},{steering},{throttle}\n")


def run_action(vehicle, throttle, steering, duration):
    if  throttle > 1.0 or throttle < -1.0 or\
        steering > 1.0 or steering < -1.0:
        print(
            f"{RED}{BOL}[FAILURE]{RES}    ",
            f"Check the throttle and steering value.",
            "\n",
            f"{RED}{BOL}         {RES}    ",
            f"It must between -1.0 ~ 1.0.",
            "\n",
            f"{RED}{BOL}         {RES}    ",
            f"{YEL}throttle: [{throttle}], steering: [{steering}]{RES}"
        )
        return
    start_time = time.time()
    while time.time() - start_time < duration:
        run_action_order(vehicle, throttle, -steering)
    vehicle.set_steering_percent(0)

def automat_run(vehicle):
    # Infor program start
    print(
        f"{CYA}{BOL}[INFORMT]{RES}    ",
        f"Automat-run process has been started at:",
        "\n",
        f"{CYA}{BOL}         {RES}    ",
        f"{time.time()}"
    )

    # Initialize objects
    vehicle.set_steering_percent(0)
    vehicle.set_throttle_percent(0)

    # Check csv label
    if  not os.path.exists(CSVFILE):
        with open(CSVFILE, "w") as file:
            file.write("miliseconds,steering,throttle\n")

    try:
        while True:
            run_action(
                vehicle,
                throttle=0.6,
                steering=0.0,
                duration=3.0
            )
            run_action(
                vehicle,
                throttle=0.6,
                steering=1.0,
                duration=2.0
            )
    except Exception as exception:
        print(
            f"{RED}{BOL}[FAILURE]{RES}    ",
            f"Unexpected exception has occured.\n",
            f"{BOL}", "-"*TERM_SIZE, f"{RES}\n",
            exception,
            "-" * TERM_SIZE,
        )
        print(
            f"{RED}{BOL}[FAILURE]{RES}    ",
            f"Exception log by traceback:\n",
            f"{BOL}", "-" * TERM_SIZE)
        traceback.print_exc()
        print(
            "-" * TERM_SIZE, f"{RES}",
        )
    finally:
        vehicle.set_steering_percent(0)
        vehicle.set_throttle_percent(0)