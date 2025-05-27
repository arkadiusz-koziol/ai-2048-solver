# file: main.py
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from stable_baselines3 import PPO
from stable_baselines3.common.logger import configure
from envs.simple_2048_env import Simple2048Env

log_path = "./logs/"
new_logger = configure(log_path, ["stdout", "tensorboard"])

env = Simple2048Env()
model = PPO("MlpPolicy", env, verbose=1)
model.set_logger(new_logger)

model.learn(total_timesteps=100_000)
model.save("model")

plt.ion()
fig = plt.figure(figsize=(5, 5))

def render_board(board: np.ndarray, episode: int = None, step: int = None, score: int = None):
    plt.clf()
    sns.heatmap(
        board,
        annot=True,
        fmt="d",
        cmap="YlOrRd",
        cbar=False,
        linewidths=0.5,
        square=True,
        linecolor="gray"
    )
    title = f"Episode: {episode + 1}, Step: {step}, Score: {score}, Max: {np.max(board)}"
    plt.title(title)
    plt.pause(0.2)

print("\n=== TESTING TRAINED AGENT ===\n")
scores = []

for episode in range(5):
    obs = env.reset()
    done = False
    score = 0
    step = 0

    while not done:
        action, _ = model.predict(obs)
        obs, reward, done, _ = env.step(action)
        score += reward
        render_board(obs, episode, step, score)
        step += 1

    scores.append(score)
    print(f"Episode {episode + 1}: score = {score}")

plt.ioff()
plt.figure(figsize=(6, 4))
plt.plot(scores, marker="o")
plt.title("Wynik agenta PPO w epizodach testowych")
plt.xlabel("Epizod")
plt.ylabel("Suma nagród (score)")
plt.grid(True)
plt.tight_layout()
plt.show()
