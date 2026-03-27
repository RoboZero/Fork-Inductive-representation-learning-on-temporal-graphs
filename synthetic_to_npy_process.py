import pandas as pd
import numpy as np
import os
import glob
from pathlib import Path

# synthetic_target = "baseline"
# SYNTHETIC_PATH = f"synthetic/synthetic/synthetic_{synthetic_target}/synthetic_{synthetic_target}.csv"
# df = pd.read_csv(SYNTHETIC_PATH)
# target = "reddit"

# synthetic_target_map = [
#     {
#         "group": "baseline", 
#         "path": f"synthetic/synthetic/synthetic_baseline/synthetic_baseline.csv"
#     },
#     {
#         "group": "mask_2B", 
#         "path": f"synthetic\synthetic\synthetic_baseline\mask_2B.csv"
#     },
#     {
#         "group": "mask_4B", 
#         "path": f"synthetic\synthetic\synthetic_baseline\mask_4B.csv"
#     },
#     {
#         "group": "mask_6B", 
#         "path": f"synthetic\synthetic\synthetic_baseline\mask_6B.csv"
#     },
#     {
#         "group": "mask_8B", 
#         "path": f"synthetic\synthetic\synthetic_baseline\mask_8B.csv"
#     },
#     {
#         "group": "mask_10B", 
#         "path": f"synthetic\synthetic\synthetic_baseline\mask_10B.csv"
#     },
#     {
#         "group": "mask_10B", 
#         "path": f"synthetic\synthetic\synthetic_baseline\mask_10B.csv"
#     },
#     {
#         "group": "missing_B", 
#         "path": f"synthetic\synthetic\synthetic_baseline\missing_B.csv"
#     }
# ]

# synthetic_target_map = [
#     {
#         "group": "stress_gene_baseline", 
#         "path": f"synthetic\synthetic\synthetic_stress_gene\synthetic_stress_gene.csv"
#     },
#     {
#         "group": "stress_gene_mask_2A", 
#         "path": f"synthetic\synthetic\synthetic_stress_gene\mask_2A.csv"
#     },
#     {
#         "group": "stress_gene_mask_4A", 
#         "path": f"synthetic\synthetic\synthetic_stress_gene\mask_4A.csv"
#     },
#     {
#         "group": "stress_gene_mask_6A", 
#         "path": f"synthetic\synthetic\synthetic_stress_gene\mask_6A.csv"
#     },
#     {
#         "group": "stress_gene_mask_8A", 
#         "path": f"synthetic\synthetic\synthetic_stress_gene\mask_8A.csv"
#     },
#     {
#         "group": "stress_gene_mask_10A", 
#         "path": f"synthetic\synthetic\synthetic_stress_gene\mask_10A.csv"
#     },
#     {
#         "group": "stress_gene_missing_A", 
#         "path": f"synthetic\synthetic\synthetic_stress_gene\missing_A.csv"
#     }
# ]


# synthetic_target_map = [
#     {
#         "group": "synthetic_stress_time", 
#         "path": f"synthetic\synthetic\synthetic_stress_time\synthetic_stress_time.csv"
#     },
#     {
#         "group": "mask_2C", 
#         "path": f"synthetic\synthetic\synthetic_stress_time\mask_2C.csv"
#     },
#     {
#         "group": "mask_4C", 
#         "path": f"synthetic\synthetic\synthetic_stress_time\mask_4C.csv"
#     },
#     {
#         "group": "mask_6C", 
#         "path": f"synthetic\synthetic\synthetic_stress_time\mask_6C.csv"
#     },
#     {
#         "group": "mask_8C", 
#         "path": f"synthetic\synthetic\synthetic_stress_time\mask_8C.csv"
#     },
#     {
#         "group": "mask_10C", 
#         "path": f"synthetic\synthetic\synthetic_stress_time\mask_10C.csv"
#     },
#     {
#         "group": "missing_C", 
#         "path": f"synthetic\synthetic\synthetic_stress_time\missing_C.csv"
#     }
# ]

