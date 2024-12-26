# BrandForge🛠️🚀
![WhatsApp Image 2024-12-26 at 09 44 32_86503e93](https://github.com/user-attachments/assets/74f8dc52-efe3-474d-8fe0-8c90686b2ffd)

**BrandForge** is an AI-powered personal branding and career coaching platform designed to help developers and students stand out in their professional communities and networks. This application provides actionable insights, strategies, and a roadmap to empower users to achieve their personal branding and career goals.

## Features

- **Customized Personal Branding Strategies**: Enhance LinkedIn, GitHub, and personal portfolios with tailored advice.
- **Content Creation Guidance**: Generate content calendars, impactful posts, and tips for engaging with the community.
- **Career Growth Tips**: Optimize resumes, prepare for interviews, and learn effective communication techniques.
- **Project and Certification Suggestions**: Get recommendations based on industry trends and personal goals.
- **Roadmap Building**: Create a step-by-step plan to achieve milestones in branding and career development.

![WhatsApp Image 2024-12-26 at 09 44 41_f843e3b8](https://github.com/user-attachments/assets/b609e005-24c5-4e13-aeb7-6118fe2c17fa)
![WhatsApp Image 2024-12-26 at 09 45 18_50af64dd](https://github.com/user-attachments/assets/54d54a2e-a67b-47ed-bf9d-35f89bc0a82d)
## Getting Started

### Prerequisites
- Python 3.7 or higher
- Git

### Installation Steps

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/brandforge.git
cd brandforge
```

2. **Set Up Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Application**
```bash
streamlit run app.py
```

5. **Access the App**
Open your browser and navigate to: `http://localhost:8501`

## Project Structure
```
brandforge/
│
├── venv/                # Virtual environment directory
├── app.py              # Main Streamlit application
├── agent_config.json   # Agent configuration file
├── requirements.txt    # Dependency file
└── README.md          # Project documentation
```

## Usage

1. Launch the application using Streamlit.
2. Enter your questions about personal branding or career growth in the input box.
3. Receive actionable suggestions powered by AI.

### Examples

- **Question**: "How can I make my LinkedIn profile stand out as a front-end developer?"
  **Response**: "Update your headline with keywords like 'React Developer | Building Seamless UI/UX.' Showcase your top projects in the Featured section..."

- **Question**: "I'm a student with no experience; how do I brand myself?"
  **Response**: "Focus on your potential and learning journey. Highlight coursework, certifications, or small personal projects..."

## API Configuration

The app connects to the Lyzr agent using the following details:
- **API URL**: `https://agent-prod.studio.lyzr.ai/v3/inference/`
- **API Key**: *Configured securely in the app.*

## Contributing

We welcome contributions to enhance BrandForge! To contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Add feature-name"`
4. Push to the branch: `git push origin feature-name`
5. Create a pull request.

## License

This project is licensed under the MIT License.

## Contact

For queries or feedback, feel free to reach out:
**Email**: sarankumar131313@gmail.com
