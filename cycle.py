import RPi.GPIO as GPIO
import time #from time import sleep
import sys

runmode = 'all'
if len(sys.argv) == 2:
  runmode = sys.argv[1]

GPIO.setmode(GPIO.BCM)
print "setmode"
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)

GPIO.setup(0, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
# gpio 14 is relay 6
#GPIO.setup(21, GPIO.OUT) 
# gpio 21 is relay 7

# turn all relays OFF
GPIO.output(17, GPIO.HIGH) # sprinkler 1
GPIO.output(27, GPIO.HIGH) # sprinkler 2
GPIO.output(22, GPIO.HIGH) # sprinkler 3
GPIO.output(10, GPIO.HIGH) # sprinkler 5
GPIO.output(9, GPIO.HIGH)  # sprinkler 6
GPIO.output( 5, GPIO.HIGH) # sprinkler sub solenoid 7
GPIO.output(11, GPIO.HIGH) # sprinkler sub solenoid 8

print "go hi"
#print "energizing transformer"
#GPIO.output( 5, GPIO.LOW)
#time.sleep(10)

if runmode == 'all' or runmode == '1':
 # pin 17 is relay 1 is sprinker circuit 1
  GPIO.output(17, GPIO.LOW)
  time.sleep(240)
  GPIO.output(17, GPIO.HIGH)

if runmode == 'all' or runmode == '2':
  #pin 27 is relay 2 is sc 2
  GPIO.output(27, GPIO.LOW)
  time.sleep(240)
  GPIO.output(27, GPIO.HIGH)

if runmode == 'all' or runmode == '3':
  #pin 22 is relay 3 is sc 3 
  GPIO.output(22, GPIO.LOW)
  time.sleep(240)
  GPIO.output(22, GPIO.HIGH)

if runmode == 'all' or runmode == '5':
  #pin 10 is relay 4 is sc5
  GPIO.output(10, GPIO.LOW)
  time.sleep(300)
  GPIO.output(10, GPIO.HIGH)

if runmode == 'all' or runmode == '6':
  # ping 9 is relay 5 is sc6
  GPIO.output( 9, GPIO.LOW)
  #start relay
  GPIO.output(11, GPIO.LOW)
  time.sleep(300)
  GPIO.output(11, GPIO.HIGH)

  # Start relay 7 for other half
  GPIO.output(5, GPIO.LOW)
  time.sleep(300)
  GPIO.output(5, GPIO.HIGH)
  GPIO.output( 9, GPIO.HIGH)

  # ping 14 is relay 6 is sc7
#GPIO.output(11, GPIO.LOW)
#sleep(300)
#GPIO.output(11, GPIO.HIGH)

#GPIO.output( 0, GPIO.LOW)
#sleep(300)
#GPIO.output( 0, GPIO.HIGH)
#sleep(300)
# GPIO.output( 5, GPIO.HIGH)

print "done"
GPIO.cleanup()