# synthetic_target_map = [
#     {
#         "group": "synthetic_stress_system", 
#         "path": f"synthetic\synthetic\synthetic_stress_system\synthetic_stress_system.csv"
#     },
#     {
#         "group": "mask_2D", 
#         "path": f"synthetic\synthetic\synthetic_stress_system\mask_2D.csv"
#     },
#     {
#         "group": "mask_4D", 
#         "path": f"synthetic\synthetic\synthetic_stress_system\mask_4D.csv"
#     },
#     {
#         "group": "mask_6D", 
#         "path": f"synthetic\synthetic\synthetic_stress_system\mask_6D.csv"
#     },
#     {
#         "group": "mask_8D", 
#         "path": f"synthetic\synthetic\synthetic_stress_system\mask_8D.csv"
#     },
#     {
#         "group": "mask_10D", 
#         "path": f"synthetic\synthetic\synthetic_stress_system\mask_10D.csv"
#     },
#     {
#         "group": "missing_D", 
#         "path": f"synthetic\synthetic\synthetic_stress_system\missing_D.csv"
#     }
# ]


synthetic_target_map = [
    # {
    #     "group": "synthetic_stress_gene", 
    #     "path": f"synthetic\synthetic\synthetic_stress_gene\synthetic_stress_gene.csv"
    # },
    {
        "group": "mask_2D", 
        "path": f"synthetic\synthetic\synthetic_stress_gene\mask_2A.csv"
    },
    {
        "group": "mask_4D", 
        "path": f"synthetic\synthetic\synthetic_stress_gene\mask_4A.csv"
    },
    {
        "group": "mask_6D", 
        "path": f"synthetic\synthetic\synthetic_stress_gene\mask_6A.csv"
    },
    {
        "group": "mask_8D", 
        "path": f"synthetic\synthetic\synthetic_stress_gene\mask_8A.csv"
    },
    {
        "group": "mask_10D", 
        "path": f"synthetic\synthetic\synthetic_stress_system\mask_10D.csv"
    }
]


def generate_synthetic_target_map(directory):
    synthetic_target_map = []

    filenames = Path(directory).glob("/*")
    for filename in filenames:
        if filename.is_file():
            synthetic_target_map.append({

            })


def generate_edge_list_csv(synthetic_path):
    target = Path(synthetic_path).stem
    edge_list_path = f"processed/ml_{target}.csv"

    synthetic_labels = ["u", "i", "ts"]
    synthetic_df = pd.read_csv(synthetic_path, header=None, names=synthetic_labels)
    edge_list_labels = ["u", "i", "ts", "label", "idx"]
    edge_list_df: pd.DataFrame = pd.DataFrame(columns=edge_list_labels)
    
    edge_list_df[["u", "i", "ts"]] = synthetic_df[["u", "i", "ts"]].copy()
    edge_list_df["u"] = edge_list_df['u'] + 1
    edge_list_df["i"] = edge_list_df['i'] + 1

    edge_list_df.loc[:, "label"] = 1
    edge_list_df["ts"] = edge_list_df["ts"]
    edge_list_df["ts"] = edge_list_df["ts"].astype('float64')
    edge_list_df = edge_list_df.sort_values(by="ts").reset_index(drop=True)
    edge_list_df["idx"] = [i + 1 for i in range(edge_list_df.shape[0])]

    edge_list_df.to_csv(edge_list_path)
    print(max(edge_list_df.u.max(), edge_list_df.i.max()))
    # print(new_link_df.head())
    print(f"Generated edge list for: {synthetic_path}")


# ml_${DATA_NAME}.npy has shape of [#temporal edges + 1, edge features dimention]. 
# Similarly, ml_${DATA_NAME}_node.npy has shape of [#nodes + 1, node features dimension].
def create_features_random(node_count, feature_dimensions):
    new_node_data = np.random.randn(node_count, feature_dimensions).astype(np.float32)
    return new_node_data

def create_features_onehot_highdim(node_count):
    return np.eye(node_count)

# No benefit to large edge feature vectors unless you have meaningful data.
def create_features_uniform_ones(node_count, feature_count):
    return np.ones((node_count, feature_count), dtype=np.float32)

def create_features_uniform_zeroes(node_count, feature_count):
    return np.zeros((node_count, feature_count), dtype=np.float32)

