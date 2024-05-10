import streamlit as st
import subprocess
import tempfile
import os
import re
import ffmpeg

st.title("Video Trimmer")

# Initialize the variable
temp_file_name = None

# Helper Functions
def time_to_seconds(t):
    h, m, s = map(int, t.split(':'))
    return h * 3600 + m * 60 + s

def seconds_to_time(sec):
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return f"{h:02}:{m:02}:{s:02}"

# Get the video file
uploaded_file = st.file_uploader("Upload a video", type=["mp4"])

if uploaded_file is not None:
    st.header("Trim Video")
    
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        temp_file_name = temp_file.name
        temp_file.write(uploaded_file.getvalue())
    
    # Display the uploaded video
    st.video(temp_file_name)

    # Get start and end times from user
    video_info = ffmpeg.probe(temp_file_name)
    duration = int(float(video_info['format']['duration']))
    
    start_time = st.text_input("Start time (HH:MM:SS):", value="00:00:00")
    end_time = st.text_input("End time (HH:MM:SS):", value=seconds_to_time(duration))

    if st.button("Trim Video"):
        progress_bar = st.progress(0)
        output_name = tempfile.mktemp(suffix=".mp4")
        command = [
            'ffmpeg',
            '-i', temp_file_name,
            '-ss', str(time_to_seconds(start_time)),
            '-to', str(time_to_seconds(end_time)),
            '-c:v', 'copy',  # Copy the video stream
            '-c:a', 'aac',  # Convert audio to AAC
            '-strict', 'experimental',  # Sometimes needed for AAC
            output_name
        ]
        
        # Log the command for debugging
        st.write("Running command:", ' '.join(command))
        
        process = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            st.error(f"Error trimming video: {stderr}")
        else:
            progress_bar.empty()
            st.success("Video trimmed successfully!")
            st.header("Trimmed Video")
            st.video(output_name)

            # Add download button for the trimmed video
            with open(output_name, "rb") as file:
                btn = st.download_button(
                    label="Download Trimmed Video",
                    data=file,
                    file_name="trimmed_video.mp4",
                    mime="video/mp4"
                )

# Cleanup
if temp_file_name and os.path.exists(temp_file_name):
    os.remove(temp_file_name)
st.write("Application finished. Please close this window.")
