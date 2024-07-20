# News Generation with GPT-Neo 125M

This project demonstrates the fine-tuning and deployment of the EleutherAI GPT-Neo 125M model for generating news articles. The dataset used for training is the "All the News" dataset from Kaggle, covering the period from 2015 to 2020. The project includes a Flask web application that allows users to generate fake news without needing to train the model themselves.

 <!-- DISPLAY=TRUE -->




## Overview

- **Model:** EleutherAI GPT-Neo 125M
- **Dataset:** All the News dataset from Kaggle
- **Framework:** Hugging Face Transformers
- **Web Framework:** Flask
- **Purpose:** Generate fake news articles from 2015 to 2020
- **Computational Requirements:** Not very intensive, suitable for an introduction to Hugging Face

## Features

1. **Model Fine-Tuning:** Detailed methodology and code for fine-tuning the GPT-Neo 125M model.
2. **Web Application:** A simple Flask web app for generating news articles without training.
3. **Dataset:** Focused on news articles from 2015 to 2020.

## Methodology

The methodology for fine-tuning the GPT-Neo 125M model on the "All the News" dataset is documented in detail in the included Jupyter notebooks and Python scripts. This includes:

1. **Data Preprocessing:** Cleaning and preparing the dataset for training.
2. **Model Training:** Fine-tuning the GPT-Neo 125M model using Hugging Face Transformers.
3. **Evaluation:** Assessing the model's performance and generating sample outputs.

## Getting Started

### Prerequisites

- Python 3.7+
- Pip
- Virtual environment (recommended)

### Installation

1. **Install Requirements**

   ```bash
   pip install -r requirements.txt

