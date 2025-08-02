import streamlit as st

st.set_page_config(page_title="AI Career Counselor", page_icon="🎯")

st.title("🎯 AI Career Counselor")
st.write("Get career suggestions based on your interests!")

# User input
interest = st.text_input("What do you love doing? (e.g. designing, coding, data analysis, problem-solving, helping people)")

# Logic for suggestions
if interest:
    st.subheader("🤖 Suggested Career Path:")
    interest = interest.lower()

    if "data" in interest or "analysis" in interest:
        st.success("🔎 Data Scientist or Data Analyst")
    elif "design" in interest:
        st.success("🎨 UI/UX Designer or Frontend Developer")
    elif "code" in interest or "develop" in interest:
        st.success("👨‍💻 Software Engineer or Web Developer")
    elif "ai" in interest or "machine" in interest:
        st.success("🧠 Machine Learning Engineer or AI Researcher")
    elif "people" in interest or "help" in interest:
        st.success("🗣 Career Coach or HR Specialist")
    elif "business" in interest:
        st.success("📊 Business Analyst or Product Manager")
    else:
        st.success("🚀 Explore tech roles — maybe try freelancing or startup ideas!")

    st.caption("Note: This is a simple AI-based suggestion tool.")

st.markdown("---")
st.markdown("Made with ❤️ using [Streamlit](https://streamlit.io)")

