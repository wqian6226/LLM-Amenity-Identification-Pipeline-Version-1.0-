# LLM-Amenity-Identification-Pipeline (Version 1.0)

Author: Qian Wan

Project: Pricing Job Amenities

Last Updated: August 2026

---

# Project Overview

This repository contains the first version of the LLM-based pipeline for identifying job amenities from Chinese online job advertisements.

The project aims to construct economically meaningful non-wage job amenities by combining:

- structured recruitment information,
- cleaned Chinese job descriptions,
- Large Language Models (LLMs).

The pipeline follows the development strategy discussed with Alex Bell, Lars Lefgren, and Shuaizhang Feng:

> Amenity Taxonomy → Purposeful Sampling → Text Cleaning → Prompt Development → LLM Annotation

Rather than applying the LLM directly to the full dataset, Version 1.0 focuses on developing and validating the complete workflow using a manually selected development sample.

---

# Project Structure

```
LLM-Amenity-Identification-Pipeline-Version-1.0
│
├── 1. clean_job_description_v1.py
│      Text preprocessing pipeline
│
├── 2. prompt_v1.txt
│      Prompt for LLM-based amenity identification
│
├── 3. run_llm_batch.py
│      Batch inference script
│
├── 4. Amenity Taxonomy Proposal.xlsx
│      Amenity taxonomy and definitions
│
├── analysis_subsample.xlsx
│      Raw development sample
│
├── analysis_subsample_clean.xlsx
│      Cleaned sample used for LLM input
│
└── README.md
```

---

# Research Workflow

## Step 1. Amenity Taxonomy

Develop an economically motivated taxonomy of job amenities based on:

- labor economics literature;
- characteristics of Chinese online recruitment advertisements.

Each amenity includes:

- Broad category
- Amenity dimension
- Specific amenity
- Economic definition
- Identification source

The taxonomy is documented in:

```
Amenity Taxonomy Proposal.xlsx
```

---

## Step 2. Development Sample

A purposeful sample of job advertisements was constructed for prompt development.

The sample was designed to ensure sufficient coverage of all amenity categories, including relatively uncommon amenities such as

- Permanent contract
- Long-term employment
- Promotion opportunities
- Skill development
- Training

The development sample contains both raw and cleaned versions.

```
analysis_subsample.xlsx
analysis_subsample_clean.xlsx
```

---

## Step 3. Text Cleaning

Chinese job descriptions were cleaned before entering the LLM.

The preprocessing script removes webpage noise while preserving economically meaningful information.

Main cleaning procedures include

- HTML decoding
- HTML tag removal
- webpage artifact removal
- repairing broken Chinese text
- repairing broken numbers
- punctuation normalization
- duplicated English description removal
- formatting normalization

The final LLM input is stored in

```
jobdes_llm
```

Script:

```
1. clean_job_description_v1.py
```

---

## Step 4. Prompt Development

Prompt engineering is performed using the cleaned development sample.

The objective is to translate economic definitions into explicit annotation rules that can be consistently followed by the LLM.

Prompt Version 1.0 is stored in

```
2. prompt_v1.txt
```

Future versions will be documented separately.

---

## Step 5. LLM Annotation

The cleaned job descriptions are submitted to the LLM in batches.

Each posting is evaluated against the predefined amenity taxonomy.

Outputs include

- amenity classifications
- explanations
- confidence (if requested)

Script:

```
3. run_llm_batch.py
```

---

# Amenity Identification Strategy

Amenities are identified from two complementary information sources.

## 1. Structured Recruitment Information

Used when amenities are explicitly provided.

Examples include

- Social security
- Housing fund
- Meal subsidy
- Transport subsidy
- Paid annual leave

---

## 2. Large Language Model (LLM)

Used when amenities are embedded in free-text job descriptions.

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

Each amenity follows an Identification Protocol specifying

- economic definition
- decision rules
- boundary cases

---

# Current Pipeline Status

| Stage | Status |
|---------|--------|
| Amenity taxonomy | ✓ Completed |
| Development sample | ✓ Completed |
| Text cleaning | ✓ Completed |
| Prompt Version 1.0 | ☐ In progress |
| Batch inference code | ☐ In progress |
| Prompt validation | ☐ In progress |
| Prompt refinement | ☐ Planned |
| Full-sample annotation | ☐ Planned |

---

# Notes

## JAAT

JAAT is not used in this pipeline.

Although JAAT can generate occupation codes and O*NET task statements, it currently supports only English job postings.

Because the recruitment dataset consists of millions of Chinese job advertisements, translating the entire corpus into English is not practically feasible.

Therefore, Version 1.0 identifies amenities using

- structured recruitment fields
- cleaned Chinese job descriptions
- LLM-based semantic classification.

---

# Future Development

Version 2.0 will include

- Prompt refinement based on ambiguous cases
- Identification Protocol documentation
- Inter-prompt consistency evaluation
- Full-sample LLM annotation
- Post-processing and quality control

---

# Citation

This repository was developed as part of the project

**Pricing Job Amenities**

Department of Economics

South China Normal University

2026
