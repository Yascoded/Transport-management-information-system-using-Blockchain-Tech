
from app import app


if __name__ == '__main__':
	app.run(host = "localhost", threaded = True, port=1881, debug=True) 
