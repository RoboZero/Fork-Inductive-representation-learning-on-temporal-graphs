import os
import json
import shlex
from pathlib import Path


# ==========================================================
# ADD / MODIFY YOUR COMMANDS HERE
# ==========================================================
COMMANDS = [
    "python -u learn_edge.py -d synthetic_baseline --node_dim 1 --bs 128 --uniform --n_degree 20 --agg_method attn --attn_mode prod --gpu 0 --n_head 1 --n_epoch 10 --prefix synthetic_baseline_nd1_bs128_ep10",
    "python -u learn_edge.py -d synthetic_baseline --node_dim 1 --bs 128 --uniform --n_degree 20 --agg_method attn --attn_mode prod --gpu 0 --n_head 1 --n_epoch 1 --prefix synthetic_baseline_nd1_bs12_ep1",
    "python -u learn_edge.py -d synthetic_baseline --node_dim 20 --time_dim 40 --bs 1024 --lr 0.001 --uniform  --n_degree 20 --agg_method attn --attn_mode prod --gpu 0 --n_head 1 --n_epoch 50 --prefix synthetic_baseline_nd20_rd40_bs1024_lr0.001_ep50",
    "python -u learn_edge.py -d synthetic_baseline --bs 100 --uniform  --n_degree 20 --agg_method attn --attn_mode prod --gpu 0 --n_head 1 --prefix synthetic_baseline_bs100",
    "python -u learn_edge.py -d synthetic_baseline --uniform  --n_degree 20 --agg_method attn --attn_mode prod --gpu 0 --n_head 1 --prefix synthetic_baseline_default_manual"

    # Add more variations below:
    # "python -u learn_edge.py -d synthetic_baseline --node_dim 20 --bs 200 --uniform --n_degree 20 --agg_method attn --attn_mode prod --gpu 0 --n_head 2 --n_epoch 50 --prefix synthetic_v2",
]


def command_to_config(command: str):
    tokens = shlex.split(command)

    # Remove python and -u
    if tokens[0] == "python":
        tokens = tokens[1:]
    if tokens and tokens[0] == "-u":
        tokens = tokens[1:]

    program = tokens[0]
    args = tokens[1:]

    # Generate readable name from prefix if available
    config_name = "Debug " + program
    if "--prefix" in args:
        prefix_index = args.index("--prefix") + 1
        if prefix_index < len(args):
            config_name = f"Debug {args[prefix_index]}"

    return {
        "name": config_name,
        "type": "debugpy",
        "request": "launch",
        "program": f"${{workspaceFolder}}/{program}",
        "console": "integratedTerminal",
        "args": args,
        "justMyCode": False
    }


def generate_launch_json(commands):
    configs = [command_to_config(cmd) for cmd in commands]

    return {
        "version": "0.2.0",
        "configurations": configs
    }


def write_launch_json(launch_data):
    vscode_dir = Path(".vscode")
    vscode_dir.mkdir(exist_ok=True)

    launch_path = vscode_dir / "launch.json"

    with open(launch_path, "w") as f:
        json.dump(launch_data, f, indent=4)

    print(f"✅ launch.json written to {launch_path.resolve()}")


if __name__ == "__main__":
    launch_json_data = generate_launch_json(COMMANDS)
    write_launch_json(launch_json_data)