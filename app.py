import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
import os
import tempfile
import time # For simulating processing time

# --- Configuration (MUST match your Colab training setup) ---
IMG_HEIGHT, IMG_WIDTH = 128, 128
SEQUENCE_LENGTH = 10
CLASSES = ['Normal', 'Violence', 'Weaponized']
MODEL_PATH = 'best_violence_detection_model.h5' # Ensure this is in the same directory as app.py

# --- Set Streamlit Page Configuration for a modern look ---
st.set_page_config(
    page_title="Smart-City CCTV Violence Detection",
    page_icon="🚨",
    layout="wide", # Use wide layout for more space
    initial_sidebar_state="collapsed" # Collapse sidebar by default
)

# --- Custom CSS for Super Modern, Colorful UI elements ---
st.markdown("""
<style>
/* Font Import (Optional: requires internet connection) */
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&family=Orbitron:wght@400;700&display=swap');

/* Global Page Styling */
.main {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); /* Deep space blue gradient */
    color: #e0e0e0; /* Light grey text */
    font-family: 'Roboto', sans-serif;
    padding: 2.5rem;
    min-height: 100vh; /* Ensure full height background */
}
.stApp {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    min-height: 100vh;
}

/* Titles and Headers */
h1 {
    color: #00e676; /* Bright green accent */
    text-align: center;
    font-family: 'Orbitron', sans-serif; /* Futuristic font */
    font-size: 3.5em;
    text-shadow: 0 0 15px rgba(0,230,118,0.7), 0 0 25px rgba(0,230,118,0.5); /* Glowing effect */
    margin-bottom: 0.8em;
    padding-bottom: 0.2em;
    border-bottom: 2px solid rgba(0,230,118,0.3);
    animation: fadeIn 1s ease-out;
}
.stMarkdown p {
    font-size: 1.15em;
    line-height: 1.7;
    text-align: center;
    color: #a0a0a0;
    margin-bottom: 2em;
}
h2 {
    color: #4fc3f7; /* Light blue accent */
    font-size: 2.2em;
    border-bottom: 2px solid rgba(79,195,247,0.3);
    padding-bottom: 0.4em;
    margin-top: 2em;
    text-shadow: 0 0 8px rgba(79,195,247,0.5);
    font-family: 'Orbitron', sans-serif;
}
h3 {
    color: #e0e0e0;
    font-size: 1.5em;
    margin-bottom: 1em;
}

/* Card/Box Styling (main containers) */
.stContainer {
    background-color: rgba(255, 255, 255, 0.05); /* Slightly transparent white */
    backdrop-filter: blur(10px); /* Frosted glass effect */
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5), 0 0 20px rgba(0,230,118,0.2); /* Deeper, glowing shadow */
    margin-bottom: 40px;
    padding: 30px 40px;
    animation: slideInUp 0.8s ease-out;
}
.stText {
    color: #e0e0e0;
}

/* File Uploader */
.stFileUploader label {
    font-size: 1.3em;
    font-weight: bold;
    color: #4fc3f7; /* Light blue */
    text-shadow: 0 0 5px rgba(79,195,247,0.3);
}
.stFileUploader > div > button {
    background-color: #007bff; /* Blue button */
    color: white;
    border-radius: 12px;
    padding: 12px 25px;
    border: none;
    box-shadow: 0 5px 15px rgba(0,123,255,0.4);
    transition: background-color 0.3s ease, transform 0.2s ease;
    font-size: 1.1em;
    font-weight: bold;
}
.stFileUploader > div > button:hover {
    background-color: #0056b3;
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0,123,255,0.6);
}

/* Buttons */
.stButton>button {
    background-color: #00e676; /* Bright green */
    color: #1a1a2e; /* Dark text on green */
    padding: 15px 30px;
    font-size: 1.3em;
    font-weight: bold;
    margin: 20px 0;
    cursor: pointer;
    border-radius: 15px;
    border: none;
    box-shadow: 0 8px 20px rgba(0,230,118,0.4), 0 0 10px rgba(0,230,118,0.5);
    transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
    letter-spacing: 1px;
}
.stButton>button:hover {
    background-color: #00c853; /* Darker green on hover */
    transform: translateY(-4px);
    box-shadow: 0 12px 25px rgba(0,230,118,0.6), 0 0 15px rgba(0,230,118,0.7);
}

/* Progress Bar */
.stProgress > div > div > div > div {
    background-color: #ff6f61; /* Vibrant orange/red */
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(255,111,97,0.5);
}

/* Metric Boxes for Results */
.result-box {
    background-color: rgba(255, 255, 255, 0.08); /* Slightly more transparent for results */
    backdrop-filter: blur(8px);
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.4), 0 0 15px rgba(79,195,247,0.3);
    margin-top: 30px;
    text-align: center;
    border: 1px solid rgba(79,195,247,0.2);
    animation: scaleIn 0.5s ease-out;
}
.predicted-label {
    font-family: 'Orbitron', sans-serif;
    font-size: 3.5em;
    font-weight: bold;
    color: #4fc3f7; /* Light blue for label */
    margin-bottom: 0.2em;
    text-transform: uppercase;
    text-shadow: 0 0 10px rgba(79,195,247,0.7);
    animation: pulse 1.5s infinite alternate;
}
.confidence-score {
    font-family: 'Orbitron', sans-serif;
    font-size: 2.5em;
    font-weight: bold;
    color: #00e676; /* Bright green for confidence */
    text-shadow: 0 0 8px rgba(0,230,118,0.5);
}
.confidence-text {
    font-size: 1.2em;
    color: #a0a0a0;
    margin-top: 10px;
}

/* Alerts */
.stAlert {
    border-radius: 10px;
    padding: 1.5rem;
    font-size: 1.2em;
    font-weight: bold;
    box-shadow: 0 0 15px rgba(255,255,255,0.1);
    margin-top: 25px;
    animation: fadeIn 0.5s ease-out;
}
.stAlert.success { background-color: rgba(0,230,118,0.15); color: #00e676; border: 1px solid rgba(0,230,118,0.5); }
.stAlert.info { background-color: rgba(79,195,247,0.15); color: #4fc3f7; border: 1px solid rgba(79,195,247,0.5); }
.stAlert.warning { background-color: rgba(255,111,97,0.15); color: #ff6f61; border: 1px solid rgba(255,111,97,0.5); }
.stAlert.error { background-color: rgba(255,0,0,0.15); color: #ff3333; border: 1px solid rgba(255,0,0,0.5); }

/* Footer */
.footer {
    font-size: 0.95em;
    color: #a0a0a0;
    text-align: center;
    margin-top: 80px;
    padding-top: 30px;
    border-top: 1px solid rgba(255,255,255,0.1);
    animation: fadeIn 1.5s ease-out;
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
@keyframes slideInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes pulse {
    0% { text-shadow: 0 0 10px rgba(79,195,247,0.7); }
    100% { text-shadow: 0 0 20px rgba(79,195,247,1), 0 0 30px rgba(79,195,247,0.8); }
}
@keyframes scaleIn {
    from { transform: scale(0.9); opacity: 0; }
    to { transform: scale(1); opacity: 1; }
}
</style>
""", unsafe_allow_html=True)


