#!/bin/bash

# Check if Conda is installed
if ! command -v conda &> /dev/null; then
    echo "Conda is not installed. Please install Conda before proceeding."
    exit 1
fi

# Environment name (change this if needed)
ENV_NAME="venv"

# Create the Conda environment
echo "Creating Conda environment: $ENV_NAME..."
conda create -p -n $ENV_NAME python=3.12 -y # Adjust Python version as needed

# Activate the environment
echo "Activating Conda environment..."
source $(conda info --base)/etc/profile.d/conda.sh
conda activate $ENV_NAME

# Install dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "No environment.yml or requirements.txt found. Skipping dependency installation."
fi

echo "Setup complete! Activate the environment with: conda activate $ENV_NAME"
