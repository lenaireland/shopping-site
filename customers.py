"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    def __init__(self,first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show info about customer in console."""

        return "<Customer: {}, {}, {}>".format(self.first_name, self.last_name, self.email)

def read_customers_from_file(filepath):
    """Read customer file and populate customer dictionary. 

    Returned dictionary will be {id: Customer object}
    """

    customers = {}

    file = open(filepath)

    for line in file:
        (first_name, last_name, email, password) = line.strip().split("|")

        customers[email] = Customer(first_name, last_name, email, password)

    return customers


def get_by_email(email):
    

    return customers[email]

customers = read_customers_from_file("customers.txt")
