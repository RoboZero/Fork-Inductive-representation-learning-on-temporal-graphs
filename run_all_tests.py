import subprocess
import shlex
from pathlib import Path

# synthetic_target_map = [
#     {
#         "group": "synthetic_baseline", 
#         "path": f"synthetic/synthetic/synthetic_baseline/synthetic_baseline.csv"
#     },
    # {
    #     "group": "mask_2B", 
    #     "path": f"synthetic\synthetic\synthetic_baseline\mask_2B.csv"
    # },
    # {
    #     "group": "mask_4B", 
    #     "path": f"synthetic\synthetic\synthetic_baseline\mask_4B.csv"
    # },
    # {
    #     "group": "mask_6B", 
    #     "path": f"synthetic\synthetic\synthetic_baseline\mask_6B.csv"
    # },
    # {
    #     "group": "mask_8B", 
    #     "path": f"synthetic\synthetic\synthetic_baseline\mask_8B.csv"
    # },
    # {
    #     "group": "mask_10B", 
    #     "path": f"synthetic\synthetic\synthetic_baseline\mask_10B.csv"
    # },
    # {
    #     "group": "mask_10B", 
    #     "path": f"synthetic\synthetic\synthetic_baseline\mask_10B.csv"
    # },
    # {
    #     "group": "missing_B", 
    #     "path": f"synthetic\synthetic\synthetic_baseline\missing_B.csv"
    # }
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
#     }
    # {
    #     "group": "mask_2C", 
    #     "path": f"synthetic\synthetic\synthetic_stress_time\mask_2C.csv"
    # },
    # {
    #     "group": "mask_4C", 
    #     "path": f"synthetic\synthetic\synthetic_stress_time\mask_4C.csv"
    # },
    # {
    #     "group": "mask_6C", 
    #     "path": f"synthetic\synthetic\synthetic_stress_time\mask_6C.csv"
    # },
    # {
    #     "group": "mask_8C", 
    #     "path": f"synthetic\synthetic\synthetic_stress_time\mask_8C.csv"
    # },
    # {
    #     "group": "mask_10C", 
    #     "path": f"synthetic\synthetic\synthetic_stress_time\mask_10C.csv"
    # },
    # {
    #     "group": "missing_C", 
    #     "path": f"synthetic\synthetic\synthetic_stress_time\missing_C.csv"
    # }
# ]


# synthetic_target_map = [
    # {
    #     "group": "synthetic_stress_system", 
    #     "path": f"synthetic\synthetic\synthetic_stress_system\synthetic_stress_system.csv"
    # },
    # {
    #     "group": "mask_2D", 
    #     "path": f"synthetic\synthetic\synthetic_stress_system\mask_2D.csv"
    # },
    # {
    #     "group": "mask_4D", 
    #     "path": f"synthetic\synthetic\synthetic_stress_system\mask_4D.csv"
    # },
    # {
    #     "group": "mask_6D", 
    #     "path": f"synthetic\synthetic\synthetic_stress_system\mask_6D.csv"
    # },
    # {
    #     "group": "mask_8D", 
    #     "path": f"synthetic\synthetic\synthetic_stress_system\mask_8D.csv"
    # },
    # {
    #     "group": "mask_10D", 
    #     "path": f"synthetic\synthetic\synthetic_stress_system\mask_10D.csv"
    # },
    # {
    #     "group": "missing_D", 
    #     "path": f"synthetic\synthetic\synthetic_stress_system\missing_D.csv"
    # }
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

def target_to_command(object):
    target = Path(object["path"]).stem
    group = object["group"]
    command = f"python -u learn_edge.py -d {target} --uniform  --n_degree 20 --agg_method attn --attn_mode prod --gpu 0 --n_head 1 --prefix {target}_default"
    return command

for item in synthetic_target_map:
    command = target_to_command(item)
    subprocess.run(shlex.split(command), check=True)