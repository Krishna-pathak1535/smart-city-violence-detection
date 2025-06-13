````markdown
🚨 Smart-City CCTV Violence Detection System

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

This project delivers an **AI-driven solution for Smart-City CCTV Violence Detection**, aimed at significantly enhancing public safety. Its core function is to automatically identify and classify critical events such as "Violence" and "Weaponized" situations within surveillance video streams, distinguishing them from "Normal" activities. The system is engineered to provide **proactive alerts** and offer vital assistance to monitoring personnel in bustling urban environments, thereby contributing to safer urban spaces.

---

## 🚀 Proposed System Architecture

The system operates as a streamlined, end-to-end video analysis pipeline:

1.  **Video Ingestion Module:**
    Facilitates the seamless upload of various video formats (e.g., AVI, MP4) through an intuitive web-based interface.

2.  **AI Core (CNN-LSTM Model):**
    At its heart, a sophisticated Convolutional Neural Network (CNN) combined with a Long Short-Term Memory (LSTM) network processes incoming video frames. This core extracts spatio-temporal features to accurately classify the video segment into one of three predefined categories: "Normal," "Violence," or "Weaponized."

3.  **Real-time Prediction & Alerting System:**
    Provides instantaneous prediction results (category and confidence score) directly on the web interface, complemented by immediate visual alerts for detected threats.

4.  **Interactive Web User Interface (UI):**
    A modern and user-friendly Streamlit application serves as the primary interface. It simplifies video upload, enables integrated video playback alongside analysis, and offers clear visualization of AI-generated predictions, making the system accessible to non-technical users.

---

## 🛠️ How We Achieved It (Brief Technical Approach)

The development involved a focused approach to address the complexities of video-based AI:

* **Deep Learning Model:** A CNN-LSTM architecture was chosen to effectively capture both spatial features within frames and temporal sequences across frames, which is essential for understanding dynamic events like violence.
* **Efficient Data Handling:** Given the large size of video datasets, training was conducted in Google Colab, leveraging its GPU resources. To prevent memory exhaustion, a custom `Keras Sequence` data generator was implemented. This allowed for on-the-fly loading and preprocessing of video segments in small batches, optimizing RAM usage.
* **Robust Video Preprocessing:** To ensure universal compatibility for video playback in the web UI, `FFmpeg` was integrated. This tool transcodes uploaded videos into a standardized MP4 (H.264/AAC) format, overcoming common codec incompatibilities.
* **Interactive UI Development:** Streamlit was utilized for rapid prototyping and development of the web application, providing a clean, responsive, and aesthetically pleasing interface with minimal front-end coding.
* **Version Control & Collaboration:** Git was used for version control, with Git Large File Storage (Git LFS) specifically implemented to handle the large `.h5` model file, ensuring the repository remains lightweight while still tracking large assets. A Python virtual environment (`venv`) was maintained throughout the development process for pristine dependency management.

---

## 🎬 Demo

Witness the Smart-City CCTV Violence Detection System in action by running the `app.py` script locally!

