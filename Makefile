# Makefile for source rpm: gnuplot
# $Id$
NAME := gnuplot
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
