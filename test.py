# polimorfism example


class Ticket:
    def __init__(self):
        pass

    def generate(self):
        return "This is the ticket"


class DigitalTicket(Ticket):
    def download(self):
        pass

    def generate(self):
        return "This is Digital ticket"


ticket = Ticket()
digital_ticket = DigitalTicket()

lst = [ticket, digital_ticket]

for obj in lst:
    print(obj.generate())

# ticket.generate()
# digital_ticket.generate()
