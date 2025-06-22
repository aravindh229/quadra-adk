# ✅ Imports — make sure agent class names match file structure
from agents.insight_agent import InsightAgent
from agents.growth_agent import GrowthAgent
from agents.voice_agent import VoiceAgent
from agents.strategy_agent import StrategyAgent

# ✅ Load reviews from .txt file
def load_reviews_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

# ✅ Main execution logic
def main():
    print("🔍 Running Insight Agent...")
    df_clean, activity_summary = InsightAgent().run()

    print("📈 Running Growth Agent...")
    activity_summary = GrowthAgent().run(activity_summary)

    print("🗣️ Running Voice Agent...")
    reviews_path = '/content/drive/MyDrive/QUADRA/data/user_reviews.txt'
    user_reviews = load_reviews_from_file(reviews_path)
    voice_summary = VoiceAgent().run(user_reviews)

    print("🎯 Running Strategy Agent...")
    final_report = StrategyAgent().run(activity_summary, voice_summary)

    print("\n✅ QUADRA SYSTEM OUTPUT:\n")
    print(final_report)

    # 🔒 Optional: Save output as markdown in Drive
    with open("/content/drive/MyDrive/QUADRA/quadra_report.md", "w", encoding="utf-8") as f:
        f.write(final_report)

# ✅ THIS LINE IS CRUCIAL
if __name__ == "__main__":
    main()