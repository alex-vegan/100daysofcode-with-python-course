from time import sleep
from itertools import cycle
from collections import OrderedDict
from subprocess import run
from click import style
from csv import DictReader

time_slots = OrderedDict([('red', 5), ('red_yellow', 5), ('green', 5), ('green_wink', 2), ('yellow', 2)])


def light_rotation(time_slots):
    rotation = cycle(time_slots)
    traffic_lights = {"red": " READY-READY-READY ",
                   "yellow": "   STEADY-STEADY   ",
                    "green": " GO-GO-GO-GO-GO-GO "}
    for colour in rotation:
        run("clear")
        if colour in list(traffic_lights.keys()):
            traffic_lights_copy = traffic_lights.copy()
            traffic_lights_copy[colour] = style(traffic_lights[colour], bg=colour)
            print("\n".join(traffic_lights_copy.values()))
            sleep(time_slots[colour])
        elif colour == "red_yellow":
            traffic_lights_copy["yellow"] = style(traffic_lights["yellow"], bg="yellow")
            print("\n".join(traffic_lights_copy.values()))
            sleep(time_slots[colour])
        elif colour == "green_wink":
            traffic_lights_copy = traffic_lights.copy()
            for _ in range(time_slots[colour]):
                run("clear")
                traffic_lights_copy["green"] = style(traffic_lights["green"], fg="green")
                print("\n".join(traffic_lights_copy.values()))
                sleep(0.5)
                run("clear")
                traffic_lights_copy["green"] = style(traffic_lights["green"], bg="green")
                print("\n".join(traffic_lights_copy.values()))
                sleep(0.5)


if __name__ == "__main__":
    light_rotation(time_slots)
