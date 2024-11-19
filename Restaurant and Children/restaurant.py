class Restaurant():
    """Object represents a Restaurant"""
    def __init__(self, name, foodtype):
        """Constructor, creates restaurant with given name and cuisine type."""
        self._name = name
        self._foodtype = foodtype
        
    def describeRestaurant(self):
        """Prints message displaying restaurant name and cuisine type."""
        print("The Restaurant", self._name, "serves", self._foodtype, "food.")
        
    def openRestaurant(self):
        """Prints declaration that restaurant is open."""
        print(self._name, "is now open.")


"""Driver code, creates 4 restaurants and prints information about them."""
restaurant = Restaurant("Wendy's", "American")
print(restaurant._name)
print(restaurant._foodtype)
restaurant.describeRestaurant()
restaurant.openRestaurant()
print()
rosas = Restaurant("Rosa's Cafe", "Tex-Mex")
rosas.describeRestaurant()
print()

olivegar = Restaurant("Olive Garden", "Italian")
olivegar.describeRestaurant()
print()

chinaking = Restaurant("China King Buffet", "Chinese")
chinaking.describeRestaurant()
print()
