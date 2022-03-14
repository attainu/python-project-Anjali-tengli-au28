import sys
import argparse
import Parking

if sys.version_info[0] == 2:
	input = raw_input

def main():
	try:
		parkinglot = Parking.ParkingLot()
		parser = argparse.ArgumentParser()
		parser.add_argument('-f', action="store", required=False, dest='src_file', help="Input File")
		args = parser.parse_args()

		if args.src_file:
			with open(args.src_file) as f:
				for line in f:
					line = line.rstrip('\n')
					parkinglot.show(line)
		else:
				while True:
					line = input("$ ")
					parkinglot.show(line)
	except:
		print("Please contact admin for error details!")
if __name__ == '__main__':
	main()