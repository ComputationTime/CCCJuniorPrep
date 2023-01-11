def find_shortest_cycle(temps):
  # initialize the shortest cycle to be the maximum possible length
  shortest_cycle = len(temps)

  # calculate the temperature differences
  differences = []
  for i in range(1, len(temps)):
    differences.append(temps[i] - temps[i - 1])

  # iterate through the temperature differences
  for i in range(len(differences)):
    # iterate through the possible cycle lengths
    for j in range(2, len(differences)):
      # check if this is a valid cycle
      valid_cycle = True
      for k in range(j):
        if differences[(i + k) % len(differences)] != differences[(i + k) % j]:
          # if any of the differences don't match or we are out of bounds, this is not a valid cycle
          valid_cycle = False
          break
      # if this is a valid cycle and it is shorter than the current shortest cycle, update the shortest cycle
      if valid_cycle and j < shortest_cycle:
        shortest_cycle = j
  return shortest_cycle


x = [int(x) for x in input().split()]
while x != [0]:
    x = x[1:]
    print(find_shortest_cycle(x))
    x = [int(x) for x in input().split()]
