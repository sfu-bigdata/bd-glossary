all:
	pandoc -s Glossary.md -t html --metadata title="Glossary" | python filter-md.py > generated/Glossary.html
