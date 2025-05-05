

import streamlit as st
import grpc
from youtube_pb2 import GenerateRequest
from youtube_pb2_grpc import GenerateServiceStub

# ==== Connect to gRPC ====
@st.cache_resource
def get_grpc_stub():
    channel = grpc.insecure_channel("localhost:50051")
    return GenerateServiceStub(channel)

stub = get_grpc_stub()

# ==== Page Setup ====
st.set_page_config(page_title="🎥 YouTube Story Generator", layout="centered")
st.markdown(
    """
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .stTextInput>div>div>input {
            border-radius: 10px;
            padding: 10px;
        }
        .stTextArea textarea {
            border-radius: 10px;
            padding: 10px;
        }
        .stButton button {
            background-color: #6c63ff;
            color: white;
            font-weight: bold;
            border-radius: 12px;
            padding: 0.75em 1.5em;
            margin-top: 10px;
        }
        .stSlider>div>div {
            color: #6c63ff;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🎬 YouTube Video to AI-Generated Story")
st.markdown("Welcome to your **Multimodal Story Generator**. Enter the fields below and get your AI-crafted story! 🧠📖")

st.divider()

# ==== Inputs ====
col1, col2 = st.columns(2)
with col1:
    keywords = st.text_input("🔍 Keywords (comma-separated)", "AI, Technology")
    regions = st.text_input("🌍 Region Codes (comma-separated)", "US, IN")

with col2:
    themes = st.text_input("🎭 Themes (comma-separated)", "funny, dramatic, romantic")
    max_results = st.slider("🔢 Max YouTube Results", 1, 50, 5)
    num_random_videos = st.slider("🎲 Videos to Process", 1, 10, 2)

custom_prompt_flag = st.checkbox("🧠 Use Custom Prompt?")
custom_prompt = ""
if custom_prompt_flag:
    custom_prompt = st.text_area("✍️ Enter Custom Prompt", "Tell a thrilling story from the video content.")

st.divider()

# ==== Submit Button ====
if st.button("🚀 Generate Story"):
    try:
        request = GenerateRequest(
            keywords=[k.strip() for k in keywords.split(",")],
            regions=[r.strip().upper() for r in regions.split(",")],
            themes=[t.strip().lower() for t in themes.split(",")],
            custom_prompt=custom_prompt,
            max_results=max_results,
            num_random_videos=num_random_videos,
        )

        response = stub.Generate(request)

        st.success("🎉 Story generated successfully!")
        st.subheader("📜 Transcript")
        st.text_area("Transcript", response.transcript, height=200)

        st.subheader("📝 Summary")
        st.text_area("Summary", response.summary, height=150)

        st.subheader("📖 Story")
        st.text_area("Generated Story", response.story, height=250)

    except grpc.RpcError as e:
        st.error(f"❌ gRPC Error: {e.code().name} — {e.details()}")

    except Exception as e:
        st.error(f"🚨 Unexpected Error: {str(e)}")



