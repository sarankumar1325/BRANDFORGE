import streamlit as st
import json

# Page configuration
st.set_page_config(
    page_title="BrandForge",
    page_icon="🚀",
    layout="wide"
)

def load_agent_config():
    with open('data/agent.json', 'r') as file:
        return json.load(file)

def create_card(title, text, page_name):
    """Helper function to create a card-like UI."""
    st.markdown(
        f"""
        <div style="
            background-color: #f9f9f9;
            padding: 20px;
            margin: 10px;
            border-radius: 10px;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
            text-align: center;">
            <h3 style="color: #333;">{title}</h3>
            <p style="color: #666;">{text}</p>
            <a href='/pages/{page_name}' style="
                display: inline-block;
                padding: 10px 20px;
                background-color: #007bff;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;">
                Explore
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

def main():
    # Load agent configuration
    agent_config = load_agent_config()
    
    # Sidebar
    st.sidebar.title("BrandForge")
    st.sidebar.info(agent_config['description'])
    
    # Main content
    st.title("Welcome to BrandForge 🚀")
    st.subheader("Your Personal Branding & Career Coach")
    
    # Quick Actions
    col1, col2, col3 = st.columns(3)
    
    with col1:
        create_card("Profile Optimizer", "Enhance your LinkedIn and GitHub profiles", "profile_optimizer.py")
    
    with col2:
        create_card("Content Calendar", "Plan and create engaging content", "content_calendar.py")
    
    with col3:
        create_card("Career Roadmap", "Build your personalized career path", "career_roadmap.py")
    
    # Quick Start Guide
    with st.expander("📚 Quick Start Guide"):
        st.markdown("""
        1. **Profile Optimization**: Start by analyzing and improving your professional profiles.
        2. **Content Strategy**: Create a content calendar and get post ideas.
        3. **Career Planning**: Define your goals and get a customized roadmap.
        """)

if __name__ == "__main__":
    main()
