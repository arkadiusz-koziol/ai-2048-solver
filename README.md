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

## 🚀 Getting Started

### 1. Install Requirements

```bash
pip install -r requirements.txt
```
2. Run Training and Testing
```bash
python main.py
```
Trained model will be saved as model.zip. TensorBoard logs are stored in ./logs/.

3. Visualize TensorBoard (optional)
```bash
tensorboard --logdir=logs/
```
📦 Dependencies
```bash
gym
numpy
matplotlib
seaborn
stable-baselines3
torch
tensorboard
```

📈 Example Output
```bash
Live rendering of game board after every move
Training logs with reward plots
Final score summaries for test episodes
```

🧱 Architecture Principles
```bash
SOLID principles applied
Domain-driven design (DDD): clear separation of domain, environment, and interface layers
DRY & KISS: concise and reusable components
```

📬 Contributions
```bash
PRs and issues are welcome. This project is structured to be extended with more agents, UIs, or gameplay enhancements.
```


📝 License
```bash
MIT License

Let me know if you want a corresponding `requirements.txt` as well.
```