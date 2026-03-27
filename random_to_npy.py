import pandas as pd
import numpy as np

# Here’s a safe synthetic generator: (will it work?)

target = "random"

edge_list_path = f"processed/ml_{target}.csv"
node_feature_path = f"processed/ml_{target}_node.npy"
edge_feature_path = f"processed/ml__{target}.npy"

num_nodes = 400
num_edges = 40000

edges = []
for t in range(num_edges):
    u = np.random.randint(0, num_nodes)
    v = (u + np.random.randint(1, 5)) % num_nodes  # local connectivity
    edges.append([u, v, float(t), 1, t])

df = pd.DataFrame(edges, columns=["u","i","ts","label","idx"])
df.to_csv(edge_list_path)

def create_features_random(node_count, feature_dimensions):
    new_node_data = np.random.randn(node_count, feature_dimensions).astype(np.float32)
    return new_node_data

node_feature_dim = 1
edge_feature_dim = 1 
node_features = np.random.randn(num_nodes, node_feature_dim).astype(np.float32)
edge_features = np.random.randn(num_edges, edge_feature_dim).astype(np.float32)

node_features = create_features_random(num_nodes + 1, node_feature_dim)
edge_features = create_features_random(num_edges + 1, edge_feature_dim)
# node_features[0] = 0
print(np.shape(node_features))
np.save(node_feature_path, node_features)
np.save(edge_feature_path, edge_features)