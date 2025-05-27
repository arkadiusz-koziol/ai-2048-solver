# 2048 Game - Reinforcement Learning Agent with PPO

This project implements a reinforcement learning agent using Proximal Policy Optimization (PPO) to play the 2048 game. The codebase follows clean architecture principles for scalability and maintainability.

---

## 🧠 Features

- PPO agent using `stable-baselines3`
- Custom OpenAI Gym environment
- Modular architecture with domain, service, and environment layers
- Real-time training visualization using seaborn/matplotlib
- TensorBoard logging support

---

## 🗂️ Project Structure

.
├── domain/
│ ├── game_2048.py # Game logic and core mechanics
│ └── value_objects.py # Board abstraction as a value object
├── envs/
│ └── simple_2048_env.py # Gym environment wrapper for 2048
├── logs/ # PPO training logs (auto-generated)
├── main.py # Training & testing PPO agent
└── README.md


---

## 🚀 Getting Started

### 1. Install Requirements

```bash
pip install -r requirements.txt
2. Run Training and Testing
python main.py
Trained model will be saved as model.zip. TensorBoard logs are stored in ./logs/.

3. Visualize TensorBoard (optional)
tensorboard --logdir=logs/
📦 Dependencies

gym
numpy
matplotlib
seaborn
stable-baselines3
torch
tensorboard
📈 Example Output

Live rendering of game board after every move
Training logs with reward plots
Final score summaries for test episodes
🧱 Architecture Principles

SOLID principles applied
Domain-driven design (DDD): clear separation of domain, environment, and interface layers
DRY & KISS: concise and reusable components
📬 Contributions

PRs and issues are welcome. This project is structured to be extended with more agents, UIs, or gameplay enhancements.

📝 License

MIT License


Let me know if you want a corresponding `requirements.txt` as well.