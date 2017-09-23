# Kristin Lin
# SoftDev pd09
# Work 04: Can I flask you a question?
# 2017-09-22

from flask import Flask

ansMach = Flask(__name__)

@ansMach.route('/')
def display1() :
    return "Hello! First stop on our journey: New York!"

@ansMach.route('/later')
def display2() :
    return "Hey there again! Second stop: Kansas City!"

@ansMach.route('/muchlater')
def display3() :
    return "Good to see all your familiar faces! Final stop: San Francisco!"

if (__name__ == '__main__') :
    ansMach.debug = True
    ansMach.run()
