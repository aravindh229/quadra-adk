class StrategyAgent:
    def run(self, activity_summary, voice_summary):
        # Segment users
        def classify_user(row):
            if row['active_days'] >= 100:
                return 'Power User'
            elif row['active_days'] <= 10 or row['avg_calorie_pct'] < 80:
                return 'At-Risk User'
            elif row['avg_calorie_pct'] > 120:
                return 'Overeater'
            elif row['avg_calorie_pct'] < 80:
                return 'Undereater'
            else:
                return 'Balanced'

        activity_summary['user_segment'] = activity_summary.apply(classify_user, axis=1)

        # Count per segment
        segment_counts = activity_summary['user_segment'].value_counts().to_dict()

        report = f"""
# 📊 QUADRA Strategy Agent Report

## 👥 User Segmentation
"""
        for segment, count in segment_counts.items():
            emoji = {
                "Power User": "🏆",
                "At-Risk User": "⚠️",
                "Overeater": "🍔",
                "Undereater": "🥗",
                "Balanced": "✅"
            }.get(segment, "")
            report += f"- {emoji} {segment}: {count}\n"

        report += f"""

## 📈 Key Behavioral Patterns
- Power users are consistent — opportunities for referral and upsell.
- At-risk users are disengaged — likely to churn without help.
- Overeaters may benefit from portion nudges or streak gamification.
- Undereaters may have unrealistic goals or inconsistent logging.

## 💬 Voice of the User (Synthesized)
{voice_summary['generated_prompt']}

---

QUADRA recommends acting on the top 3 friction points identified by users and deploying growth ideas for each segment to improve retention and engagement.
"""

        return report
