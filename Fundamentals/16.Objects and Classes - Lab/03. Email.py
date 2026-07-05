class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'

emails = []
data = input()

while data != 'Stop':
    data = data.split()
    emails.append(data)
    data = input()

index = list(map(int, input().split(", ")))

for i in range(len(emails)):
    current_email = Email(sender=emails[i][0], receiver=emails[i][1], content=emails[i][2])
    if i in index:
        current_email.send()

    print(current_email.get_info())


