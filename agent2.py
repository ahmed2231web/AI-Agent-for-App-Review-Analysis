import marimo

__generated_with = "0.12.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    mo.md('# Agents to Analyze Mobile App Reviews in Python')
    return (mo,)


@app.cell
def _():
    import os
    from dotenv import load_dotenv


    # Load environment variables from .env file
    load_dotenv()
    gemini_api_key = os.getenv('GEMINI_API_KEY')
    return gemini_api_key, load_dotenv, os


@app.cell
def _():
    # 'All Packages Imports'

    import sqlite3
    import textwrap
    from dataclasses import dataclass
    from pathlib import Path
    from typing import List

    import nest_asyncio

    from pydantic import BaseModel, Field
    from pydantic_ai import Agent, RunContext
    from pydantic_ai.models.openai import OpenAIModel
    from pydantic_ai.providers.openai import OpenAIProvider

    db_file_path = "database.db"

    ollama_model = OpenAIModel(
        model_name='qwen2.5:3b', provider=OpenAIProvider(base_url='http://localhost:11434/v1')
    )

    nest_asyncio.apply()
    return (
        Agent,
        BaseModel,
        Field,
        List,
        OpenAIModel,
        OpenAIProvider,
        Path,
        RunContext,
        dataclass,
        db_file_path,
        nest_asyncio,
        ollama_model,
        sqlite3,
        textwrap,
    )


@app.cell
def _(dataclass):
    # 'Get Reviews'

    @dataclass
    class Review:
        app: str
        content: str
        score: int


    # without @dataclass it have to write like this

    # class Review:
    #     def __init__(self, app: str, content: str, score: int):
    #         self.app = app
    #         self.content = content
    #         self.score = score

    #     def __repr__(self):
    #         return f"Review(app={self.app!r}, content={self.content!r}, score={self.score})
    return (Review,)


