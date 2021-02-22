"""
File: weather_master.py
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment Handout.

"""


def main():
	"""
	TODO:
	"""

print("stanCode \"weather master 4.0!\"")

userinput = 0
inputTimes = 0
sum = 0
colddays = 0

while (int(userinput) != -100):

	userinput = input()

	print("Next temperature: (or -100 to quit):" + userinput)

	sum += int(userinput)
	inputTimes += 1

	if int(userinput) < 16:
		colddays += 1

	HighestTemp = int(userinput)
	LowestTemp = int(userinput)
	AverageTemp = int(userinput)

	if int(userinput) > HighestTemp:
		HighestTemp = userinput

	if int(userinput) < LowestTemp:
		LowestTemp = userinput

AverageTemp = sum/inputTimes

print("Highest Temperature:" + HighestTemp)
print("Lowest Temperature:" + LowestTemp)
print("Average Temperature:" + AverageTemp)
print("Cold days:" + colddays)

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