def generate_node_and_edge_features(synthetic_path, printout=False):
    target = Path(synthetic_path).stem
    node_feature_path = f"processed/ml_{target}_node.npy"
    edge_feature_path = f"processed/ml__{target}.npy"

    if printout:
        np.set_printoptions(suppress=True, precision=6, threshold=np.inf)
        edge_data = np.load(edge_feature_path)
        node_data = np.load(node_feature_path)
        print(np.shape(node_data))
        print(np.shape(edge_data))

    node_count = 400
    node_feature_dim = 100
    
    node_features = create_features_random(node_count + 1, node_feature_dim)
    node_features[0] = 0
    print(np.shape(node_features))
    np.save(node_feature_path, node_features)

    # 40,000 edges to simulate 1 edge per 10 genes. 
    # edge_count = 37960
    edge_count = 3760
    edge_feature_dim = 100
    edge_features = create_features_random(edge_count + 1, edge_feature_dim)
    edge_features[0] = 0 
    print(np.shape(edge_features))
    np.save(edge_feature_path, edge_features)

    print(f"Saved node and edge features for {synthetic_path}")

def generate_edge_list_with_node_and_edge_features_npy(synthetic_path, node_feature_dim):
    target = Path(synthetic_path).stem
    edge_list_path = f"processed/ml_{target}.csv"
    node_feature_path = f"processed/ml_{target}_node.npy"
    edge_feature_path = f"processed/ml__{target}.npy"

    # --- 1. Load your synthetic sparse matrix here ---
    # Assuming 'synthetic_matrix' is a NumPy array of shape (num_edges, 3)
    # Example: synthetic_matrix = np.array([[source, dest, time], ...])
    # g_df = pd.read_csv("synthetic\synthetic\synthetic_baseline\synthetic_baseline.csv".format(DATA), header=None, names=['u', 'i', 'ts'])
    g_df = pd.read_csv(synthetic_path)

    # If you loaded your sparse matrix via Pandas:# g_df = pd.read_csv('./processed/your_synthetic_file.csv') 
    # Convert the whole thing to a NumPy array once to make slicing easy:
    synthetic_matrix = g_df.values # Now this NumPy-style slicing will work perfectly:
    src_l_raw = synthetic_matrix[:, 0].astype(int)
    dst_l_raw = synthetic_matrix[:, 1].astype(int)
    ts_l_raw  = synthetic_matrix[:, 2].astype(int)

    # --- 2. Enforce TGAT's 1-Based Indexing Rule ---
    # TGAT reserves index 0 for "null" or "padding" nodes/edges.
    # If your synthetic nodes start at 0, we must shift them up by 1.
    if src_l_raw.min() == 0 or dst_l_raw.min() == 0:
        src_l_raw += 1
        dst_l_raw += 1

    # --- 3. Chronological Sorting (CRITICAL) ---
    # The model must process events in strict time order to prevent data leakage.
    sort_idx = np.argsort(ts_l_raw)
    src_l = src_l_raw[sort_idx]
    dst_l = dst_l_raw[sort_idx]
    ts_l = ts_l_raw[sort_idx]

    num_edges = len(src_l)
    max_node_id = max(src_l.max(), dst_l.max())

    # --- 4. Generate Edge Indices and Labels ---
    e_idx_l = np.arange(1, num_edges + 1) # Must start at 1
    label_l = np.ones(num_edges)          # 1 means observed edge

    edge_list_df = pd.DataFrame({
        'u': src_l,
        'i': dst_l,
        'ts': ts_l,
        'label': label_l,
        'idx': e_idx_l
    })
    edge_list_df.to_csv(edge_list_path)

    # --- 5. Generate Features (Fixes your Dimension Errors) ---
    # We use NODE_DIM (from your argparse) to ensure the tensor shapes exactly 
    # match what the Attention layers are initialized to expect.
    print(f'Generating features with Node/Edge Dim: {node_feature_dim}')

    # +1 is required because index 0 is the null/padding vector
    n_feat = np.random.randn(max_node_id + 1, node_feature_dim).astype(np.float32)
    n_feat[0] = 0  

    # Ensure edge features match node features in dimension
    e_feat = np.random.randn(num_edges + 1, node_feature_dim).astype(np.float32)
    e_feat[0] = 0  

    # --- 6. Set Time Splits ---
    val_time, test_time = list(np.quantile(ts_l, [0.70, 0.85]))

    max_src_index = src_l.max()
    max_idx = max_node_id

    print(f'Successfully loaded {max_node_id} nodes and {num_edges} temporal edges.')

    np.save(node_feature_path, n_feat)
    np.save(edge_feature_path, e_feat)


# Run
for item in synthetic_target_map:
    generate_edge_list_csv(item["path"])
    # generate_node_and_edge_features(item["path"])
    # generate_edge_list_with_node_and_edge_features_npy(item["path"], 100)

# pd.read_csv("ml_reddit")

# generate_synthetic_target_map("synthetic/synthetic")