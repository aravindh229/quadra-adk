class GrowthAgent:
    def run(self, activity_summary):
        def growth_recommendation(row):
            tips = []

            if row['churn_risk'] == 'High':
                tips.append("⚠️ High churn risk – trigger re-engagement email with benefits reminder.")

            if row['overeat_days'] > 10:
                tips.append("🥗 Suggest portion tracking feature or meal plan assistant.")

            if row['undereat_days'] > 10:
                tips.append("🍴 Encourage user to set a realistic goal with motivational coaching.")

            if row['avg_calorie_pct'] < 70:
                tips.append("🔔 Add smart reminder at mealtimes to log food.")

            if row['avg_calorie_pct'] > 120:
                tips.append("📉 Offer streak-based challenges to balance calories weekly.")

            if row['active_days'] > 100:
                tips.append("🏆 Power user! Offer referral bonus or upsell premium tier.")

            return tips

        # Apply the strategy logic
        activity_summary['growth_ideas'] = activity_summary.apply(growth_recommendation, axis=1)

        return activity_summary
