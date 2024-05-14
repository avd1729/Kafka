import random
from faker.providers import BaseProvider


class PizzaProvider(BaseProvider):

    def pizza_name(self):

        name = [
            'Margherita',
            "Marinara",
            "Diayola",
            "Salami",
            "Pepperoni"
        ]

        return name[random.randint(0, len(name)-1)]
