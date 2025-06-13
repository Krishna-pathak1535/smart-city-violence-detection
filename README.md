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


Markdown

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
Showcase your app's live capabilities here with compelling visuals:

Animated GIF/Short Video (Highly Recommended!): A concise GIF or a brief video demonstrating the entire workflow (upload, playback, prediction) is paramount for immediate impact.

&lt;p align="center">
&lt;img src="assets/images/app_demo.gif" alt="Smart-City Violence Detection App Demo">
&lt;/p>

Key Screenshots:

Initial UI:

&lt;p align="center">
&lt;img src="assets/images/initial_ui.png" alt="Initial App UI Screenshot">
&lt;br>&lt;em>The clean, inviting interface ready for video upload.&lt;/em>
&lt;/p>

Video Playback & Awaiting Analysis:

&lt;p align="center">
&lt;img src="assets/images/video_playback.png" alt="Video Playback Screenshot">
&lt;br>&lt;em>Video playing seamlessly before triggering AI analysis.&lt;/em>
&lt;/p>

Prediction Result (e.g., Normal):

&lt;p align="center">
&lt;img src="assets/images/prediction_normal.png" alt="Prediction Result Normal Screenshot">
&lt;br>&lt;em>Example of a 'Normal' activity prediction with high confidence.&lt;/em>
&lt;/p>

Prediction Result (e.g., Violence/Weaponized Alert):

&lt;p align="center">
&lt;img src="assets/images/prediction_violence_alert.png" alt="Prediction Result Alert Screenshot">
&lt;br>&lt;em>Critical alert for detected violence or weaponized activity.&lt;/em>
&lt;/p>

⚙️ Technical Architecture
Frontend (Web UI): &lt;b style="color:#4fc3f7;">Streamlit&lt;/b>
Deep Learning Framework: &lt;b style="color:#00e676;">TensorFlow&lt;/b> / &lt;b style="color:#00e676;">Keras&lt;/b>
Video Processing: &lt;b style="color:#ff6f61;">OpenCV (cv2)&lt;/b>
Data Serialization: &lt;b style="color:#17a2b8;">NumPy&lt;/b>
Video Transcoding: &lt;b style="color:#007bff;">FFmpeg&lt;/b>
Dependency Management: &lt;b style="color:#e0e0e0;">Python venv&lt;/b>
Version Control for Large Files: &lt;b style="color:#a0a0a0;">Git Large File Storage (Git LFS)&lt;/b>
📦 Dataset
This project is robustly built upon the Smart-City CCTV Violence Detection Dataset (SCVD).

Dataset Source: https://www.kaggle.com/datasets/toluwaniaremu/smartcity-cctv-violence-detection-dataset-scvd

Description: A comprehensive collection of video clips meticulously categorized for violence detection, providing a solid foundation for both model training and thorough evaluation. The dataset includes both original and second-split (shorter segments) versions, offering flexibility in data processing.

💻 Local Setup Guide
Follow these steps precisely to set up and run the Streamlit web application on your local machine.

1. Prerequisites
Ensure you have these installed:

Python 3.8+: Download from python.org.

Git: Download from git-scm.com.

FFmpeg: Essential for video format compatibility.

Open PowerShell and install via winget:

PowerShell

winget install "FFmpeg (Essentials Build)"
2. Clone the Repository
First, ensure Git LFS is installed globally, then clone the project.

PowerShell

# Step 2.1: Install Git LFS system-wide (if not already done)
# Run PowerShell as Administrator for this command
git lfs install

# Step 2.2: Navigate to your desired parent directory
# For example, to clone onto your Desktop:
cd C:\Users\Krish\OneDrive\Desktop\

