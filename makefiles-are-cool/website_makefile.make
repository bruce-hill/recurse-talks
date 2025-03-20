POSTS := $(shell find posts/ -name '*.md')
POST_SYMLINKS = $(POSTS:posts/%.md=%.html)
DRAFTS := $(shell find drafts/ -name '*.md')
MD_FILES := $(shell find . -path ./media -prune -false -o -name '*.md')
MD_GEN = $(MD_FILES:%.md=%.html)
DEST=bruce@bruce-hill.com:/var/www/htdocs/blog.bruce-hill.com

all: $(MD_GEN) index.html drafts/index.html archive.html rss.xml symlinks style.gz.css

symlinks: $(POST_SYMLINKS)

$(POST_SYMLINKS):
	ln -sf "posts/$@" "$@"

clean:
	rm -f $(MD_GEN) posts/*.html posts/*/index.html drafts/*.html drafts/*/index.html index.html archive.html rss.xml

index.html: .staticgen/index.sh $(POSTS) .pandoc/defaults.yml .pandoc/templates/default.html .pandoc/templates/blogpreview.html
	.staticgen/index.sh >$@

archive.html: .staticgen/archive.sh $(POSTS) .pandoc/defaults.yml .pandoc/templates/blogarchive.html
	.staticgen/archive.sh >$@

rss.xml: .staticgen/rss.sh $(POSTS) .pandoc/defaults.yml .pandoc/templates/rss.xml
	.staticgen/rss.sh >$@

drafts/index.html: .staticgen/drafts-index.sh $(DRAFTS) .pandoc/defaults.yml .pandoc/templates/blogpreview.html
	.staticgen/drafts-index.sh >$@

posts/%.html: posts/%.md .pandoc/defaults.yml .pandoc/templates/default.html
	pandoc --defaults .pandoc/defaults.yml -L .pandoc/prev-next.lua --metadata=url:/$(subst posts/,,$(subst .html,,$@)) $< -o $@

%.html: %.md .pandoc/defaults.yml .pandoc/templates/default.html
	pandoc --defaults .pandoc/defaults.yml --metadata=url:/$(subst .html,,$@) $< -o $@

%.gz.css: %.css
	gzip -ck $< >$@

sync: all
	rsync -PuzzlOJtrh --delete --chmod=g+w --chown=:www-data --exclude-from=.rsync-exclude ./ $(DEST)

.PHONY: all sync clean symlinks
# vim: ft=make
