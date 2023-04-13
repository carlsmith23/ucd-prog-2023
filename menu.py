class Menu:

  def __init__(self, simulation):
    self.simulation = simulation

  def main(self):
    continue_menu = True
    while continue_menu:
      print("")
      print("MENU")
      print("")
      print("Set (s)ize of the map")
      print("Add number of (a)gents")
      print("(P)rint map")
      print("(Q)uit")
      print("")
      ans = input("Menu choice: ")

      if ans == "q" or ans == "Q":
        continue_menu = False
      elif ans == "s" or ans == "S":
        self.simulation.map.generate(self.map_size())
      elif ans == "a" or ans == "A":
        self.number_agents()
      elif ans == "p" or ans == "P":
        self.simulation.map.print()

  def map_size(self):
    N = input("How large should the map be (length of a square map): ")
    if not N.isnumeric():
      print("ERROR: The map size should be a number")
      self.simulation.log.write("ERROR: attempt to make non-numeric map size: {}" .format(N))
      return 0

    N = int(N)
    if N < 1 or N > 100:
      print("ERROR: Map size needs to be between 1 and 100")
      self.simulation.log.write("ERROR: attempt to make map size outside of bounds: {}" .format(N))
      return 0
    self.simulation.log.write("map size set to {}" .format(N))
    return N

  def number_agents(self):
    map_size = self.simulation.map.get_length()**2

    if map_size == 0:
      print("ERROR: Cannot set number of agents before setting the map size")
      return 0

    ans = input("How many agents should there be: ")

    if not ans.isnumeric():
      print("ERROR: The number of agents should be a number")
      self.simulation.log.write("ERROR: attempt to non-numeric number of agents: {}" .format(ans))
      return 0

    ans = int(ans)
    if ans < 1 or ans > map_size:
      print("ERROR: The number of agents should be between 1 and %d" %
            map_size)
      self.simulation.log.write("ERROR: attempt to add too many agent: {}" .format(ans))
      return 0

    i = 0
    while i < ans:
      self.simulation.set_random_agent()
      i += 1

    self.simulation.log.write("{} agents randomly placed on map" .format(ans))