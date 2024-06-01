from essential_generators import DocumentGenerator
import random

gen = DocumentGenerator()

sentence = gen.sentence()

students = ["Prince", "Phil", "Nicole"]
random_int = random.randint(0, 3)

print(f'{students[random_int]} always says - "{sentence}"')



