import json
import random
import datetime

facts = [
    "PyTorch utilizes dynamic computational graphs, making it highly flexible for deep learning research.",
    "Graph Neural Networks (GNNs) are powerful tools for modeling relational data and building complex recommender systems.",
    "Attention mechanisms fundamentally changed how sequence-to-sequence models process context.",
    "Docker containers ensure consistency across different deployment environments, solving the 'it works on my machine' problem."
]

data = {
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC"),
    "fact": random.choice(facts),
    "author": "Milynx"
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

print(f"Updated data.json at {data['last_updated']}")