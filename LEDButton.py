#imports
import time
import RPi.GPIO as GPIO

#pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#main
def main():
	#part 1
	print("part 1")
	#turn led on
	GPIO.output(17,GPIO.HIGH
	#wait
	time.sleep(4)
	#turn led off
	GPIO.output(17,GPIO.LOW)

	#part 
	print("part 2")
	#led starts off
	GPIO.output(17,GPIO.LOW)
	#Button pressed
	try:
		while True:
			GPIO.output(17, not GPIO.input(23)
			time.sleep(.5)
	finally:
		GPIO.output(17,GPIO.LOW)

#run main
if __name__ == "__main__":
	#required to close the GPIO 
	try:
		while True:
			main()
	except KeyboardInterrupt:
		print("closed")
		GPIO.cleanup()
	except Exception as e:
		GPIO.cleanup
		print(e.message)
