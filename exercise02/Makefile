# Latex Makefile using latexmk
# Author: Michael Eliachevitch <meliache@uni-bonn.de>
# Adapted from https://gist.github.com/dogukancagatay/2eb82b0233829067aca6 by Dogukan Cagatay <dcagatay@gmail.com>
# Originally from : http://tex.stackexchange.com/a/40759

export TEXINPUTS:=.//:../../tex//:${TEXINPUTS}:

# Change only the variable below to the name of the main tex file.
PROJNAME=exercise02

# You want latexmk to *always* run, because make does not have all the info.
# Also, include non-file targets in .PHONY so they are run regardless of any
# file of the given name existing.
.PHONY: $(PROJNAME).pdf all clean

# The first rule in a Makefile is the one executed by default ("make"). It
# should always be the "all" rule, so that "make" and "make all" are identical.
all: $(PROJNAME).pdf

# CUSTOM BUILD RULES

# In case you didn't know, '$@' is a variable holding the name of the target,
# and '$<' is a variable holding the (first) dependency of a rule.
# "raw2tex" and "dat2tex" are just placeholders for whatever custom steps
# you might have.

%.tex: %.raw
	./raw2tex $< > $@

%.tex: %.dat
	./dat2tex $< > $@

# MAIN LATEXMK RULE

# -pdf tells latexmk to generate PDF directly (instead of DVI).
# -use-make tells latexmk to call make for generating missing files.
# -interaction=nonstopmode keeps the pdflatex backend from stopping at a
#  missing file reference and interactively asking you for an alternative.
# -shell-escape: allows latex to execude code in the shell, which is disabled by
#  default for security reasons. Require for the latex "minted" package which
#  allows for syntax highlighting via the python Pygments package

$(PROJNAME).pdf: $(PROJNAME).tex
	latexmk -pdf -pdflatex="pdflatex -synctex=1 -interaction=nonstopmode" -shell-escape -use-make $<

cleanall:
	latexmk -C
	rm -vf *.aux  *.qsl  *.sol *_xdefs.cut *.bbl *.pyg
	rm -rfv _minted-exercise*

clean:
	latexmk -c
	rm -vf *.aux  *.qsl  *.sol *_xdefs.cut *.bbl *.pyg
	rm -rfv _minted-exercise*
