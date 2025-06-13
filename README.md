<!-- Project Title and Badges -->
<p align="center">
  <strong>🚨 Smart-City CCTV Violence Detection System</strong>
</p>

<p align="center">
  <a href="https://github.com/Krishna-pathak1535/smart-city-violence-detection">
    <img src="https://img.shields.io/github/stars/Krishna-pathak1535/smart-city-violence-detection?style=social" alt="GitHub Stars" />
  </a>
  <a href="https://github.com/Krishna-pathak1535/smart-city-violence-detection">
    <img src="https://img.shields.io/github/forks/Krishna-pathak1535/smart-city-violence-detection?style=social" alt="GitHub Forks" />
  </a>
  <a href="https://github.com/Krishna-pathak1535/smart-city-violence-detection/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python" alt="Python Version" />
  <img src="https://img.shields.io/badge/TensorFlow-GPU-orange?style=for-the-badge&logo=tensorflow" alt="TensorFlow GPU" />
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit" alt="Streamlit App" />
  <img src="https://img.shields.io/badge/OpenCV-Python-green?style=for-the-badge&logo=opencv" alt="OpenCV" />
</p>

---

## ✨ Project Overview

An **AI-driven solution for Smart-City CCTV Violence Detection** that automatically identifies and classifies events as **Normal**, **Violence**, or **Weaponized** in surveillance video streams. This system provides **proactive alerts** to monitoring personnel, enhancing public safety in urban environments.

---

## 🚀 System Architecture

1. **Video Ingestion Module**  
   Web interface for uploading common formats (AVI, MP4).

2. **AI Core (CNN-LSTM Model)**  
   Combines Convolutional Neural Network with LSTM for spatio-temporal feature extraction and classifies clips into three categories.

3. **Real-time Prediction & Alerting**  
   Displays predictions (label + confidence) in the UI and triggers visual alerts for detected threats.

4. **Interactive Web UI**  
   Built with Streamlit for easy upload, playback, and visualization.

---

## 🛠️ Technical Approach

- **Deep Learning Model**: CNN-LSTM for spatial and temporal analysis.  
- **Data Handling**: Custom `Keras Sequence` data generator for efficient batch loading on Google Colab GPUs.  
- **Video Preprocessing**: `FFmpeg` to transcode inputs to MP4 (H.264/AAC) for browser compatibility.  
- **UI Development**: Streamlit for rapid, responsive front-end.  
- **Version Control**: Git + Git LFS for large model artifacts; Python `venv` for dependency management.

---

## 🎬 Demo

Run locally:

```bash
streamlit run app.py
```

<p align="center">
  <img src="assets/app_demo.gif" alt="App Demo" width="600"/>
</p>

---

## **Key Screenshots**

<p align="center">
  <img src="assets/initial_ui_screenshot.png" alt="Initial App UI Screenshot" width="600"/>
  <br><em>The clean, inviting interface ready for video upload.</em>
</p>

<p align="center">
  <img src="assets/video_playback_after_upload.png" alt="Video Playback Screenshot" width="600"/>
  <br><em>Video playing seamlessly after upload.</em>
</p>

<p align="center">
  <img src="assets/prediction_normal_result.png" alt="Prediction Result Normal Screenshot" width="600"/>
  <br><em>Example of a 'Normal' activity prediction with high confidence.</em>
</p>

<p align="center">
  <img src="assets/prediction_violence_alert.png" alt="Prediction Result Alert Screenshot" width="600"/>
  <br><em>Critical alert for detected violence activity.</em>
</p>

<p align="center">
  <img src="assets/prediction_weaponized_alert.png" alt="Prediction Result Weaponized Alert Screenshot" width="600"/>
  <br><em>Alternative alert for weaponized activity detection.</em>
</p>

---

## 💻 Dataset

**Smart-City CCTV Violence Detection Dataset (SCVD)**  
- **Source**: https://www.kaggle.com/datasets/toluwaniaremu/smartcity-cctv-violence-detection-dataset-scvd  
- Includes original and split segments for flexible processing.

---

## 👋 Contributing

Contributions are welcome! Fork, issue, or PR. For major changes, please open an issue first to discuss.

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE).

---

## 📧 Contact

**GitHub:** [Krishna-pathak1535](https://github.com/Krishna-pathak1535)  
**LinkedIn:** [krishnanand-pathak](https://www.linkedin.com/in/krishnanand-pathak/)  
**Email:** krishna.pathak2003@gmail.com  
