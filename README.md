# quadra-adk
# QUADRA: The Strategic Co-Pilot for Product Teams

> *"The most powerful insights aren't just delivered. They're discovered, reasoned, and orchestrated by intelligent systems."*  — QUADRA

---

## 🌍 The Problem We Set Out to Solve

In a world where user churn can break billion-dollar apps, most product teams still operate reactively. They analyze data in fragments, interview customers late, and experiment with strategies that are already outdated. We asked ourselves:

**What if a product team had a virtual co-pilot that processed everything for them — user logs, sentiment, behavior patterns — and distilled it into strategy?**

---

## 🧠 Meet QUADRA: A Multi-Agent AI System

QUADRA is an intelligent, multi-agent product strategist built using the philosophy of Google’s Agent Development Kit (ADK). It simulates a full-stack product team: a data analyst, a behavioral researcher, a growth hacker, and a strategic product lead — each powered by a specialized AI agent.

Imagine Sundar Pichai meets Steve Jobs meets Satya Nadella — each playing their part to help you understand *why* users churn and *what you should do about it*.

---

## 🤖 Agent Architecture

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

## 🧩 The 4 Agents of QUADRA

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

## ⚠️ Dataset Note

Due to file size, `mfp-diaries.tsv` (2GB+) is not stored on GitHub. Place it manually inside the `data/` folder. The path is already hardcoded to work with Google Drive:

```python
'/content/drive/MyDrive/QUADRA/data/mfp-diaries.tsv'
```

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

> \[Link to 3-min demo on YouTube or Loom] *(To be added)*

---

## 🏁 Submission Category

**Category:** Data Analysis & Insights
**Region:** Asia Pacific (India)
**Devpost:** [QUADRA Hackathon Page](https://googlecloudmultiagents.devpost.com/)

---

## ✨ Credits

Built with purpose by \[Aravindh] — a product-thinker with a data backbone.
Thank you Google & Devpost for making space for this experiment in human-AI collaboration.

---

## 💬 Final Thought

> *"If Steve Jobs designed the product vision, Sundar scaled the platform, and Satya built the infrastructure — QUADRA is the brain they would share."*

---
