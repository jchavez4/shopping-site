"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 password):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return "<Customer: {name}, {email}".format(
            name=self.first_name + " " + self.last_name,
            email=self.email)


def read_customers_from_file(filepath):
    """Read customer data and populate dictionary of customers."""

    customers = {}

    for line in open(filepath):
        (first_name,
         last_name,
         email,
         password) = line.strip().split("|")

        customers[email] = Customer(first_name,
                                    last_name,
                                    email,
                                    password)

    return customers


def get_by_email(email):
    """Return a customer, given their email."""

    return customers[email]


customers = read_customers_from_file("customers.txt")
