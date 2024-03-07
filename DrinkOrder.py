#DrinkOrder.py
from Coffee import Coffee
from FruitJuice import FruitJuice

class DrinkOrder:
    def __init__(self):
        self.drinks = []
    def addBeverage(self, beverage):
        self.drinks.append(beverage)
    def getTotalOrder(self):
        orderTotal = 0.0
        if len(self.drinks) == 0:
            return "Order Items:\nTotal Price: $0.00"
        orderString = "Order Items:\n"
        for drink in self.drinks:
            orderTotal += drink.getPrice()
            orderString += f"* {drink.getInfo()}\n"
        orderString += f"Total Price: ${orderTotal:.2f}"
        return orderString
            
    

