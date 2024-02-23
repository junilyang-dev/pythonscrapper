class Puppy:

  def __init__(self, name, color):
    self.name = name
    self.age = 0.1
    self.color = color

  def __str__(self):
    return f"Puppy name: {self.name}, age: {self.age}, color: {self.color}"

  def woof_woof(self):
    print(f"{self.name} woof woof!")

  def introduce(self):
    self.woof_woof()
    print(f"Hi, my name is {self.name} and I'm a {self.color} puppy.")

ruffus = Puppy(
  name="Ruffus", 
  color="brown",
)
bibi = Puppy(
  name="Bibi", 
  color="white",
)

print(ruffus, bibi)
ruffus.introduce()
bibi.introduce()
