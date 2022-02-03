all:
	pandoc -s Glossary.md -t html --metadata title="Glossary" -s | python3 filter-md.py > generated/Glossary.html
