MD_FILES := $(shell find -name '*.md')
MD_GEN = $(MD_FILES:%.md=%.html)

all: tomo.html

clean:
	rm -f $(MD_GEN)

%.html: %.md .pandoc/defaults.yml .pandoc/template.html .pandoc/tomo.xml Makefile
	pandoc --webtex -t slidy --embed-resources --standalone --defaults .pandoc/defaults.yml \
		--metadata=url:/$(subst .html,,$@) $< -o $@

%.pdf: %.md .pandoc/defaults.yml
	pandoc --pdf-engine typst --defaults .pandoc/defaults.yml --metadata=url:/$(subst .html,,$@) $< -o $@

.PHONY: all clean
