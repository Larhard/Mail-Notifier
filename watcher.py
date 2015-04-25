import pyinotify
import re
import notify
import mailbox


class MailEventHandler(pyinotify.ProcessEvent):
    def my_init(self, maildir):
        self.maildir = mailbox.Maildir(maildir)

    def process_IN_MOVED_TO(self, event):
        self.new_mail_notify(event.name)

    def process_IN_CREATE(self, event):
        self.new_mail_notify(event.name)

    def new_mail_notify(self, mail_path):
        mail_id, *_ = mail_path.split(':')
        mail = self.maildir.get(mail_id)
        notify.send('new_mail', 'From: {}\nSubject: {}'.format(mail.get('From'), mail.get('Subject')))


def watch_maildir(maildir):
    notify.init('mail notifier')

    watch_manager = pyinotify.WatchManager()

    handler = MailEventHandler(maildir=maildir)
    notifier = pyinotify.Notifier(watch_manager, handler)

    watch_manager.add_watch(maildir, pyinotify.IN_CREATE | pyinotify.IN_MOVED_TO, rec=True)

    notifier.loop()
