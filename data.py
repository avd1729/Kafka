from faker import Faker
from pizzaproducer import PizzaProvider
fake = Faker()


fake.add_provider(PizzaProvider)
for i in range(0, 10):
    print(fake.pizza_name())


# message = {
#     "name": fake.name(),
#     "address": fake.address(),
#     "phone": fake.phone_number()
# }

# print(message)
