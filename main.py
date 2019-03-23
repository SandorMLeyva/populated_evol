from src.simulator import Simulator
from app import app
from sys import argv

def main():
	woman = 50
	man = 50
	years = 10
	if len(argv) > 1:
		woman = int(argv[1])
		man = int(argv[2])
		years = int(argv[3])
	s = Simulator()
	s.build(woman, man, 12*years)
	collector = s.sim()

	app.run(host='0.0.0.0', port=8080, debug=True)


if __name__ == '__main__':
	main()


