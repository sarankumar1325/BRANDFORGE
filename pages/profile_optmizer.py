import streamlit as st
from utils.linkedin_helper import LinkedinHelper
from utils.github_helper import GithubHelper

st.set_page_config(page_title="Profile Optimizer", page_icon="📊")

def main():
    st.title("Profile Optimizer 📊")
    
    tab1, tab2 = st.tabs(["LinkedIn Optimization", "GitHub Optimization"])
    
    with tab1:
        st.header("LinkedIn Profile Analysis")
        
        profile_text = st.text_area("Paste your LinkedIn profile content here", height=200)
        col1, col2 = st.columns(2)
        
        with col1:
            experience = st.text_input("Your experience areas")
        with col2:
            skills = st.text_input("Your key skills")
        
        if st.button("Analyze LinkedIn Profile"):
            with st.spinner("Analyzing your profile..."):
                linkedin_helper = LinkedinHelper()
                analysis = linkedin_helper.analyze_profile(profile_text)
                headline = linkedin_helper.generate_headline(experience, skills)
                
                st.success("Analysis Complete!")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Suggested Headline")
                    st.info(headline.get('response', 'No headline generated.'))
                with col2:
                    st.subheader("Profile Improvements")
                    st.write(analysis.get('response', 'No improvements suggested.'))
    
    with tab2:
        st.header("GitHub Profile Analysis")
        
        github_username = st.text_input("Enter your GitHub username")
        experience_level = st.select_slider(
            "Experience Level",
            options=["Beginner", "Intermediate", "Advanced"]
        )
        
        if st.button("Analyze GitHub Profile"):
            with st.spinner("Analyzing your GitHub profile..."):
                github_helper = GithubHelper()
                analysis = github_helper.analyze_profile(github_username)
                project_suggestions = github_helper.suggest_projects("your skills", experience_level)
                
                st.success("Analysis Complete!")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Profile Analysis")
                    st.write(analysis.get('response', 'No analysis available.'))
                with col2:
                    st.subheader("Suggested Projects")
                    st.write(project_suggestions.get('response', 'No projects suggested.'))

if __name__ == "__main__":
    main()
