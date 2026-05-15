import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI College FAQ Chatbot",
    page_icon="🎓",
)

# Main title
st.title("🎓 AI College FAQ Chatbot")

# Subtitle
st.markdown("### Welcome Student!")
st.write("Ask questions related to college facilities, exams, fees, hostel, and more.")

# Divider
st.write("---")

# User input box
user_question = st.text_input("💬 Enter your question:")

# Chatbot logic
if user_question:

    # Convert input to lowercase
    question = user_question.lower()

    # Library
    if "library" in question or "books" in question:
        st.success("📚 Library opens from 8 AM to 8 PM.")

    # Fees
    elif "fees" in question or "payment" in question:
        st.success("💰 Fees can be paid through the college portal.")

    # Exams
    elif "exam" in question or "test" in question:
        st.success("📝 Exams start from June 10.")

    # Hostel
    elif "hostel" in question or "room" in question:
        st.success("🏠 Hostel facility is available for boys and girls.")

    # Canteen
    elif "canteen" in question or "food" in question:
        st.success("🍔 Canteen opens from 9 AM to 5 PM.")

    # Holidays
    elif "holiday" in question or "vacation" in question:
        st.success("🎉 Summer holidays start from May 25.")

    # Unknown question
    else:
        st.error("❌ Sorry, I do not know the answer.")

# Footer
st.write("---")
st.caption("Developed using Python and Streamlit")