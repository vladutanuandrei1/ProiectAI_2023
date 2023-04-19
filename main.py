import gymnasium
import numpy as np
import agent
import cv2
import os

# Initializare Environment

env = gymnasium.make("CarRacing-v2", render_mode="human")
a = np.array([0.0, 0.0, 0.0])



quit = False
while not quit:
        env.reset()
        # np.savetxt("output.csv", env.render(), '')
        total_reward = 0.0
        steps = 0
        restart = False
        while True:
            a =  agent.tokyoDrift(a)
            s, r, terminated, truncated, info = env.step(a)
            
            total_reward += r
            if steps % 200 == 0 or terminated or truncated:
                print("\naction " + str([f"{x:+0.2f}" for x in a]))
                print(f"step {steps} total_reward {total_reward:+0.2f}")
                # print("##########################################")
                # print(env.render())
                # print("##########################################")
            steps += 1
            if terminated or truncated or restart or quit:
                break
env.close()


#STUPID IDEA
# Make a Main Menu where the player can chose if want to play with keyboard or agent