# --- Load the Trained Model (cached for efficiency) ---
@st.cache_resource # Caches the model so it's loaded only once
def load_model():
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.warning("Please ensure 'best_violence_detection_model.h5' is in the same directory as 'app.py'.")
        return None

model = load_model()

# --- Function to preprocess a single video for inference ---
def preprocess_video_for_inference(video_path, sequence_length, img_size):
    frames = []
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        st.error(f"Error: Could not open video {video_path}")
        return None

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if total_frames == 0:
        cap.release()
        return None

    indices = np.linspace(0, total_frames - 1, sequence_length, dtype=int)

    current_frame_idx = 0
    selected_frame_count = 0

    progress_text = "Processing video frames..."
    frame_progress_bar = st.progress(0, text=progress_text)

    while cap.isOpened() and selected_frame_count < sequence_length:
        ret, frame = cap.read()
        if not ret:
            break

        if current_frame_idx in indices:
            resized_frame = cv2.resize(frame, img_size)
            normalized_frame = resized_frame / 255.0
            frames.append(normalized_frame)
            selected_frame_count += 1
            frame_progress_bar.progress(selected_frame_count / sequence_length, text=progress_text)
        current_frame_idx += 1

    cap.release()
    frame_progress_bar.empty() # Clear the progress bar after completion

    if len(frames) < sequence_length:
        st.warning(f"Video has fewer than {sequence_length} frames. Attempting to pad with zeros.")
        while len(frames) < sequence_length:
            frames.append(np.zeros((img_size[0], img_size[1], 3), dtype=np.float32))

    if not frames or any(f.shape != (img_size[0], img_size[1], 3) for f in frames):
        st.error("Could not extract valid frames from video.")
        return None

    return np.expand_dims(np.array(frames, dtype=np.float32), axis=0)


# --- Main Inference Function ---
def detect_violence_in_video(video_path):
    if model is None:
        return "Model Not Loaded", 0.0

    preprocessed_video = preprocess_video_for_inference(video_path, SEQUENCE_LENGTH, (IMG_HEIGHT, IMG_WIDTH))

    if preprocessed_video is None or preprocessed_video.shape[1] != SEQUENCE_LENGTH:
        return "Video Processing Failed", 0.0

    prediction = model.predict(preprocessed_video, verbose=0)[0]
    predicted_class_index = np.argmax(prediction)
    predicted_class_label = CLASSES[predicted_class_index]
    confidence = prediction[predicted_class_index]

    return predicted_class_label, confidence