@app.cell
def _(List, Review, sqlite3):
    # 'Tools'

    def fetch_reviews(
        min_rating: int,
        max_rating: int,
        max_reviews: int = 30000,
        min_words_in_review: int = 10,
    ) -> List[Review]:
        """
        Get reviews within a specified rating range.

        Args:
            min_rating (int): The lower bound of the rating (inclusive). Between 1 and 5.
            max_rating (int): The upper bound of the rating (inclusive). Between 1 and 5.
            max_reviews (int): The maximum number of reviews to return.
            min_words_in_review (int): The minimum number of words required in a review.
    
        Returns:
            List[Review]: A list of reviews meeting the criteria.
        """

        db_file_path = "database.db"  # Ensure the correct path is set

        with sqlite3.connect(db_file_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT app, content, score FROM dataset
                WHERE score >= ? AND score <= ? 
                AND content IS NOT NULL
                ORDER BY RANDOM()
                """,
                (min_rating, max_rating),
            )

            reviews = []

            for app, content, score in cursor.fetchall():
                word_count = len(content.split())
                if word_count < min_words_in_review:
                    continue
                reviews.append(Review(app=app, content=content, score=score))

        return reviews[:max_reviews]  # Limit the number of returned reviews
    return (fetch_reviews,)


@app.cell
def _(fetch_reviews):
    # Reviews

    reviews = fetch_reviews(2, 4, max_reviews=10000)

    # Print total number of reviews
    print(f"Total number of reviews fetched: {len(reviews)}")
    

    # reviews[0]
    return (reviews,)


@app.cell
def _(dataclass):
    # Dependencies

    @dataclass
    class Dependencies:
        app_description: str
    return (Dependencies,)


@app.cell
def _(Agent, BaseModel, Dependencies, Field, List, fetch_reviews):
    # Agents

    PRODUCT_IMPROVEMENT_PROMPT = """
    As a specialized assistant for app developers and product managers, your task is to analyze user feedback and identify actionable areas for improvement in their applications. Please consider the following aspects while providing your insights:

    Categorization: Break down the feedback into categories such as usability, performance, features, and customer support to provide a structured analysis.

    Prioritization: Assess the impact and frequency of the feedback to prioritize the areas that require immediate attention versus those that can be addressed in future updates.

    Recommendations: For each identified area of improvement, suggest specific strategies or features that could enhance user experience and satisfaction.

    Trends: Highlight any emerging trends or recurring themes in the feedback that could inform long-term development strategies.

    User Personas: Consider different user personas when analyzing feedback to ensure that recommendations cater to the diverse needs of the app's user base.

    Please provide a comprehensive report based on the user feedback data provided, including examples where applicable to support your recommendations.
    """.strip()

    class ProductImprovementResult(BaseModel):
        issues: List[str] = Field(
            description="Prioritized list of common bugs or issues (e.g., 'app crashes on startup')"
        )
        feature_requests: List[str] = Field(
            description="Suggest top requested features (e.g., 'add dark mode')"
        )

    improvement_agent = Agent(
        'google-gla:gemini-2.0-flash',
        # ollama_model,
        deps_type=Dependencies,
        result_type=ProductImprovementResult,
        system_prompt=PRODUCT_IMPROVEMENT_PROMPT,
        tools=[fetch_reviews],
    )
    return (
        PRODUCT_IMPROVEMENT_PROMPT,
        ProductImprovementResult,
        improvement_agent,
    )


@app.cell
def _(Agent, BaseModel, Dependencies, Field, List, fetch_reviews):
    MARKETING_PROMPT = """
    As a seasoned mobile app marketing specialist, your expertise lies in crafting compelling and engaging marketing copy that resonates with users. Your goal is to create clear, focused, and persuasive messaging that drives user acquisition and retention. Please provide a detailed marketing strategy that includes:

    Target Audience Analysis: Define the ideal user personas for the mobile app, including demographics, interests, and pain points.

    Key Messaging: Develop a concise value proposition that highlights the unique features and benefits of the app.

    Marketing Channels: Identify the most effective channels for reaching the target audience (e.g., social media, email marketing, in-app messaging) and provide examples of tailored copy for each channel.

    Call-to-Action Strategies: Suggest strong calls-to-action that encourage users to download the app or engage with its features.

    Performance Metrics: Outline how to measure the success of the marketing efforts, including key performance indicators (KPIs) to track user engagement and conversion rates.

    Your response should be structured, actionable, and include examples where applicable to illustrate your points.
    """.strip()

    class MarketingResult(BaseModel):
        praised_features: List[str] = Field(
            description="Prioritized list of features that users praise the most.  One item per line."
        )
        important_phrases: List[str] = Field(
            description="List of phrases that the marketing team should include in the copy. One item per line."
        )

    marketing_agent = Agent(
        'google-gla:gemini-2.0-flash',
        # ollama_model,
        deps_type=Dependencies,
        result_type=MarketingResult,
        system_prompt=MARKETING_PROMPT,
        tools=[fetch_reviews],
    )
    return MARKETING_PROMPT, MarketingResult, marketing_agent


@app.cell
def _(Agent, BaseModel, Dependencies, Field, List):
    class PlanningResult(BaseModel):
        app_names: List[str] = Field(description="List of suggested app names")
        marketing_copy: str = Field(
            description="Marketing copy of the app to build. 2-3 paragraphs at most"
        )
        mvp_features: List[str] = Field(
            description="List of features to include in the MVP of the app"
        )
        possible_issues: List[str] = Field(
            description="Prioritized list of possible bugs that might come up during development"
        )

    planner_agent = Agent('google-gla:gemini-2.0-flash', deps_type=Dependencies, result_type=PlanningResult)
    return PlanningResult, planner_agent


@app.cell
def _(Dependencies, RunContext, planner_agent):
    @planner_agent.system_prompt
    async def get_system_prompt(ctx: RunContext[Dependencies]) -> str:
        return f"""
    You're planning an MVP for new {ctx.deps.app_description} app. You'll propose
    the best possible way to approach the process of building it.
    """.strip()
    return (get_system_prompt,)


@app.cell
def _(Dependencies, improvement_agent, marketing_agent, planner_agent):
    # Run Agents 

    #  to determine the overall user experience rating, if available, and identify specific features or aspects that users consistently praise or criticize, presenting the findings in a concise, bullet-point format to clearly highlight the app's strengths and weaknesses.

    deps = Dependencies(
        app_description="Facebook"
    )

    improvement_result = improvement_agent.run_sync(
        "Please analyze the customer reviews for our product, focusing on identifying specific areas for improvement. Consider aspects such as product features, usability, customer service, and overall satisfaction. Provide a detailed summary of common themes, both positive and negative, and suggest actionable recommendations based on the feedback. Additionally, categorize the reviews into strengths and weaknesses to help prioritize which areas need the most attention. Aim for a comprehensive analysis that can guide our product development and customer service strategies. Desired Outcome: A detailed analysis of customer feedback with actionable insights for product improvement.", deps=deps
    )

    # for item in improvement_result.new_messages():
    #     print(item)

    # for item in improvement_result.data.issues:
    #     print(f"- {item}")

    # print()

    # for item in improvement_result.data.feature_requests:
    #     print(f"- {item}")

    # print()
    # print()


    marketing_result = marketing_agent.run_sync(
        "Based on the provided customer reviews, generate compelling marketing materials that highlight the product's key strengths and address any identified weaknesses, focusing on crafting persuasive copy that resonates with potential users and effectively communicates the product's value proposition.", deps=deps
    )

    # for item in marketing_result.new_messages():
    #     print(item)

    # for item in marketing_result.data.praised_features:
    #     print(f"- {item}")

    # print()

    # for item in marketing_result.data.important_phrases:
    #     print(f"- {item}")


    prompt = f"""Propose an MVP based on these reports:

    # Improvements:
    common issues:
    {improvement_result.data.issues}

    feature requests:
    {improvement_result.data.feature_requests}

    # Marketing:
    praised features:
    {marketing_result.data.praised_features}

    important phrases:
    {marketing_result.data.important_phrases}
    """

    planner_result = planner_agent.run_sync(prompt, deps=deps)

    # for itm in planner_result.data.app_names:
    #     print(itm)

    # for item in planner_result.data.marketing_copy.split("\n"):
    #     print(f"{textwrap.fill(item, 100)}")

    # for item in planner_result.data.mvp_features:
    #     print(f"- {item}")

    print(planner_result.all_messages())
    return deps, improvement_result, marketing_result, planner_result, prompt


@app.cell
def _(deps, planner_agent, planner_result, textwrap):
    planner_new_result = planner_agent.run_sync(
        "Focus the mvp features on the app functionality - habit tracking and tasks. Give a detailed explanation of the features.",
        message_history=planner_result.new_messages(),
        deps=deps,
    )

    for item in planner_new_result.data.mvp_features:
        print(f"- {textwrap.fill(item, 100)}")

    print()
    return item, planner_new_result


if __name__ == "__main__":
    app.run()
