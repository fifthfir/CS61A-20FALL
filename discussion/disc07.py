class Student:
    students = 0  # This is a class sttribute

    def __init__(self, name, staff):
        self.name = name  # This is an instance sttribute
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        staff.add_student(self)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks,", staff.name)


class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1


class MinList:
    """A list that can only pop the smallest element"""
    def __init__(self):
        self.items = []
        self.size = 0

    def append(self, item):
        """Appends an item to the MinList
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(2)
        >>> m.size
        2
        """
        self.items.append(item)
        self.size += 1

    def pop(self):
        """Removes and returns the smallest item from the MinList
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(1)
        >>> m.append(5)
        >>> m.pop()
        1
        >>> m.size
        2
        """
        min_item = min(self.items)
        self.items.pop(self.items.index(min_item))
        self.size -= 1
        return min_item


class Email:
    """Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.message = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

    def __str__(self):
        return f"From: {self.sender_name}\n\
            To: {self.recipient_name}\n\
                Message: {self.message}\n"


class Server:
    """Each Server has an instance attribute clients, which
    is a dictionary that associates client names with
    client objects.
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to.
        """
        recipient = self.clients[email.recipient_name]
        if recipient:
            recipient.receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds them
        to the clients instance attribute.
        """
        self.clients[client_name] = client


class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).
    """
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.
        """
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)

    def receive(self, email):
        """Take an email and add it to the inbox of this
        client.
        """
        self.inbox.append(email)


class Pet:
    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)


class Dog(Pet):
    def talk(self):
        print(self.name + " says woof!")


class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner)
        self.lives = lives

    def talk(self):
        print(self.name + " says meow!")

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is alive'
        becomes False. If this is called after lives has reached zeor,
        print out that the cat has no more ives to lose.
        """
        if self.is_alive:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False
        else:
            print(self.name + " has no more lives to lose.")


class NoisyCat(Cat):
    """A Cat that repeats things twice."""
    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat("Magic", "James").talk()
        Magic says meow!
        Magic says meow!
        """
        super().talk()
        super().talk()

    def __repr__(self):
        """The interpreter-readable representation of a NoisyCat
        >>> muffin = NoisyCat('Muffin', 'Catherine')
        >>> repr(muffin)
        "NoisyCat('Muffin', 'Catherine')"
        >>> muffin
        NoistCat('Muffin', 'Catherine')
        """
        return f"NoisyCat('{self.name}', '{self.owner}')"
