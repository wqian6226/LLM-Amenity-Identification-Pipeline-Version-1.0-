# Pricing Job Amenities

## Project Overview

This project develops a large-scale measure of job amenities using Chinese online job advertisements. The objective is to construct economically meaningful amenity variables that can be used to estimate compensating wage differentials.

Unlike existing studies relying solely on structured benefit fields, this project combines structured recruitment information with Large Language Models (LLMs) to identify both explicit and implicit job amenities contained in job descriptions.

The workflow follows the principles discussed with the research team (Alex Bell, Lars Lefgren, and Shuaizhang Feng): taxonomy development → text preprocessing → prompt engineering → small-sample validation → large-scale extraction.

---

# Project Structure

```
Pricing Job Amenities
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── llm_output/
│
├── code/
│   ├── 01_text_cleaning.py
│   ├── 02_prompt_development.py
│   ├── 03_llm_annotation.py
│   ├── 04_post_processing.py
│   └── utils.py
│
├── prompt/
│   ├── system_prompt.md
│   └── user_prompt.md
│
├── taxonomy/
│   ├── amenity_taxonomy.xlsx
│   └── identification_protocol.pdf
│
├── sample/
│   ├── analysis_subsample.xlsx
│   └── analysis_subsample_clean.xlsx
│
└── README.md
```

---

# Research Workflow

The project consists of five stages.

## Stage 1. Amenity Taxonomy

Develop an economically motivated amenity taxonomy based on the labor economics literature and characteristics of Chinese recruitment advertisements.

The taxonomy contains

- Broad amenity category
- Amenity dimension
- Specific amenity
- Definition
- Identification source

---

## Stage 2. Purposeful Sampling

Construct a small development sample for prompt engineering.

The sample contains approximately 300 job advertisements selected to cover all amenity categories.

Sampling combines

- occupation-driven sampling
- text-driven sampling

to ensure sufficient coverage of relatively rare amenities.

---

## Stage 3. Text Cleaning

Chinese job descriptions are preprocessed before entering the LLM.

Main cleaning steps include

- removing HTML tags
- decoding HTML entities
- removing webpage artifacts
- repairing broken numbers
- repairing broken Chinese text
- normalizing punctuation
- removing duplicated English descriptions
- generating LLM-ready text

The cleaned text is stored in

```
jobdes_llm
```

---

## Stage 4. Prompt Development

Prompts are developed using the cleaned development sample.

Following the recommendations from the research team, prompt development is fully documented.

For each prompt version we record

- prompt text
- model
- temperature
- output format
- ambiguous cases
- revisions

The first development sample is used only for prompt refinement rather than final estimation.

---

## Stage 5. Large-scale Amenity Extraction

After the prompt reaches satisfactory consistency, it is applied to the full recruitment dataset.

Each job posting is classified into multiple amenity dimensions.

---

# Amenity Identification

Amenities are identified using two sources.

## 1. Structured Recruitment Fields

Used when the information is explicitly provided.

Examples

- Social security
- Housing fund
- Meal subsidy
- Transport subsidy
- Paid annual leave

---

## 2. Large Language Model (LLM)

Used for amenities embedded in free-text job descriptions.

Examples include

- Permanent contract
- Long-term employment
- Worker-oriented flexibility
- Employer-oriented scheduling unpredictability
- Meaning
- Authority
- Autonomy
- Physical demands
- Outdoor work
- Hazardous work
- Stress
- Training
- Promotion opportunities
- Skill development

Each amenity follows a separate Identification Protocol specifying

- economic definition
- decision rules
- boundary cases
- examples

---

# Notes

JAAT is not used in this project.

Although JAAT can generate O*NET occupation codes and task statements, it currently only supports English job postings. Because the recruitment dataset contains millions of Chinese job advertisements, translating the entire corpus into English is not practically feasible. Therefore, amenity identification relies on structured recruitment fields together with LLM-based classification of Chinese job descriptions.

---

# Current Status

- ✓ Amenity taxonomy completed
- ✓ Development sample constructed
- ✓ Text cleaning completed
- □ Prompt engineering
- □ Small-sample validation
- □ Large-scale LLM extraction
- □ Dataset construction
- □ Econometric analysis

---

# Author

Qian Wan

Project:
Pricing Job Amenities

Department of Economics

South China Normal University
