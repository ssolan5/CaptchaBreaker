LATEX=pdflatex
BIBTEX=bibtex
RM=rm -f

#############################
TARGET=paper
#############################

TEXFILES=*.tex
BIBFILES=*.bib

all: ${TARGET}.pdf

${TARGET}.pdf: ${TEXFILES} ${TARGET}.bbl
	$(LATEX) $(TARGET)

${TARGET}.bbl: ${BIBFILES}
	$(LATEX) $(TARGET)
	$(BIBTEX) $(TARGET)
	$(LATEX) $(TARGET)
	$(LATEX) $(TARGET)


clean:
	$(RM) *.aux *.bbl *.blg *.log *.dvi *.toc *.lof *.out $(TARGET).ps $(TARGET).pdf

