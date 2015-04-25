GIT ?= git
CP ?= cp -r
MKDIR ?= mkdir -p
LN ?= ln -sf

prefix = $(DESTDIR)/usr
target_dir = $(prefix)/share/maildir-notifier
bin_dir = $(prefix)/bin

TARGETS = \
	mail_notify.py \
	notify.py \
	watcher.py \

EXECUTABLES = \
	maildir-notifier.sh \

all: $(TARGETS)

install::
	$(MKDIR) $(target_dir) $(bin_dir)
	$(CP) $(TARGETS) $(target_dir)
	$(CP) $(EXECUTABLES) $(target_dir)
	for i in $(EXECUTABLES) ; do \
		chmod +x $(target_dir)/$$i; \
		$(LN) $(target_dir)/$$i $(bin_dir)/$$i; \
	done

uninstall::
	for i in $(EXECUTABLES) ; do \
		$(RM) $(bin_dir)/$$i; \
	done
	$(RM) -r $(target_dir)

clean::
	$(GIT) clean -d -f

.PHONY : install uninstall clean
