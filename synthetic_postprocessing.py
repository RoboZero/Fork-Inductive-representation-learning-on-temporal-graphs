import pandas as pd
import numpy as np
import os
import glob
from pathlib import Path

# Done
# synthetic_target_map = [
#     # {
#     #     "group": "baseline", 
#     #     "path": f"predicted_edges_synthetic_baseline_synthetic_baseline.csv"
#     # },
#     {
#         "group": "mask_2B", 
#         "path": f"predicted_edges_mask_2B_mask_2B_default.csv"
#     },
#     {
#         "group": "mask_4B", 
#         "path": f"predicted_edges_mask_4B_mask_4B_default.csv"
#     },
#     {
#         "group": "mask_6B", 
#         "path": f"predicted_edges_mask_6B_mask_6B_default.csv"
#     },
#     {
#         "group": "mask_8B", 
#         "path": f"predicted_edges_mask_8B_mask_8B_default.csv"
#     },
#     {
#         "group": "mask_10B", 
#         "path": f"predicted_edges_mask_10B_mask_10B_default.csv"
#     },
#     # {
#     #     "group": "missing_B", 
#     #     "path": f"synthetic\synthetic\synthetic_baseline\missing_B.csv"
#     # }
# ]

# Done
# synthetic_target_map = [
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

# Not done
synthetic_target_map = [
    {
        "group": "synthetic_stress_time", 
        "path": f"synthetic\synthetic\synthetic_stress_time\synthetic_stress_time.csv"
    },
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
]


# synthetic_target_map = [
#     {
#         "group": "synthetic_stress_time", 
#         "path": f"synthetic\synthetic\synthetic_stress_time\synthetic_stress_time.csv"
#     },
#     {
#         "group": "mask_2D", 
#         "path": f"predicted_edges_mask_2D_mask_2D_default.csv"
#     },
#     {
#         "group": "mask_4D", 
#         "path": f"predicted_edges_mask_4D_mask_4D_default.csv"
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
#         "group": "mask_10D", 
#         "path": f"predicted_edges_mask_10D_mask_10D_default.csv"
#     },
#     {
#         "group": "missing_C", 
#         "path": f"synthetic\synthetic\synthetic_stress_time\missing_C.csv"
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


def postprocess(synthetic_path):
    edge_list_df = pd.read_csv(synthetic_path, header=None, names=["u", "i", "ts"])
    print(edge_list_df)
    edge_list_df["u"] = edge_list_df['u'] - 1
    edge_list_df["i"] = edge_list_df['i'] - 1
    print(edge_list_df)

    edge_list_df.to_csv(synthetic_path, header=False, index=False)


for item in synthetic_target_map:
    postprocess(item["path"])