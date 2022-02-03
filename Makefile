all:
	pandoc -s Glossary.md -t html --metadata title="Glossary" -s | python3 filter-md.py > generated/Glossary.html

md2word:
	pandoc -s Glossary.md --reference-doc=templates/bdh-template.docx -o generated/Glossary.docx