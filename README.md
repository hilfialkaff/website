The code in this repository is being used for my personal website, which is located at http://www.hilfialkaff.com

Requirement
===========

* [Hyde](http://hyde.github.io/)
* [Boto](https://code.google.com/p/boto/) (For AWS)
* [pdflatex](http://www.tug.org/texlive/) (For compiling the resume)

Building
========

Generate version for local development:
* make gen

Preview local version (this is previewable in the browser at localhost:8080):
* make serve

Deploying it in AWS:
* python ./scripts/deploy_aws.py
