<div align="center">

# 🤖 AI Agent for App Review Analysis

![Banner](/banner.png)

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Pydantic](https://img.shields.io/badge/Pydantic_AI-2.0+-green.svg?style=for-the-badge&logo=pydantic&logoColor=white)](https://github.com/pydantic/pydantic-ai)
[![Marimo](https://img.shields.io/badge/Marimo-0.12.4-orange.svg?style=for-the-badge&logo=jupyter&logoColor=white)](https://marimo.io)
[![LLM](https://img.shields.io/badge/LLM-Powered-red.svg?style=for-the-badge&logo=openai&logoColor=white)](https://github.com/pydantic/pydantic-ai)

</div>

## 🌟 Overview

This project features an advanced AI agent system designed to analyze mobile app reviews and extract actionable insights. Leveraging the power of Pydantic AI and large language models, these intelligent agents process thousands of app reviews to identify patterns, common issues, feature requests, and marketing opportunities.

## ✨ Features

### 🧠 Multi-Agent Intelligence
Specialized AI agents for different analytical tasks working in harmony

### 📊 Mass Review Processing
Analyzes thousands of app reviews from SQLite database with ease

### 💡 Insight Generation
- Identifies common bugs and issues
- Extracts feature requests from users
- Highlights praised features for marketing
- Discovers key phrases for copywriting

### 🚀 Strategic Planning
- Suggests compelling app names
- Generates persuasive marketing copy
- Prioritizes features based on user feedback
- Predicts potential development issues

### 🖥️ Interactive Experience
Built with Marimo for a seamless notebook-like interface with real-time agent interactions

## 🛠️ Technology Stack

### Core Technologies
- **Python**: Foundation of the entire agent system
- **Pydantic AI**: Structured AI agent interactions with type safety
- **SQLite**: Efficient storage and querying of app reviews
- **Marimo**: Interactive notebook interface for agent visualization

### 🧠 LLM Integration
- **Google Gemini**: Advanced reasoning capabilities
- **OpenAI Models**: Powerful completion and analysis
- **Local LLMs via Ollama**: Privacy-focused options (e.g., Qwen 2.5)

## 📊 Data Processing

The system processes app reviews stored in CSV format and converts them to a SQLite database for efficient querying.

### Filtering Capabilities
- 🌟 **Rating Range**: Select reviews within specific star ratings to focus on problem areas or success stories
- 📝 **Minimum Word Count**: Filter by review length/detail to get more substantive feedback
- 🎲 **Random Sampling**: Prevent bias in selection to ensure representative insights

## 🤖 AI Agents

The project implements three specialized AI agents working together:

### 🛠️ Product Improvement Agent
Analyzes negative reviews to identify:
- Common bugs and crashes
- UI/UX pain points
- Missing features
- Performance issues

### 📣 Marketing Agent
Mines positive reviews to extract:
- Most-loved features
- Compelling user testimonials
- Persuasive language patterns
- Competitive advantages

### 🧩 Planning Agent
Synthesizes insights to generate:
- Catchy app names
- Compelling marketing copy
- Prioritized MVP feature list
- Risk assessment

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Required packages (see requirements.txt)
- API keys for LLM providers (if using cloud models)

### Installation

```bash
# 1. Clone this repository
git clone https://github.com/yourusername/ai-app-review-agents.git
cd ai-app-review-agents

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
# Create a .env file with your API keys
echo "GEMINI_API_KEY=your_gemini_api_key" > .env
```

### Running the Agents

```bash
# Launch the interactive Marimo notebook with agents
marimo edit agent2.py
```

## 📝 Usage Examples

### Example Use Cases
- **Review Analysis**: Analyze reviews for specific apps or filter by rating
- **Product Enhancement**: Generate prioritized improvement recommendations
- **Marketing Creation**: Create compelling copy based on user sentiment
- **MVP Planning**: Design new apps based on competitor reviews

```python
# Example: Running the marketing agent on filtered reviews
marketing_result = marketing_agent.run_sync(
    "Generate compelling marketing materials highlighting our app's strengths",
    deps=Dependencies(app_description="Social Media App")
)

# Access the agent's insights
for feature in marketing_result.data.praised_features:
    print(f"✅ {feature}")

for phrase in marketing_result.data.important_phrases:
    print(f"💬 {phrase}")
```

## 🔍 Future Enhancements

### 📊 Advanced Analytics
- **Sentiment Visualization**: Interactive dashboards showing sentiment trends
- **Temporal Analysis**: Track how app perception changes over time
- **Competitive Intelligence**: Compare reviews across similar apps

### 🤖 Enhanced Agent Capabilities
- **Automated Reporting**: Generate PDF/HTML reports with insights
- **Multi-language Support**: Analyze reviews in various languages
- **Voice Analysis**: Process audio feedback alongside text

### 🔄 Integration Ecosystem
- **App Store Connectors**: Direct integration with app stores
- **Slack/Teams Notifications**: Real-time alerts for critical feedback
- **Jira/GitHub Integration**: Auto-create tickets from issues

### 🧠 Advanced AI Models
- **Fine-tuned Models**: Domain-specific LLMs for app analysis
- **Multimodal Analysis**: Process screenshots alongside text
- **Predictive Analytics**: Forecast rating trends

## 🙏 Acknowledgments

- [**Pydantic AI**](https://github.com/pydantic/pydantic-ai) - Agent Framework
- [**Marimo**](https://marimo.io) - Interactive UI
- [**Gemini API**](https://github.com/google/generative-ai-python) - LLM Provider

Inspired by real-world app development challenges and the power of AI agents to transform feedback into action.

---

<div align="center">
<p>Made with ❤️ by AI enthusiasts</p>

[![GitHub stars](https://img.shields.io/github/stars/yourusername/ai-app-review-agents?style=social)](https://github.com/yourusername)
</div>
