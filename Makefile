#!/usr/bin/make
#
all: run
VERSION=`cat version.txt`
BUILD_NUMBER='0'

.PHONY: bootstrap
bootstrap:
	if ! test -f bin/python; then virtualenv-2.7 --no-site-packages .;fi
	./bin/python bootstrap.py

.PHONY: buildout
buildout:
	if ! test -f bin/buildout;then make bootstrap;fi
	#if ! test -f var/filestorage/Data.fs;then make standard-config; else bin/buildout -Nt 7;fi
	bin/buildout -Nt 7

.PHONY: plone-site
plone-site:
	if ! test -f bin/buildout;then make bootstrap;fi
	bin/buildout -Nt 7 -c plone-site.cfg

.PHONY: run
run:
	if ! test -f bin/instance;then make buildout;fi
	bin/instance fg

.PHONY: cleanall
cleanall:
	rm -fr develop-eggs downloads eggs parts .installed.cfg lib include bin buildout.cfg .mr.developer.cfg
