class Email:
    is_sent = False

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}\nSent: {self.is_sent}'

data = input()

while data != 'Stop':
    data = data.split(" ")
    emails = Email(sender=data[0], receiver=data[1], content=data[2])
