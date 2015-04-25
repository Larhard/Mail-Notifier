import notify2


def init(program):
    notify2.init(program)


def send(title, message):
    notify2.Notification(title, message).show()