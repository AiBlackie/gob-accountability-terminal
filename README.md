# GOB Accountability Terminal 📉🇧🇧

An objective, open-source dashboard designed to track and visualize the Government of Barbados' compliance with statutory financial reporting deadlines under the **Public Finance Management Act, 2019-1 (PFMA)**.

## 🎯 Purpose
The primary legal obligation of the Accountant General is to submit the Government's Financial Statements to the Auditor General within four months of the fiscal year end (by July 31st). This terminal visually tracks the exact number of days the Government is in breach of this law, translating complex institutional delays into plain, undeniable data.

## 📊 Key Features
*   **Live Delinquency Clock:** A real-time JavaScript counter tracking the exact days, hours, minutes, and seconds since the legal deadline was missed.
*   **Filing Status Matrix:** A visual heat-map showing the legal deadline, the actual submission date, and the resulting delay for every fiscal year from 2020 to the present.
*   **Digital Evidence Cross-Check:** Direct links to the official Treasury, Audit Office, and Parliament websites, allowing users to verify the exact filing status themselves.
*   **Plain English Glossary:** A built-in translation guide that explains dense accounting jargon (like "Adverse Opinion" and "IPSAS 35") to the general public.

## ⚙️ Technology Stack
*   **Python** (Streamlit)
*   **HTML/CSS/JavaScript** (Custom terminal-style UI and live ticker)
*   **Data Sourced Directly From:** Public Finance Management Act 2019-1, Auditor General Annual Reports, and official Government portals.

## 🚀 How to Run Locally
To run this dashboard on your own machine:
1. Clone this repository.
2. Install the required packages: `pip install -r requirements.txt`
3. Run the Streamlit app: `streamlit run app.py`

## ⚖️ Disclaimer
This is an independent civic technology project. The data presented is derived directly from publicly available legal documents and official Government of Barbados websites. It is designed to promote transparency, institutional accountability, and public financial literacy.
