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

class GovernmentMelonOrder(AbstractMelonOrder):

    # passed_inspection = False
    tax = 0
    order_type = "government"
    
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.passed_inspection = False
        
 
    def mark_inspection(self,passed):
        """a method mark_inspection(passed) that takes a Boolean input, passed, and updates 
        whether or not the melon has passed inspection. 
        This method should update the attribute passed_inspection."""

        self.passed_inspection = passed



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08
     
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        
        super().__init__(species, qty)


    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5

        if self.species=='christmas melons':
            base_price = base_price * 1.5
            total = (1 + self.tax) * self.qty * base_price

            return total    
    


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        
        super().__init__(species, qty)
        self.country_code = country_code

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
