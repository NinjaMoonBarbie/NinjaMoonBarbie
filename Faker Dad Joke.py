from dadjokes import Dadjoke
from faker import Faker

# Initialize Dadjoke
dadjoke = Dadjoke()

# Print a dad joke
print(dadjoke.joke)

# Initialize Faker
fake = Faker()

# Generate and print fake name and address
print(fake.name())     # Output: Lucy Cechtelar
print(fake.address())  # Output: 426 Jordy Lodge\nCartwrightshire, SC 88120-6700

print(f"{fake.name()} lives at {fake.address()} and the favorite Dadjoke is {dadjoke.joke}")

