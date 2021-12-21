import subprocess

x = subprocess.check_output("ls /media/rostugs", shell=True)
x = str(x.strip()).strip("b\'")
print(x + "makan") 