from datetime import datetime


class Owner:
    """Owner class with information about borrowed books."""

    def __init__(
        self,
        firstname: str,
        lastname: str,
        borrowdate: str,
        returned: bool,
        returndate: str,
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.borrowdate = borrowdate
        self.returned = returned
        self.returndate = returndate

    def borrowtime(self):
        borrowtime = datetime.strptime(self.returndate, "%Y-%M-%d") - datetime.strptime(
            self.borrowdate, "%Y-%M-%d"
        )
        return f"You have this book borrowed for {borrowtime}."


class Read:
    """Read class with information about reading a book."""

    def __init__(self, start, end, duringreading, note, review):
        self.start = start
        self.end = end
        self.duringreading = duringreading
        self.note = note
        self.review = review
