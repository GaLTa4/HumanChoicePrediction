# Improving Human Choice Prediction in Language-based Persuasion Games:
Leveraging Advanced NLP Techniques for Simulation

## Getting Started


### Prerequisites

Before you begin, ensure you have the following tools installed on your system:
- Git
- Anaconda or Miniconda

### Installation

To install and run the code on your local machine, follow these steps:

1. **Clone the repository**

   First, clone the repository to your local machine using Git. Open a terminal and run the following command:
   ```bash
   git clone https://github.com/GaLTa4/HumanChoicePrediction.git
    ```
2. **Create and activate the conda environment**

    After cloning the repository, navigate into the project directory:

    ```bash
    cd HumanChoicePrediction
    ```

    Then, use the following command to create a conda environment from the requirements.yml file provided in the project:
    ```bash
    conda env create -f requirements.yml
    ```
3. **Log in to Weights & Biases (W&B)**

   Weights & Biases is a machine learning platform that helps you track your experiments, visualize data, and share your findings. Logging in to W&B is essential for tracking the experiments in this project. If you haven't already, you'll need to create a W&B account. 
   Use the following command to log in to your account:
    ```bash
    wandb login
    ```

### How to create our baseline file for simulations
1. Navigate into the right directory:

    ```bash
    cd RunningScripts/CreatingBaselineForSimulation
    ```
2. Run the 'final_project_NLP.ipynb' file

Note: We supplied pkl files (in 'CreatingBaselineForSimulation' folder) that were created during different parts of the code, so you don't need to run the entire notebook to get the baseline file. 