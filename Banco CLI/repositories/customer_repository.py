from models import Customer


class CustomerRepository:

    def __init__(self):
        self._customers = []

    def add_customer(self, customer):
        self._customers.append(customer)

    def list_all_customers(self):
        return self._customers.copy()

    def count_customers(self):
        return len(self._customers)

    def search_customer_by_id(self, customer_id):
        for customer in self._customers:
            if customer.get_id() == customer_id:
                return customer

        return None

    def id_already_exists(self, customer_id):
        for customer in self._customers:
            if customer.get_id() == customer_id:
                return True

        return False
