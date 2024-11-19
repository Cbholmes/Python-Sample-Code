from restaurant import Restaurant
class IceCreamStand(Restaurant):
    "Represents an ice cream stand as a child of restaurant."
    def __init__(self, name, foodtype, flavors, numserved = 0):
        """Constructor, creates ice cream stand with given restaurant arguments and flavors"""
        super().__init__(name, foodtype, numserved)
        self._flavors = flavors

    def showFlavors(self):
        """Prints availible ice cream flavors."""
        print("Availible flavors:")
        for flavor in self._flavors: print(flavor)

"""Driver Code creates an icecream stand restaurant and then gets the icecream flavors"""
stand = IceCreamStand("Joe's Ice Cream", "Ice Cream", ["Chocolate", "Vanilla", "Strawberry"])
stand.showFlavors()
