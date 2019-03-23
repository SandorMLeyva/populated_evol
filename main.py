from src.simulator import Simulator
from sys import argv

def main():

	woman = 500
	man = 500
	years = 20
	if len(argv) == 4:
		woman = int(argv[1])
		man = int(argv[2])
		years = int(argv[3])
	s = Simulator()
	s.build(woman, man, 12*years)
	collector = s.sim()

	if argv.count('graph'):
		from app import app
		app.data = collector
		app.run(host='0.0.0.0', port=80, debug=False)


if __name__ == '__main__':
	main()