```bash
streamlit run app.py
````

**Showcase your app's live capabilities here with compelling visuals:**

  * **Animated GIF/Short Video (Highly Recommended\!):** A concise GIF or a brief video demonstrating the entire workflow (upload, playback, prediction) is paramount for immediate impact.

    \<p align="center"\>
    \<img src="assets/images/app\_demo.gif" alt="Smart-City Violence Detection App Demo"\>
    \</p\>

  * **Key Screenshots:**

      * **Initial UI:**

        \<p align="center"\>
        \<img src="assets/images/initial\_ui\_screenshot.png" alt="Initial App UI Screenshot"\>
        \<br\>\<em\>The clean, inviting interface ready for video upload.\</em\>
        \</p\>

      * **Video Playback & Awaiting Analysis:**

        \<p align="center"\>
        \<img src="assets/images/video\_playback\_after\_upload.png" alt="Video Playback Screenshot"\>
        \<br\>\<em\>Video playing seamlessly after upload.\</em\>
        \</p\>

      * **Prediction Result (e.g., Normal):**

        \<p align="center"\>
        \<img src="assets/images/prediction\_normal\_result.png" alt="Prediction Result Normal Screenshot"\>
        \<br\>\<em\>Example of a 'Normal' activity prediction with high confidence.\</em\>
        \</p\>

      * **Prediction Result (e.g., Violence/Weaponized Alert):**

        \<p align="center"\>
        \<img src="assets/images/prediction\_violence\_alert.png" alt="Prediction Result Alert Screenshot"\>
        \<br\>\<em\>Critical alert for detected violence activity.\</em\>
        \</p\>
        \<p align="center"\>
        \<img src="assets/images/prediction\_weaponized\_alert.png" alt="Prediction Result Weaponized Alert Screenshot"\>
        \<br\>\<em\>Alternative alert for weaponized activity detection.\</em\>
        \</p\>

-----

## ⚙️ Technical Architecture

  * **Frontend (Web UI):** \<b style="color:\#4fc3f7;"\>Streamlit\</b\>
  * **Deep Learning Framework:** \<b style="color:\#00e676;"\>TensorFlow\</b\> / \<b style="color:\#00e676;"\>Keras\</b\>
  * **Video Processing:** \<b style="color:\#ff6f61;"\>OpenCV (`cv2`)\</b\>
  * **Data Serialization:** \<b style="color:\#17a2b8;"\>NumPy\</b\>
  * **Video Transcoding:** \<b style="color:\#007bff;"\>FFmpeg\</b\>
  * **Dependency Management:** \<b style="color:\#e0e0e0;"\>Python `venv`\</b\>
  * **Version Control for Large Files:** \<b style="color:\#a0a0a0;"\>Git Large File Storage (Git LFS)\</b\>

-----

## 📦 Dataset

This project is robustly built upon the **Smart-City CCTV Violence Detection Dataset (SCVD)**.

  * **Dataset Source:** [https://www.kaggle.com/datasets/toluwaniaremu/smartcity-cctv-violence-detection-dataset-scvd](https://www.kaggle.com/datasets/toluwaniaremu/smartcity-cctv-violence-detection-dataset-scvd)

  * **Description:** A comprehensive collection of video clips meticulously categorized for violence detection, providing a solid foundation for both model training and thorough evaluation. The dataset includes both original and second-split (shorter segments) versions, offering flexibility in data processing.

-----

## 💻 Local Setup Guide

Follow these steps precisely to set up and run the Streamlit web application on your local machine.

### **1. Prerequisites**

Ensure you have these installed on your system:

  * **Python 3.8+:** Download the installer from [python.org](https://www.python.org/).

  * **Git:** Download from [git-scm.com](https://git-scm.com/).

  * **FFmpeg:** Essential for video format compatibility.

      * Open PowerShell and install via `winget`:

        ```powershell
        winget install "FFmpeg (Essentials Build)"
        ```

### **2. Clone the Repository**

First, ensure Git LFS is installed globally, then clone the project.

```powershell
# Step 2.1: Install Git LFS system-wide (if not already done)
# It's recommended to run PowerShell as Administrator for this command
git lfs install

# Step 2.2: Navigate to your desired parent directory
# For example, to clone onto your Desktop:
cd C:\Users\YourUsername\Desktop\ # Replace YourUsername with your actual Windows username

