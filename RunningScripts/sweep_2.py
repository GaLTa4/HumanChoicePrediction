import wandb
YOUR_WANDB_USERNAME = "galtamar"
project = "Strategy_Transfer_TACL"

command = [
        "${ENVIRONMENT_VARIABLE}",
        "${interpreter}",
        "StrategyTransfer.py",
        "${project}",
        "${args}"
    ]


sweep_config = {
    "name": "LSTM: SimFactor=0/4 for any features representation 3",
    "method": "grid",
    # "metric": {
    #     "goal": "maximize",
    #     "name": "AUC.test.max"
    # },
    "parameters": {
        "ENV_HPT_mode": {"values": [False]},
        "architecture": {"values": ["LSTM"]},
        "online_simulation_factor": {"values": [0, 1, 2, 4]},
        "basic_nature": {"values": [10]},
        "seed": {"values": list(range(1, 4))},
        # "features": {"values": ["EFs", "GPT4"]},
    },
    "command": command
}

# Initialize a new sweep
sweep_id = wandb.sweep(sweep=sweep_config, project=project)
print("run this line to run your agent in a screen:")
print(f"screen -dmS \"sweep_agent\" wandb agent {YOUR_WANDB_USERNAME}/{project}/{sweep_id}")
