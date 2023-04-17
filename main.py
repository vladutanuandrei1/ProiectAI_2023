import gym
import numpy as np

# Create an instance of the environment
env = gym.make('CarRacing-v2')

# Reset the environment to start a new game
observation = env.reset()

# Run a loop to play the game
while True:
    # Render the current state of the game
    env.render()

    # Choose an action to take
    action = env.action_space.sample()

    # Take the chosen action and get the new observation, reward, and done flag
    observation, reward, done, info = env.step(action)

    # If the game is over, break out of the loop
    if done:
        break

# Close the environment
env.close()
