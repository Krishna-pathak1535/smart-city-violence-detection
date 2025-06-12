# 🚨 Smart-City CCTV Violence Detection System

[![GitHub Stars](https://img.shields.io/github/stars/Krishna-pathak1535/smart-city-violence-detection?style=social)](https://github.com/Krishna-pathak1535/smart-city-violence-detection)
[![GitHub Forks](https://img.shields.io/github/forks/Krishna-pathak1535/smart-city-violence-detection?style=social)](https://github.com/Krishna-pathak1535/smart-city-violence-detection)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/Krishna-pathak1535/smart-city-violence-detection/blob/main/LICENSE)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/TensorFlow-GPU-orange?style=for-the-badge&logo=tensorflow" alt="TensorFlow GPU">
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit" alt="Streamlit App">
  <img src="https://img.shields.io/badge/OpenCV-Python-green?style=for-the-badge&logo=opencv" alt="OpenCV">
</p>

## ✨ Project Overview

This project delivers an **AI-driven solution for Smart-City CCTV Violence Detection**, aimed at significantly enhancing public safety. Its core function is to automatically identify and classify critical events such as "Violence" and "Weaponized" situations within surveillance video streams, distinguishing them from "Normal" activities. The system is engineered to provide **proactive alerts** and offer vital assistance to monitoring personnel in bustling urban environments.

---

## 🚀 Proposed System Architecture

Our system is structured as an end-to-end video analysis pipeline, designed for efficiency and clarity:

1.  **Video Ingestion:**
    Accepts various video formats (AVI, MP4) through an intuitive, user-friendly web interface.

2.  **AI Core (CNN-LSTM Model):**
    The heart of the system, this component processes incoming video frames. It leverages spatio-temporal feature extraction to accurately classify video segments into one of the predefined categories.

3.  **Real-time Prediction & Alerting:**
    Provides instantaneous prediction results (category and confidence score) directly on the web interface, complemented by immediate visual alerts for detected threats.

4.  **Web-based User Interface:**
    A modern, interactive Streamlit application serving as the front-end. It simplifies video upload, enables seamless playback, and provides clear visualization of AI-generated predictions.

---

## 🛠️ How We Built It (Technical Deep Dive)

The development of this sophisticated system unfolded across several critical phases:

* **Dataset Acquisition:**
    Utilized the comprehensive **Smart-City CCTV Violence Detection Dataset (SCVD)**, a large collection of categorized video clips, meticulously sourced from Kaggle.
    * **Dataset Source:** [https://www.kaggle.com/datasets/toluwaniaremu/smartcity-cctv-violence-detection-dataset-scvd](https://www.kaggle.com/datasets/toluwaniaremu/smartcity-cctv-violence-detection-dataset-scvd)

* **Model Architecture:**
    A hybrid **Convolutional Neural Network (CNN)** combined with a **Long Short-Term Memory (LSTM)** network was meticulously chosen. The CNN component excels at extracting salient spatial features from individual video frames, while the LSTM layer intelligently captures the temporal dynamics and sequential patterns crucial for discerning different activities across time.

* **Training & Optimization:**
    The model underwent intensive training in **Google Colab**, harnessing its powerful GPU capabilities. A significant challenge inherent in processing large video datasets—high RAM consumption—was elegantly overcome by implementing **Keras `Sequence` data generators**. These generators efficiently load and preprocess video frames in small batches on-the-fly, effectively preventing out-of-memory errors and ensuring smooth training.

* **Video Preprocessing:**
    Addressing the challenge of varying video codecs and formats (e.g., AVI files often containing codecs incompatible with standard web playback), **FFmpeg** was integrated as a crucial transcoding tool. It ensures all videos are converted into a universally compatible MP4 (H.264/AAC) format, guaranteeing seamless playback within the web application.

* **User Interface Development:**
    A sleek, intuitive, and highly interactive web application was crafted using **Streamlit**. This provides users with a simple drag-and-drop interface for video uploads, integrated video playback, and exceptionally clear display of AI-generated predictions.

* **Dependency Management:**
    A dedicated Python **virtual environment (`venv`)** was meticulously employed to isolate all project dependencies, ensuring a clean, consistent, and reproducible setup across different environments. For handling the large `.h5` model file during version control, **Git Large File Storage (Git LFS)** was implemented, allowing efficient tracking without bloating the Git history.

---

## 🎬 Demo

Witness the Smart-City CCTV Violence Detection System in action by running the `app.py` script locally!

```bash
streamlit run app.py
