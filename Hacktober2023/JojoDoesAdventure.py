class Room:
  def __init__(self, name, description, exits):
    self.name = name
    self.description = description
    self.exits = exits

class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room

  def move(self, direction):
    if direction in self.current_room.exits:
      self.current_room = self.current_room.exits[direction]
    else:
      print('You cannot go in that direction.')

# Create the rooms
kitchen = Room('Kitchen', 'You are in the kitchen.', {'north': 'living_room'})
living_room = Room('Living Room', 'You are in the living room.', {'south': 'kitchen'})

# Create the player
player = Player('Jojo', kitchen)

# Start the game loop
while True:
  print(player.current_room.description)
  print('What do you want to do?')

  command = input()

  if command == 'go north':
    player.move('north')
  elif command == 'go south':
    player.move('south')
  elif command == 'quit':
    break
  else:
    print('I do not understand that command.')
