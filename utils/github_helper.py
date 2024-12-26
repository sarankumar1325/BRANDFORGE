class GithubHelper:
    def analyze_profile(self, github_username):
        if not github_username.strip():
            return {"response": "Please enter a GitHub username for analysis."}
        
        # Placeholder analysis logic
        analysis = [
            f"GitHub username '{github_username}' has a good presence.",
            "Consider contributing to popular open-source projects.",
            "Add detailed README files to showcase your projects."
        ]
        return {"response": "GitHub Analysis:\n" + "\n".join(analysis)}
    
    def suggest_projects(self, skills, experience_level):
        if not skills or not experience_level:
            return {"response": "Provide both skills and experience level to get suggestions."}
        
        # Placeholder project suggestions
        project_suggestions = [
            f"Build a portfolio website to showcase {skills}.",
            "Contribute to open-source libraries in your field of expertise.",
            "Develop a project that solves a real-world problem using your skills."
        ]
        return {"response": "Suggested Projects:\n" + "\n".join(project_suggestions)}