# Step 2.3: Clone the repository
git clone [https://github.com/Krishna-pathak1535/smart-city-violence-detection.git](https://github.com/Krishna-pathak1535/smart-city-violence-detection.git)

# Step 2.4: Navigate into the cloned project directory
cd "smart-city-violence-detection"
```

### **3. Create and Activate a Virtual Environment**

Using a virtual environment is crucial for managing project dependencies without conflicts.

```powershell
# Create the virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate
```

*(Your PowerShell prompt should change to `(venv) PS ...>` indicating the virtual environment is active.)*

### **4. Install Project Dependencies**

Install all required Python packages within your activated virtual environment.

```powershell
pip install tensorflow opencv-python numpy scikit-learn streamlit tqdm
```

### **5. Prepare Sample Videos for Testing**

The dataset videos are originally in `.avi` format, which may not play correctly in web browsers. You'll need to convert them to the more compatible `.mp4` format using FFmpeg.

1.  **Download Sample Videos:**
    You can download a batch of 50 random videos from each category (150 total) from your Google Colab notebook (refer to Phase 1.13 in your Colab setup if you followed our previous guide).

      * Download the `random_50_videos_per_category.zip` file.

      * Extract its contents into a subfolder within your cloned project directory, e.g., `.\sample_videos_for_testing`.

2.  **Convert `.avi` to `.mp4` using FFmpeg:**
    Navigate to the directory where your downloaded `.avi` sample videos are located (e.g., `cd ".\sample_videos_for_testing"`).
    Then, execute this PowerShell command to convert all `.avi` files in that folder and its subdirectories to `.mp4`:

    ```powershell
    Get-ChildItem -Path. -Recurse -Include *.avi | ForEach-Object {
        $inputPath = $_.FullName
        $outputPath = Join-Path $_.Directory.FullName ($_.BaseName + "-converted.mp4")
        Write-Host "Converting $($_.Name)..."
        ffmpeg -i "$inputPath" -c:v libx264 -preset medium -crf 23 -c: a aac -b :a 128k -vf format=yuv420p "$outputPath" -y
        Write-Host "Converted to $($outputPath)"
    }
    Write-Host "All conversions complete!"
    ```

    *This will create `-converted.mp4` versions of your videos alongside the originals, maintaining the folder structure.*

3.  **Clean Up Original `.avi` Files (Optional):**
    Once all conversions are verified, you can delete the original `.avi` files to free up disk space:

    ```powershell
    Get-ChildItem -Path. -Recurse -Include *.avi | Remove-Item -Force
    ```

### **6. Run the Streamlit Application**

Ensure your virtual environment is active, then launch the Streamlit app.

```powershell
# If you changed the directory for video conversion, navigate back to the root of your project
# e.g., cd C:\Users\Krish\OneDrive\Desktop\smart-city-violence-detection

# Ensure the virtual environment is active
.\venv\Scripts\activate

# Run the Streamlit application
streamlit run app.py
```

This command will start a local server, and your web browser should automatically open a new tab at `http://localhost:8501`, displaying the Smart-City CCTV Violence Detection System UI.

## 💡 Usage

1.  **Upload Video:** On the web UI, use the "Select a video file to analyze" button or simply drag and drop an `.mp4` video file (preferably one you converted from the dataset for testing).

2.  **Video Playback:** The uploaded video will appear in the "Uploaded Video Stream" section and should start playing automatically (if your browser policies allow it for muted videos). If not, simply click the play button.

3.  **Run Analysis:** Click the prominent "Run Violence Detection Analysis" button.

4.  **View Results:** The "Analysis Results" section will dynamically update with the predicted activity (Normal, Violence, or Weaponized) and its corresponding confidence level. A clear alert message will also appear based on the prediction's severity.

-----

## 👋 Contribution

Contributions are highly welcomed\! Feel free to fork this repository and contribute to its ongoing development. If you encounter any bugs, have suggestions for new features, or wish to improve existing functionalities, please don't hesitate to open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Krishna-pathak1535/smart-city-violence-detection/blob/main/LICENSE) file in the repository for full details.


## 📧 Contact

For any questions, collaboration opportunities, or inquiries, please feel free to reach out:

  * **GitHub:** [https://github.com/Krishna-pathak1535](https://github.com/Krishna-pathak1535)

  * **LinkedIn:** [https://www.linkedin.com/in/krishnanand-pathak/](https://www.linkedin.com/in/krishnanand-pathak/)

  * **Email:** krishna.pathak2003@gmail.com

<!-- end list -->

```
```
