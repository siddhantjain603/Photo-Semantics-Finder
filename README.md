# Photo Semantics Finder

## Overview

Photo Semantics Finder is a web application that uses a machine learning model to generate descriptive text (semantics) from images. It utilizes the BLIP (Bootstrapped Language-Image Pre-training) image captioning model to analyze the content of uploaded photos and provide a textual description.

## Files

- **`photo_semantics.py`**: Main script that sets up the Streamlit interface, loads the BLIP model, and generates semantics from images.
- **`requirements.txt`**: Lists the Python dependencies required for the project.

## Setup

### 1. Clone the Repository

- git clone https://github.com/siddhantjain603/Photo-Semantics-Finder.git
- cd Photo-Semantics-Finder

### 2. Install Dependencies

- pip install -r requirements.txt

### 3. Run the Application

- streamlit run photo_semantics.py

## Usage

### 1. Upload an Image

- Click the "Choose a photo" button.
- Select an image file (supported formats: JPG, JPEG, PNG).

### 2. Generate Semantics

- Click the "Generate Semantics" button.
- The application will process the image and display a textual description of the image content.
