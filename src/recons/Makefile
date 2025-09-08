MD_DIR=markdown
HTML_DIR=../../docs/recons
MD=$(shell find $(MD_DIR) *.md)
HTML=$(MD:$(MD_DIR)%.md=$(HTML_DIR)%/index.html)

all: $(HTML)

$(HTML_DIR)%/index.html: $(MD_DIR)%.md
	mkdir -p $$(dirname $@)
	pandoc -f markdown -t html $< -o $@

$(HTML_DIR)/index.html: $(MD_DIR).md
	pandoc -f markdown -t html $< -o $@

clean:
	rm -rf ../../docs/recons
