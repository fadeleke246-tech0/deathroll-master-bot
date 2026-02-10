from bot.brain import Brain
import time

brain = Brain()

print(brain.think())

brain.set_state("scanning")
print(brain.think())

time.sleep(2)

brain.set_state("posting")
print(brain.think())
