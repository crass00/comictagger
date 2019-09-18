VERSION_STR := $(shell python -c 'import comictaggerlib.ctversion; print( comictaggerlib.ctversion.version)')

ifeq ($(OS),Windows_NT)
	APP_NAME=comictagger.exe
	FINAL_NAME=ComicTagger-$(VERSION_STR).exe
else ifeq ($(shell uname -s),Darwin)
	APP_NAME=ComicTagger.app
	FINAL_NAME=ComicTagger-$(VERSION_STR).app
else
	APP_NAME=comictagger
	FINAL_NAME=ComicTagger-$(VERSION_STR)
endif

.PHONY: all clean pydist upload unrar dist
	
all: clean dist

clean:
	rm -rf *~ *.pyc *.pyo
	rm -rf scripts/*.pyc
	cd comictaggerlib; rm -f *~ *.pyc *.pyo
	rm -rf dist MANIFEST
	rm -rf *.deb
	rm -rf logdict*.log
	$(MAKE) -C mac clean   
	rm -rf build
	rm -rf comictaggerlib/ui/__pycache__

pydist:
	make clean
	mkdir -p piprelease
	rm -f comictagger-$(VERSION_STR).zip
	python setup.py sdist --formats=zip  #,gztar
	mv dist/comictagger-$(VERSION_STR).zip piprelease
	rm -rf comictagger.egg-info dist
		
upload:
	python setup.py register
	python setup.py sdist --formats=zip upload

dist: pyinstaller -y comictagger.spec
	mv dist/$(APP_NAME) dist/$(FINAL_NAME)
