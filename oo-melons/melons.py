"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
    
    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total    
    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder():
    """A melon order within the USA."""

    def __init__(self, order_type, tax):
        """Initialize melon order attributes."""
        
        self.order_type = "domestic"
        self.tax = 0.08

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5

        if self.species=='christmas melons':
            base_price = base_price * 1.5
            total = (1 + self.tax) * self.qty * base_price

            return total    
    


class InternationalMelonOrder():
    """An international (non-US) melon order."""

    def __init__(self, country_code, order_type, tax):
        """Initialize melon order attributes."""

        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5

        if self.species=='christmas melons':
            base_price = base_price * 1.5
            total = (1 + self.tax) * self.qty * base_price
        if self.qty <10:
            total = ((1 + self.tax) * self.qty * base_price )+ 3

        return total    

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
