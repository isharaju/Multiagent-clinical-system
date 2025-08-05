# Clinical Trials Finder Agent

This project provides an AI-powered tool to help users find **actively recruiting clinical trials** near their location based on condition, age, gender, and ZIP code.

It integrates:

- 🔍 Real-time data from [ClinicalTrials.gov](https://clinicaltrials.gov)
- 🧠 Basic eligibility parsing (age/gender-based)
- 📍 Distance ranking using `geopy`
- 🌐 A Streamlit-based web UI
- 🚀 A FastAPI backend endpoint

---

## 📦 Features

- Query trials for a given disease or condition
- Filter by location and recruiting status
- Parse trial eligibility to check gender restrictions
- Rank trials by proximity to user ZIP code
- Present a summarized list of matched trials

---

## 🛠️ How to Run

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Start the FastAPI backend

```bash
uvicorn main:app --reload
```

The API will be available at:
```
POST http://localhost:8000/query_trials
```

Example payload:
```json
{
  "query": "I’m a 62-year-old female in Chicago with Parkinson's looking for trials within 50 miles.",
  "zip_code": "60601"
}
```

---

### Step 3: Run the Streamlit frontend

```bash
streamlit run frontend.py
```

Use the UI to enter:
- Condition (e.g., Parkinson's)
- Age
- Gender
- ZIP Code
- Travel Radius

---

## 📁 Folder Structure

```
.
├── main.py                 # FastAPI backend
├── frontend.py             # Streamlit frontend
├── tools/
│   ├── clinical_trials.py
│   ├── eligibility_parser.py
│   ├── geopy_tool.py
│   └── summary_generator.py
├── requirements.txt
└── README.md
```

---

## 🚧 Next Steps (Future Ideas)
- Integrate full eligibility criteria parsing
- Add contact email + phone from trials
- Add maps with trial locations
- Expand to other countries

---

Built with ❤️ using FastAPI, LangChain-style tools, and Streamlit.
