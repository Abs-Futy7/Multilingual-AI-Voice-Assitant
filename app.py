import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .stButton>button {
            width: 100%;
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 10px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stTextArea textarea {
            font-size: 16px;
            border-radius: 10px;
            padding: 10px;
        }
        .stAudio {
            margin-top: 20px;
        }
        .stDownloadButton>button {
            background-color: #008CBA;
            color: white;
            padding: 10px;
            border-radius: 10px;
            border: none;
        }
        .stDownloadButton>button:hover {
            background-color: #007bb5;
        }
    </style>
""", unsafe_allow_html=True)

def main():
    st.title("🎙️ Multilingual AI Assistant")

    if st.button("Ask a Question"):
        with st.spinner("⏳ Generating response..."):
            text = voice_input()
            response = llm_model_object(text)
            text_to_speech(response)

            audio_file = open("audio.mp3", "rb")
            audio_bytes = audio_file.read()

            st.text_area("📝 Response:", value=response, height=200)
            st.audio(audio_bytes, format="audio/mp3")

            st.download_button(label="⬇️ Download Audio",
                               data=audio_bytes, 
                               file_name="audio.mp3", 
                               mime="audio/mp3")

if __name__ == "__main__":
    main()
