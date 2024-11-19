class Restaurant():
    """Object represents a Restaurant"""
    def __init__(self, name, foodtype, numserved = 0):
        """Constructor, creates restaurant with given name and cuisine type."""
        self._name = name
        self._foodtype = foodtype
        self._numserved = numserved
        
    def describeRestaurant(self):
        """Prints message displaying restaurant name and cuisine type."""
        print("The Restaurant", self._name, "serves", self._foodtype, "food.")
        
    def openRestaurant(self):
        """Prints declaration that restaurant is open."""
        print(self._name, "is now open.")

    def setNumServed(self, numserved):
        """Sets the number of guests served."""
        self._numserved = numserved

    def incrNumServed(self, numserved):
        """Increments the number of guests served by a set ammount."""
        self._numserved += numserved

restaurant = Restaurant("Wendy's", "American", 432)
print("Customers Served:", restaurant._numserved)
restaurant._numserved = 496
print("Customers Served:", restaurant._numserved)
restaurant.setNumServed(512)
print("Customers Served:", restaurant._numserved)
restaurant.incrNumServed(30)
print("Customers Served:", restaurant._numserved)
