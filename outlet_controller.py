# Located in some directory *update on raspberry pi*
# Author: Jason C. Nucciarone
# Drafted: 4/21/2019
# Purpose of this program is to enable me to control
# various outlets that I have built into my mechanical relay
# box. I would like to use it on the porch.

import RPi.GPIO as gp
from flask import Flask, render_template
import os  # To cleanup port once program is aborted

app = Flask(__name__)

# Set gpio mode to broadcom and set warnings to false
gp.setmode(gp.BCM)
gp.setwarnings(False)

# Set mode everytime a function is called
# Will see if needed when testing with pi
def gpmode():
    return gp.setmode(gp.BCM)

# Set channels for each of the outlets
# 2 is outlet1
# 3 is outlet2
# 4 is outlet3
# 17 is outlet4
# 27 is outlet5
# 22 is outlet6
# 10 is outlet7
# 9 is outlet8
pinList = [2, 3, 4, 17, 27, 22, 10, 9]

# Set initial switch_closed values to False
# Corresponds to each value in pinList
switch_closed = [False, False, False, False, False, False, False, False]

# Initialize pin modes
for pin in pinList:
    gp.setup(pin, gp.OUT)
    gp.output(pin, gp.HIGH)

# Define function to initialize outlets everytime a function is called
# Will see if needed when testing with pi
def oputMode():
    for pin in pinList:
        gp.setup(pin, gp.OUT)
        gp.output(pin, gp.HIGH)


@app.route("/")  # When the page is first visited
def home_page():
    return render_template("home.html")

@app.route("/outlet1")
def outlet1():
    if switch_closed[0] is False:
        gp.output(pinList[0], gp.LOW)
        switch_closed[0] = True
        return render_template("home.html")

    if switch_closed[0] is True:
        gp.output(pinList[0], gp.HIGH)
        switch_closed[0] = False
        return render_template("home.html")


@app.route("/outlet2")
def outlet2():
    if switch_closed[1] is False:
        gp.output(pinList[1], gp.LOW)
        switch_closed[1] = True
        return render_template("home.html")

    if switch_closed[1] is True:
        gp.output(pinList[1], gp.HIGH)
        switch_closed[1] = False
        return render_template("home.html")


@app.route("/outlet3")
def outlet3():
    if switch_closed[2] is False:
        gp.output(pinList[2], gp.LOW)
        switch_closed[2] = True
        return render_template("home.html")

    if switch_closed[2] is True:
        gp.output(pinList[2], gp.HIGH)
        switch_closed[2] = False
        return render_template("home.html")


@app.route("/outlet4")
def outlet4():
    if switch_closed[3] is False:
        gp.output(pinList[3], gp.LOW)
        switch_closed[3] = True
        return render_template("home.html")

    if switch_closed[3] is True:
        gp.output(pinList[3], gp.HIGH)
        switch_closed[3] = False
        return render_template("home.html")


@app.route("/outlet5")
def outlet5():
    if switch_closed[4] is False:
        gp.output(pinList[4], gp.LOW)
        switch_closed[4] = True
        return render_template("home.html")

    if switch_closed[4] is True:
        gp.output(pinList[4], gp.HIGH)
        switch_closed[4] = False
        return render_template("home.html")


@app.route("/outlet6")
def outlet6():
    if switch_closed[5] is False:
        gp.output(pinList[5], gp.LOW)
        switch_closed[5] = True
        return render_template("home.html")

    if switch_closed[5] is True:
        gp.output(pinList[5], gp.HIGH)
        switch_closed[5] = False
        return render_template("home.html")


@app.route("/outlet7")
def outlet7():
    if switch_closed[6] is False:
        gp.output(pinList[6], gp.LOW)
        switch_closed[6] = True
        return render_template("home.html")

    if switch_closed[6] is True:
        gp.output(pinList[6], gp.HIGH)
        switch_closed[6] = False
        return render_template("home.html")


@app.route("/outlet8")
def outlet8():
    if switch_closed[7] is False:
        gp.output(pinList[7], gp.LOW)
        switch_closed[7] = True
        return render_template("home.html")

    if switch_closed[7] is True:
        gp.output(pinList[7], gp.HIGH)
        switch_closed[7] = False
        return render_template("home.html")

@app.route("/all_off")
def allOff():
    # pin and switch are iterables starting at 0
    for pin in range(len(pinList)):
        gp.output(pinList[pin], gp.HIGH)  # Open all relays

    for switch in range(len(switch_closed)):
        switch_closed[switch] = False

    return render_template("home.html")

# When executing the program
if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)

    except KeyboardInterrupt:
        os.system("sudo fuser -k 5000/tcp")
        app.exit()
