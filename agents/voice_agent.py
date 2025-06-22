class VoiceAgent:
    def run(self, user_reviews):
        prompt = f"""
You are QUADRA’s Research Agent.

Here are 25 real user reviews:
{chr(10).join(user_reviews)}

Your job is to:
- Identify the top 3–5 recurring pain points or feedback themes.
- Categorize them as: UX, performance, pricing, features, or motivation.
- Write a short summary for each theme.
- Add the general sentiment tone: Positive, Negative, or Mixed.

Return your response as bullet points, labeled clearly.
"""

        # Simulated agent (you could connect to Vertex AI or OpenAI here)
        return {
            "agent_name": "Voice Agent",
            "review_count": len(user_reviews),
            "generated_prompt": prompt
        }
