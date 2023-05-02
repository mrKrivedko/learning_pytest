#############################
###### ТЕСТИРУЕМЫЙ КОД ######
#############################
class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()

##########################
###### ТЕСТИРОВАНИЕ ######
##########################
import pytest

# ПОДГОТОВКА
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]

def test_fruit_salad(fruit_bowl):
    # ДЕЙСТВИЕ
    fruit_salad = FruitSalad(*fruit_bowl)

    # УТВЕРЖДЕНИЕ
    assert all(fruit.cubed for fruit in fruit_salad.fruit)
