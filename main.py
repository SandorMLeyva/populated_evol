from src.simulator import Simulator
from sys import argv

def main():
	woman = 500
	man = 500
	years = 100
	if len(argv) > 1:
		woman = int(argv[1])
		man = int(argv[2])
		years = int(argv[3])
	s = Simulator()
	s.build(woman, man, 12*years)
	collector = s.sim()

	# from app import app
	# app.data = collector
	# app.run(host='0.0.0.0', port=8080, debug=True)


if __name__ == '__main__':
	main()


