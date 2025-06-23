# QUADRA: The Strategic Co-Pilot for Product Teams

> *"The most powerful insights aren't just delivered. They're discovered, reasoned, and orchestrated by intelligent systems."*  — QUADRA

---

## 🌍 The Problem We Set Out to Solve

In a world where user churn can break billion-dollar apps, most product teams still operate reactively. They analyze data in fragments, interview customers late, and experiment with strategies that are already outdated. We asked ourselves:

**What if a product team had a virtual co-pilot that processed everything for them — user logs, sentiment, behavior patterns — and distilled it into strategy?**

---

## 🧠 Meet QUADRA: A Multi-Agent AI System

QUADRA is an intelligent, multi-agent product strategist built using the philosophy of Google’s Agent Development Kit (ADK). It simulates a full-stack product team: a data analyst, a behavioral researcher, a growth hacker, and a strategic product lead — each powered by a specialized AI agent.

---

## 🧹 Agent Architecture

```plaintext
+-------------------+        +----------------+        +----------------+
|   Insight Agent   | -----> |  Growth Agent  | -----> | Strategy Agent |
+-------------------+        +----------------+        +----------------+
          |                          ^                        ^
          v                          |                        |
  +----------------+                |                        |
  |  Voice Agent   | ---------------+------------------------+
  +----------------+
```

---

## 🧹 The 4 Agents of QUADRA

### 1. **Insight Agent** — "The Data Brain"

* Ingests real user logs from 2GB `.tsv` file
* Parses and aggregates calorie, protein, fat, sugar intake
* Calculates user behavior summaries: active days, over/under-eat patterns
* Outputs churn risk classifications

### 2. **Growth Agent** — "The Experimenter"

* Analyzes user segments from Insight Agent
* Recommends growth nudges like streak challenges, goal reframing, reward systems
* Tailors strategies based on engagement and calorie behavior

### 3. **Voice Agent** — "The Researcher"

* Reads 50+ human-written user reviews (loaded from `.txt`)
* Synthesizes top pain points across UX, performance, pricing, and motivation
* Generates structured prompts for product reflection

### 4. **Strategy Agent** — "The Final Word"

* Consolidates all agent outputs
* Segments users (Power, At-Risk, Overeater, Balanced)
* Outputs a markdown strategy report: what’s happening, why it matters, what you should do

---

## 🛠 Tech Stack

* Python (pandas, json, re)
* Google Colab + Google Drive
* Structured modular architecture
* Optional integration with BigQuery / Vertex AI (future-ready)

---

## 📁 Project Folder Structure

```bash
QUADRA/
├── agents/
│   ├── insight_agent.py
│   ├── growth_agent.py
│   ├── voice_agent.py
│   └── strategy_agent.py
├── controller.py
├── data/
│   ├── user_reviews.txt
│   └── mfp-diaries.tsv  # Not included in repo (2GB file)
├── requirements.txt
├── quadra_report.md
└── README.md
```

---

## 🚀 How to Run QUADRA

1. Upload `mfp-diaries.tsv` (from Google Drive) to `/data/`
2. Open `controller.py` in Colab or Python
3. Run all agents:

```bash
python controller.py
```

4. Final report will be printed and saved to `quadra_report.md`

---

## ⚠️ Dataset Note & Citation

Due to file size, `mfp-diaries.tsv` (2GB+) is not stored on GitHub. Place it manually inside the `data/` folder. The path is already hardcoded to work with Google Drive:

```python
'/content/drive/MyDrive/QUADRA/data/mfp-diaries.tsv'
```

**Dataset Source:** [MyFitnessPal Dataset on Kaggle](https://www.kaggle.com/datasets/zvikinozadze/myfitnesspal-dataset) by Zvi Kinozadze

---

## 📄 Sample Output (Strategy Report)

```
# QUADRA Strategy Agent Report

## User Segmentation
- Power Users: 2243
- At-Risk Users: 5589
- Overeaters: 61
- Balanced: 2003

## Key Patterns
- At-risk users log inconsistently but over-target frequently
- Growth ideas include portion nudges, streak rewards, goal resetting

## Voice of the User
- "App crashes while logging dinner"
- "Too many ads"
- "Loved the barcode scanner"

## Action Plan
- Fix bugs, reduce friction, experiment with rewards for over-loggers
```

---

## 🎥 Demo Video

Youtube (https://youtu.be/odhstclfpJs)

---

## 🏁 Submission Category

**Category:** Data Analysis & Insights
**Region:** United States
**Devpost:** [QUADRA Hackathon Page](https://googlecloudmultiagents.devpost.com/)

---

## ✨ Credits

Created with care by **Aravindh**, a data driven product systems thinker with a drive to reimagine how product teams think and act.

This project is a practical, fully functioning prototype of what AI-assisted product decision-making could look like when modular intelligence meets real user behavior.

Special thanks to Kaggle for open data access, Google for the ADK vision, and Devpost for hosting this opportunity to build for real impact.

---

## 💬 Final Thought

> *"QUADRA is not a replacement for human intuition. It's the structured intelligence layer that empowers it."*

---
