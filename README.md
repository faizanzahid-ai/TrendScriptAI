# TrendScriptAI
TrendStory is an AI microservice that extracts trending YouTube videos, transcribes audio, summarizes content, and generates story scripts in themes like comedy or tragedy. Features include trend detection, audio extraction, transcription with Whisper, story generation with Falcon-RW-1B, async gRPC API, Gradio/Streamlit demo, and CI/CD deployment.

# Features
YouTube Video Search: Search for trending YouTube videos by keyword and region.
Transcription: Convert YouTube video audio into accurate transcripts using Whisper.
Summarization: Summarize lengthy transcripts using BART for concise, meaningful summaries.
Story Generation: Use Falcon-RW-1B to generate unique, creative stories based on the transcript and user-defined themes.
TTS Conversion: Convert the generated stories into audio using the Tortoise TTS model.

# Models Used
Whisper (large-v3): For transcription of YouTube video audio.
BART (facebook/bart-large-cnn): For summarization of transcripts.
Falcon-RW-1B: For generating stories based on transcripts and given themes.
Tortoise TTS (Gatozu35/tortoise-tts): For converting stories into audio format.

# Setup and Installation
Clone this repository:
bash
git clone https://github.com/faizanzahid-ai/TrendScriptAI.git
cd TrendScriptAI

Install the required dependencies:
bash
pip install -r requirements.txt

# Ensure you have a valid YouTube API Key and set it in the YOUTUBE_API_KEY variable.

# Download the required models by running the script:
bash
python download_models.py

# Usage
Run the pipeline:
bash
python app.py

# The script will prompt you to enter:
Keywords for searching YouTube videos.
Themes for the generated story (e.g., dramatic, funny, romantic).
Region codes (e.g., US, IN, UK).
Max YouTube results per keyword.
Number of videos to process randomly.

# The script will then:
Search YouTube for videos based on your keywords.
Download the audio of the selected videos.
Transcribe the audio into text.
Summarize the transcript.
Generate a creative story based on the transcript and your selected themes.
Convert the story into audio using TTS.
The output will be saved in the final_transcript_story.txt file and the generated audio will be saved in the generated_audios directory.

# Contributing
Feel free to contribute to this project by submitting pull requests. Suggestions and improvements are always welcome!
