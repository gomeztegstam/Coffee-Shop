from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder

def test_beverage():
    b = Beverage(4, 4.0)
    assert b.getOunces() == 4
    assert b.getPrice() == 4.00
    b.updateOunces(6)
    b.updatePrice(6.00)
    assert b.getOunces() == 6
    assert b.getPrice() == 6.00
    assert b.getInfo() == "6 oz, $6.00"
def test_coffee():
    c = Coffee(6, 2.0, "Latte")
    assert "Latte Coffee, 6 oz, $2.00" == c.getInfo()
def test_FruitJuice():
    juice = FruitJuice(10, 4.57, ["Apple", "Banana"])
    assert "Apple/Banana Juice, 10 oz, $4.57" == juice.getInfo()
def test_DrinkOrder():
    c1 = Coffee(9, 4.5, "Americano")
    juice = FruitJuice(16, 4.5, ["Strawberry", "Blueberry"])
    order = DrinkOrder()
    order1 = DrinkOrder()
    order.addBeverage(c1)
    order.addBeverage(juice)
    assert order.getTotalOrder() == "Order Items:\n* Americano Coffee, 9 oz, $4.50\n* Strawberry/Blueberry Juice, 16 oz, $4.50\nTotal Price: $9.00"
    assert order1.getTotalOrder() == "Order Items:\nTotal Price: $0.00"
