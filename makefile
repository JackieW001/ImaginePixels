all: work01.py
	python work01.py
	convert work01.ppm work01.png

clean: 
	rm work01.ppm
