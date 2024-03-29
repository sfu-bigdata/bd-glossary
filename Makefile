#PYTHON := $(shell conda run -n base which python)
PYTHON = ~/miniconda3/bin/python

all: md2html html2word
#	pandoc -s Glossary.md -t html --metadata title="Glossary" -s | python3 filter-md.py > generated/Glossary.html

md2html: Glossary.md
	@echo "Markdown to HTML..."
	pandoc -s Glossary.md -t html --metadata title="Data Literacy: Glossary and Index" -s | ${PYTHON} filter-md.py > generated/Glossary.html
	@echo "Markdown to HTML...complete"

html2word: generated/Glossary.html
	@echo "HTML to Word..."
	pandoc -s --toc generated/Glossary.html --reference-doc=templates/bdh-template.docx -o generated/Glossary.docx
	@echo "HTML to Word...complete"

# Generic; Unused
md2word: Glossary.md
	@echo "Markdown to Word..."
	pandoc -s Glossary.md --reference-doc=templates/bdh-template.docx -o generated/Glossary.docx
	@echo "Markdown to Word...complete"

	@echo "Markdown to Word..."

htmlheadings: 
	# Add CSS and <header> sections
	(cd generated; pandoc -s --toc --css ../templates/template.css -H ../templates/header.html Glossary.html -o Glossary.html)

clean_all:
	@echo "Removing generated HTML and Word..."
	-rm generated/Glossary.html generated/Glossary.docx
