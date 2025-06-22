import pandas as pd
import json

class InsightAgent:
    def run(self):
        file_path = '/content/drive/MyDrive/QUADRA/data/mfp-diaries.tsv'
        all_outputs = []

        # Read the file in 10,000-row chunks
        chunks = pd.read_csv(file_path, sep='\t', chunksize=10000)

        for chunk in chunks:
            for index, row in chunk.iterrows():
                try:
                    user_id = row.iloc[0]
                    date = row.iloc[1]
                    daily_summary = json.loads(row.iloc[3])

                    total_nutrition = {
                        item['name']: float(str(item['value']).replace(',', '').strip())
                        for item in daily_summary['total']
                    }

                    goal_nutrition = {
                        item['name']: float(str(item['value']).replace(',', '').strip())
                        for item in daily_summary['goal']
                    }

                    all_outputs.append({
                        'user_id': user_id,
                        'date': date,
                        'calories_total': total_nutrition.get('Calories', 0),
                        'calories_goal': goal_nutrition.get('Calories', 0),
                        'protein_total': total_nutrition.get('Protein', 0),
                        'protein_goal': goal_nutrition.get('Protein', 0),
                        'carbs_total': total_nutrition.get('Carbs', 0),
                        'carbs_goal': goal_nutrition.get('Carbs', 0),
                        'fat_total': total_nutrition.get('Fat', 0),
                        'fat_goal': goal_nutrition.get('Fat', 0),
                        'sugar_total': total_nutrition.get('Sugar', 0),
                        'sugar_goal': goal_nutrition.get('Sugar', 0)
                    })

                except Exception:
                    continue

        # Final DataFrame
        df_clean = pd.DataFrame(all_outputs)
        df_clean['date'] = pd.to_datetime(df_clean['date'])
        df_clean = df_clean.sort_values(by=['user_id', 'date'])

        # Add goal completion %
        df_clean['calorie_pct'] = (df_clean['calories_total'] / df_clean['calories_goal']) * 100
        df_clean['calorie_flag'] = df_clean['calorie_pct'].apply(
            lambda x: 'Under' if x < 90 else ('Over' if x > 110 else 'OK')
        )

        # Summarize behavior per user
        activity_summary = df_clean.groupby('user_id').agg(
            active_days=('date', 'nunique'),
            avg_calorie_pct=('calorie_pct', 'mean'),
            overeat_days=('calorie_flag', lambda x: (x == 'Over').sum()),
            undereat_days=('calorie_flag', lambda x: (x == 'Under').sum()),
        )

        # Add churn risk flag
        activity_summary['churn_risk'] = activity_summary['active_days'].apply(
            lambda x: 'High' if x < 5 else 'Low'
        )

        return df_clean, activity_summary
