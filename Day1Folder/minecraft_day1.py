# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################


################## On Chat Commands Section #####################
def move_forward(steps):
    agent.move(FORWARD, steps)

def move_backward(steps):
    agent.move(BACK, steps)

def move_right(steps):
    agent.move(RIGHT, steps)
def move_left(steps):
    agent.move(LEFT, steps)

def turn_right():
    agent.turn(TurnDirection.LEFT)

def turn_left():
    agent.turn(TurnDirection.RIGHT)

def teleport():
    agent.teleport_to_player()

player.on_chat("come",teleport)
player.on_chat("forward",move_forward)
player.on_chat("back",move_backward)
player.on_chat("left",move_left)
player.on_chat("right",move_right)
player.on_chat("turn left",turn_left)
player.on_chat("turn right", turn_right)
def cow():
    mobs.spawn(COW, pos(423, 76, -1767))
player.on_chat("cow",cow)
def obby():
    agent.move(FORWARD, 4)
    agent.move(LEFT, 4)
    agent.move(FORWARD, 3)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)