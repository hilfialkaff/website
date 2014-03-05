FILES := resume.aux resume.log

all: resume

resume: resume.tex
	pdflatex $<
	rm -f $(FILES)

clean:
	rm -f resume.pdf $(FILES)
