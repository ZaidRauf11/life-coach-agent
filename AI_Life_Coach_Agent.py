import streamlit as st
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.googlesearch import GoogleSearchTools
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# --- Define Agent ---
life_coach_agent = Agent(
    name = "Life Coach Agent",
    model=Groq(id="qwen/qwen3-32b"),
    role="A friendly AI life coach who cares about the user’s feelings and offers uplifting advice",
    tools=[GoogleSearchTools()],
    instructions=(
       "When the user shares their mood (e.g., tired, stressed, happy, or sad), "
       "reply with a short, warm, and practical suggestion that feels supportive. "
       "Keep your tone positive, motivational, and friendly—like a caring coach. "
       "If the mood isn’t clear, gently ask the user to describe how they feel."
    ),
    
    show_tool_calls=False,
    markdown=True,
)


# Streamlit UI
st.set_page_config(page_title="Life Coach", page_icon="🧘", layout="centered")

st.markdown("""
    <h1>AI Life Coach Agent 🧘</h1>
    <p>Try examples like: <b>"I feel tired"</b>, <b>"I am stressed"</b>, <b>"I'm really happy today"</b>, or <b>"Feeling a bit sad"</b>.</p>
""", unsafe_allow_html=True)


# Input form
with st.form(key="query_form"):
    query = st.text_input("💭 How are you feeling today?", placeholder="e.g. I feel tired, I am stressed, I'm happy, Feeling sad")
    submit = st.form_submit_button("Get Suggestion")

# Main Processing
if submit and query:
    with st.spinner("⏳ Fetching results…"):
        try:
            response = life_coach_agent.run(query)
            result_text = response.content if hasattr(response, "content") else str(response)

            if result_text:
                st.markdown("### 📄 Results")
                st.markdown(result_text)
            else:
                st.warning("⚠ No results found for your query.")

        except Exception as e:
            st.error(f"⚠ Something went wrong: {e}")
            st.info("Check your GROQ_API_KEY or internet connection.")