# --- Streamlit UI ---
st.title("🚨 Smart-City CCTV Violence Detection System")
st.markdown("<p style='text-align: center; font-size: 1.2em; color: #a0a0a0;'>Leveraging AI for enhanced public safety and proactive threat detection.</p>", unsafe_allow_html=True)
st.markdown("---")

# Main content area
st.markdown('<div class="stContainer">', unsafe_allow_html=True) # Start custom container for upload
st.subheader("Upload & Preview Video")
uploaded_file = st.file_uploader("Select a video file to analyze", type=["avi", "mp4"], accept_multiple_files=False)
st.markdown('</div>', unsafe_allow_html=True) # End custom container for upload


# Placeholders for dynamic content
video_col, results_col = st.columns(2)

# Video display section
with video_col:
    st.markdown('<div class="stContainer">', unsafe_allow_html=True) # Start custom container for video
    st.subheader("Uploaded Video Stream")
    uploaded_video_placeholder = st.empty() # Placeholder for video display
    detection_button_placeholder = st.empty() # Placeholder for button
    st.markdown('</div>', unsafe_allow_html=True) # End custom container for video

# Results display section
with results_col:
    st.markdown('<div class="stContainer">', unsafe_allow_html=True) # Start custom container for results
    st.subheader("Analysis Results")
    results_placeholder = st.empty() # Placeholder for prediction results
    alert_placeholder = st.empty() # Placeholder for alerts
    st.markdown('</div>', unsafe_allow_html=True) # End custom container for results


# ... (rest of your app.py code) ...

# Logic after file upload
if uploaded_file is not None:
    # Create a temporary file to save the uploaded video
    with tempfile.NamedTemporaryFile(delete=False, suffix=".avi") as tmp_file:
        tmp_file.write(uploaded_file.read())
        video_path = tmp_file.name

    # --- ADDED: Small delay to ensure file is written ---
    time.sleep(0.5) # Give the file system a moment to write the video

    st.success(f"Video uploaded successfully: {uploaded_file.name}", icon="✅")

    with uploaded_video_placeholder.container():
        st.info("Video uploaded. It should start playing automatically. If not, please click the play button manually. Then click 'Run Analysis'.", icon="ℹ️")

        # Display the uploaded video prominently and ensure it plays
        # Removed 'format="video/avi"' as it might cause issues if the internal codec is different
        # ADDED: muted=True for better autoplay chances
        st.video(video_path, start_time=0, loop=True, autoplay=True, muted=True) # Removed use_container_width as per your last fix

        st.caption("The uploaded video is playing above. Click 'Run Analysis' to get predictions.")


    with detection_button_placeholder:
        # Use a key to prevent re-triggering button on minor state changes
        if st.button("Run Violence Detection Analysis", key="run_detection_button", use_container_width=True):
            if model is not None:
                with st.spinner("Analyzing video frames... This might take a moment based on video length and model complexity."):
                    # Simulate processing time slightly if needed for better UX, remove for real performance
                    # time.sleep(2)
                    predicted_label, confidence = detect_violence_in_video(video_path)

                with results_placeholder.container():
                    st.markdown(
                        f"""
                        <div class="result-box">
                            <div class="predicted-label">{predicted_label}</div>
                            <div class="confidence-score">{confidence*100:.2f}%</div>
                            <div class="confidence-text">Confidence Level</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with alert_placeholder:
                    if predicted_label == "Violence" or predicted_label == "Weaponized":
                        st.error("🚨 **CRITICAL ALERT: Potential Threat Detected! Immediate action required.**", icon="🚨")
                    else:
                        st.info("✅ **STATUS: All Clear. No anomalous activity detected.**", icon="👍")
            else:
                st.error("Model not loaded. Cannot perform analysis.", icon="❌")

    # Clean up the temporary file when the script re-runs (due to interaction or new upload)
    try:
        if os.path.exists(video_path):
            os.unlink(video_path)
            # st.text(f"Temporary file {video_path} deleted.") # Uncomment for debugging
    except Exception as e:
        st.warning(f"Could not delete temporary file {video_path}: {e}")

else:
    # Clear content in placeholders when no file is uploaded or during initial load
    with uploaded_video_placeholder:
        st.info("Upload a video file to get started.", icon="⬆️")
    detection_button_placeholder.empty()
    results_placeholder.empty()
    alert_placeholder.empty()

st.markdown("---")
st.markdown("""
<div class="footer">
    <p>A proactive security solution for smart urban environments. Designed in Hyderabad, Telangana.</p>
    <p>© 2025 Smart-City Surveillance. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)