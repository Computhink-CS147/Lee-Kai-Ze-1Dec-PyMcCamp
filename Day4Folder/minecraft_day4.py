# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
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

player.on_chat("obby", obby)


# def chop_all():
    

def chop(height):
    for count in range(height):
        agent.destroy(FORWARD)
        agent.move(UP, 1)
    agent.move(DOWN, height)   
    agent.collect_all()



def chopmore(height):
    for count in range(height):
        agent.destroy(FORWARD)
        agent.move(UP, 1)
        agent.destroy(UP)
    agent.move(DOWN, height)
    agent.collect_all()
    agent.move(FORWARD, 1)
    for count in range(height):
            agent.destroy(FORWARD)
            agent.move(UP, 1)
            agent.destroy(UP)
    agent.move(DOWN, height)
    agent.collect_all()






def mineall(length):
    for mine in range(length):
        agent.destroy(FORWARD) 
        agent.destroy(RIGHT)
        agent.destroy(LEFT)
        agent.destroy(DOWN)
        agent.collect_all()
        agent.move(FORWARD,1)


player.on_chat("chop",chopmore)
player.on_chat("mine",mineall)

def diamond():
    blocks.place(DIAMOND, pos(0, 0, 0))

player.on_chat("diamond",diamond) 



def wall():
    agent.set_slot(1)
    for count in range(21):
        agent.place(UP)
        agent.place(DOWN)
        agent.place(BACK)
        agent.move(FORWARD, 1)
    agent.set_slot(2)
    for count in range(10):
        agent.place(UP)
        agent.place(DOWN)
        agent.place(BACK)
        agent.move(FORWARD, 1)
player.on_chat("wall",wall)

def wall2(length):
    agent.set_slot(1)
    for count in range(length):
        agent.place(UP)
        agent.place(DOWN)
        agent.place(BACK)
        agent.move(FORWARD, 1)
player.on_chat("wall2",wall2)
def roof(length):
    for count in range(length):
        agent.set_slot(1)
        agent.place(DOWN)
        agent.move(FORWARD, 1)
player.on_chat("roof",roof)

def obsidian(LENGTH):
    for count in range(LENGTH):
        agent.destroy(DOWN)
        agent.collect_all()
        agent.move(FORWARD,1)
mobs.spawn(CHICKEN, pos(0, 0, 0))
player.on_chat("obsidian",obsidian)

def dragon():
    mobs.spawn(ENDER_DRAGON, player.position())

player.on_chat("dragon",dragon)
def block():
    blocks.place(ANCIENT_DEBRIS, player.position())

player.on_chat("block",block)

def ss():
    while agent.inspect_block(DOWN)!=DIAMOND_BLOCK:
        if agent.inspect_block(RIGHT)!=BLUE_CONCRETE:
            agent.turn(TurnDirection.RIGHT)
        
        agent.move(FORWARD,1)

player.on_chat("ss",ss)

def maze():
    while agent.inspect_block(DOWN)!=DIAMOND_BLOCK:
        if not agent.inspect_block(LEFT):
            agent.turn(TurnDirection.LEFT)
        elif not agent.inspect_block(FORWARD):
            agent.move(FORWARD,1)
        else:
            agent.turn(TurnDirection.RIGHT)

player.on_chat("maze",maze)


def down():
    while agent.inspect_block(DOWN):
        agent.destroy(DOWN)
        agent.move(DOWN,1)
player.on_chat("down",down)
