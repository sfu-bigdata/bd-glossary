all: md2html html2word
#	pandoc -s Glossary.md -t html --metadata title="Glossary" -s | python3 filter-md.py > generated/Glossary.html

md2html:
	@echo "Markdown to HTML..."
	pandoc -s Glossary.md -t html --metadata title="Glossary" -s | python3 filter-md.py > generated/Glossary.html
	@echo "Markdown to HTML...complete"

html2word:
	@echo "HTML to Word..."
	pandoc -s --toc generated/Glossary.html --reference-doc=templates/bdh-template.docx -o generated/Glossary.html
	@echo "HTML to Word...complete"

# Unused
md2word:
	@echo "Markdown to Word..."
	pandoc -s Glossary.md --reference-doc=templates/bdh-template.docx -o generated/Glossary.docx
	@echo "Markdown to Word...complete"

	@echo "Markdown to Word..."

clean:
	@echo "Removing generated HTML and Word..."
	-rm generated/Glossary.html generated/Glossary.docx