# Step 2.3: Clone the repository (replace with your actual repo URL)
git clone [https://github.com/Krishna-pathak1535/smart-city-violence-detection.git](https://github.com/Krishna-pathak1535/smart-city-violence-detection.git)

# Step 2.4: Navigate into the cloned project directory
cd "smart-city-violence-detection"
3. Create and Activate a Virtual Environment
Using a virtual environment is crucial for dependency isolation.

PowerShell

# Create the virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate
(Your PowerShell prompt should change to (venv) PS ...>)

4. Install Project Dependencies
Install all required Python packages within your activated virtual environment.

PowerShell

pip install tensorflow opencv-python numpy scikit-learn streamlit tqdm
5. Prepare Sample Videos for Testing
The dataset videos are originally AVI, which may not play in web browsers. You'll need to convert them to MP4 for optimal playback in the Streamlit app.

Download Sample Videos (from your Colab session):
You can download a batch of 50 random videos per category (150 total) from your Google Colab notebook (from Phase 1.13 in your Colab setup).

Download the random_50_videos_per_category.zip file.

Extract its contents into a subfolder within your project directory, e.g., .\sample_videos_for_testing.

Convert .avi to .mp4 using FFmpeg:
Navigate to the directory where your downloaded .avi sample videos are located (e.g., cd ".\sample_videos_for_testing").
Then, run this command to convert all .avi files in that folder and its subfolders to .mp4:

PowerShell

Get-ChildItem -Path . -Recurse -Include *.avi | ForEach-Object {
    $inputPath = $_.FullName
    $outputPath = Join-Path $_.Directory.FullName ($_.BaseName + "-converted.mp4")
    Write-Host "Converting $($_.Name)..."
    ffmpeg -i "$inputPath" -c:v libx264 -preset medium -crf 23 -c:a aac -b:a 128k -vf format=yuv420p "$outputPath" -y
    Write-Host "Converted to $($outputPath)"
}
Write-Host "All conversions complete!"
This will create -converted.mp4 versions of your videos alongside the originals.

Clean Up Original .avi Files (Optional):
Once all conversions are done, you can delete the original .avi files to save disk space:

PowerShell

Get-ChildItem -Path . -Recurse -Include *.avi | Remove-Item -Force
6. Run the Streamlit Application
Ensure your virtual environment is active, then launch the Streamlit app.

PowerShell

# If you changed directory for video conversion, navigate back to the root of your project
# e.g., cd C:\Users\Krish\OneDrive\Desktop\smart-city-violence-detection

# Ensure venv is active
.\venv\Scripts\activate

# Run the Streamlit application
streamlit run app.py
This command will start a local server, and your web browser should automatically open a new tab at http://localhost:8501, displaying the Smart-City CCTV Violence Detection System UI.

💡 Usage
Upload Video: On the web UI, use the "Select a video file to analyze" button or simply drag and drop an .mp4 video file (preferably one you converted from the dataset for testing).

Video Playback: The uploaded video will appear in the "Uploaded Video Stream" section and should start playing automatically (if your browser policies allow it for muted videos). If not, simply click the play button.

Run Analysis: Click the prominent "Run Violence Detection Analysis" button.

View Results: The "Analysis Results" section will dynamically update with the predicted activity (Normal, Violence, or Weaponized) and its corresponding confidence level. A clear alert message will also appear based on the prediction's severity.

👋 Contribution
Contributions are highly welcomed! Feel free to fork this repository and contribute to its ongoing development. If you encounter any bugs, have suggestions for new features, or wish to improve existing functionalities, please don't hesitate to open an issue or submit a pull request.

📄 License
This project is licensed under the MIT License. See the LICENSE file in the repository for full details.

🙏 Acknowledgements
We extend our sincere gratitude to the following resources and communities:

Google Colab: For generously providing essential GPU computing resources for efficient model training.

Kaggle: For hosting and facilitating access to the Smart-City CCTV Violence Detection Dataset.

FFmpeg: An indispensable open-source tool critical for robust video transcoding and compatibility.

Streamlit: For empowering the rapid development of such a user-friendly and visually appealing web application.

TensorFlow & Keras: For providing the foundational deep learning framework that underpins our AI model.

OpenCV: For its versatile functionalities in video processing and frame manipulation.

📧 Contact
For any questions, collaboration opportunities, or inquiries, please feel free to reach out:

GitHub: https://github.com/Krishna-pathak1535

LinkedIn: https://www.linkedin.com/in/krishnanand-pathak/

Email: krishna.pathak2003@gmail.com

<!-- end list -->


---
