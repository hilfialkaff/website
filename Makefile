all: gen

resume: content/media/pdfs/resume.pdf

content/media/pdfs/resume.pdf: resume/resume.tex
	cd resume; make
	mkdir -p content/media/pdfs/
	cp resume/resume.pdf content/media/pdfs/

gen: resume
	hyde gen

serve: clean gen
	hyde serve

clean:
	rm -rf deploy/*
