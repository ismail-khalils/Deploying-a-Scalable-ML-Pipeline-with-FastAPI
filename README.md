# Deploying a Scalable ML Pipeline with FastAPI

This repository contains code for deploying a scalable machine learning pipeline using FastAPI.

## Environment Setup

You can set up the environment using either pip or conda:

- **Option 1**: Use the supplied file `environment.yml` to create a new environment with conda.
- **Option 2**: Use the supplied file `requirements.txt` to create a new environment with pip.

## Repository Structure

The repository contains the following directories and files:

- `.github/workflows`: Contains GitHub workflows.
- `data`: Contains the data used for training the model.
- `ml`: Contains the machine learning code.
- `model`: Contains the trained model.
- `screenshots`: Contains screenshots related to the project.
- `CODEOWNERS`: File to specify the code owners.
- `LICENSE.txt`: License file.
- `README.md`: This file.
- `environment.yml`: Conda environment file.
- `local_api.py`: Local API file.
- `main.py`: Main Python file.
- `model_card_template.md`: Model card template.
- `requirements.txt`: Requirements file.
- `test_ml.py`: File for testing the machine learning code.
- `train_model.py`: File for training the model.

## Usage

To use this repository, follow these steps:

1. Clone the repository.
2. Set up the environment as described above.
3. Train the model using the `train_model.py` script.
4. Test the model using the `test_ml.py` script.
5. Start the FastAPI server using the `main.py` script.
