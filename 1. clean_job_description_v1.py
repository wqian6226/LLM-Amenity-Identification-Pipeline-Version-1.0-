# =====================================================
# Version: 1.0
# Author: Qian
# Project: Pricing Job Amenities
# Purpose:
#     Clean Chinese online job descriptions for LLM-based amenity identification.

# Pipeline
# Step 1. Read data
# Step 2. Clean job description
# Step 3. Build LLM-ready text
# Step 4. Generate variables
# Step 5. Keep variables for LLM annotation
# Step 6. Save
# =====================================================

import pandas as pd
import re
from bs4 import BeautifulSoup
import html

# =====================================================
# Step 1. Read data
# =====================================================
df = pd.read_excel("analysis_subsample.xlsx")

# =====================================================
# Step 2. Clean job description
# =====================================================
def clean_job_description(text):

    # -------------------------------------------------
    # Missing values
    # -------------------------------------------------
    if pd.isna(text):
        return ""
    text = str(text)

    # -------------------------------------------------
    # Decode HTML
    # -------------------------------------------------
    text = html.unescape(text)
    text = BeautifulSoup(
        text,
        "lxml"
    ).get_text(separator="\n")
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    # -------------------------------------------------
    # Remove webpage artifacts(网页噪声)
    # -------------------------------------------------
    text = text.replace("\xa0", " ")
    # HTML生成的大量 -
    text = re.sub(r'([：:])\s*-\s*', r'\1', text)
    text = re.sub(r'([；;。！，,])\s*-\s*', r'\1', text)
    text = re.sub(r'(\d+)-([、．。.])', r'\1\2', text)
    text = re.sub(r'（(\d+)）\s*-\s*', r'（\1）', text)
    text = re.sub(r'(\d+)\.\s*-\s*', r'\1.', text)
    text = re.sub(r'(\d+[、.．])\s*-\s*', r'\1', text)
    # 删除单独一行 -
    text = re.sub(
        r'(?m)^\s*-\s*$',
        '',
        text
    )
    # 删除 ------
    text = re.sub(
        r'(?:-\s*){3,}',
        '',
        text
    )
    # 删除 bullet
    text = re.sub(
        r'[●•▪■◆○▶►☑√]\s*-*\s*',
        '',
        text
    )

    # -------------------------------------------------
    # Repair broken numbers(数字修复)
    # -------------------------------------------------
    # 20\n-28岁
    text = re.sub(
        r'(\d+)\n*-\n*(\d+)\n*(岁|年|个月|月)',
        r'\1-\2\3',
        text
    )
    # 5000-\n8000
    text = re.sub(
        r'(\d)-\n+(\d)',
        r'\1-\2',
        text
    )
    # 5\n000 → 5000
    while re.search(r'(\d)\n+(\d)', text):
        text = re.sub(
            r'(\d)\n+(\d)',
            r'\1\2',
            text
        )
    # 20\n年以上
    text = re.sub(
        r'(\d)\n+(年|个月|月|天|小时|薪|年以上|以下)',
        r'\1\2',
        text
    )

    # -------------------------------------------------
    # Repair broken Chinese text(中文文本修复)
    # -------------------------------------------------
    # 中文短语被换行
    text = re.sub(
        r'([一-龥]{2,})\n+([一-龥]{1,4})',
        r'\1\2',
        text
    )
    # 连续单字断裂
    pattern = re.compile(
        r'((?:[\u4e00-\u9fff]\n){2,}[\u4e00-\u9fff])'
    )
    while True:

        new_text = pattern.sub(
            lambda m: m.group().replace("\n", ""),
            text
        )
        if new_text == text:
            break
        text = new_text

    # -------------------------------------------------
    # Normalize punctuation(标点规范化)
    # -------------------------------------------------
    text = re.sub(
        r'\n([，。；：！？])',
        r'\1',
        text
    )
    text = re.sub(
        r'([，。；：！？])\n+',
        r'\1',
        text
    )
    text = re.sub(
        r'\s*([：:])\s*',
        r'\1',
        text
    )
    text = re.sub(
        r'(\d+)\s+、',
        r'\1、',
        text
    )

    # -------------------------------------------------
    # Normalize formatting(格式规范化)
    # -------------------------------------------------
    text = re.sub(
        r'\s*—\s*',
        '—',
        text
    )
    text = re.sub(
        r'•\s*\n+',
        '• ',
        text
    )
    text = re.sub(
        r'(\d+)\.\s*\n+\s*([^\n])',
        r'\1. \2',
        text
    )
    text = re.sub(
        r'(\d+、)\s*\n+\s*([^\n])',
        r'\1\2',
        text
    )

    # -------------------------------------------------
    # Normalize section headers
    # -------------------------------------------------
    text = re.sub(
        r'岗位职责：\s*工作职责：',
        '岗位职责：',
        text
    )
    text = re.sub(
        r'-+\s*【',
        '【',
        text
    )
    text = re.sub(
        r'【\s*([^】]+?)\s*】',
        lambda m: m.group(1).strip() + "：",
        text
    )

    # -------------------------------------------------
    # Normalize spaces
    # -------------------------------------------------
    text = re.sub(
        r'[ \t]+',
        ' ',
        text
    )
    text = re.sub(
        r'\n\s*\n+',
        '\n',
        text
    )

    return text.strip()


# =====================================================
# Step 3. Build LLM-ready text
# =====================================================
def build_llm_text(text):

    if pd.isna(text):
        return ""
    text = str(text)

    # =====================================================
    # Merge section headings
    # =====================================================
    headers = [
        "岗位职责",
        "工作职责",
        "职责描述",
        "职位描述",
        "职位要求",
        "岗位要求",
        "任职要求",
        "岗位要求及任职资格",
        "任职资格",
        "技能要求",
        "岗位说明",
        "工作内容",
        "薪酬",
        "福利",
        "待遇",
        "工作时间",
        "工作地点",
        "福利待遇",
        "晋升发展",
        "学历要求",
        "专业要求",
        "工作经验",
        "其他要求",
    ]

    for h in headers:
        text = re.sub(
            rf"({h}[：:])\s*\n+",
            r"\1",
            text
        )

    # =====================================================
    # Remove webpage buttons
    # =====================================================
    remove_words = [
        "立即申请",
        "举报",
        "收藏职位",
        "职位收藏",
        "分享",
        "微信分享",
        "分享到朋友圈",
        "申请职位",
        "投递简历"
    ]

    for w in remove_words:
        text = text.replace(w, "")

    # =====================================================
    # Remove duplicated English JD
    # =====================================================
    english_headers = [
        r"Job[\s\-_]*Description",
        r"Job[\s\-_]*Responsibilities",
        r"Job[\s\-_]*Requirement[s]?",
        r"Responsibilities",
        r"Qualifications",
        r"Requirement[s]?"
    ]
    pattern = "(" + "|".join(english_headers) + ")"
    match = re.search(
        pattern,
        text,
        flags=re.IGNORECASE
    )
    if match:
        text = text[:match.start()]

    # =====================================================
    # Remove empty lines
    # =====================================================
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if line:
            lines.append(line)
    text = "\n".join(lines)

    # =====================================================
    # Remove excessive blank lines
    # =====================================================
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()

# =====================================================
# 4. Generate variables
# =====================================================
df["jobdes_clean"] = df["jobdes"].apply(clean_job_description)
df["jobdes_llm"] = df["jobdes_clean"].apply(build_llm_text)

# =====================================================
# 5. Keep variables for LLM annotation
# =====================================================
df = df.rename(columns={
    "职位标题": "jobtitle",
    "福利": "benefits"
})

keep_vars = [
    "user_id",
    "year",
    "jobid",
    "jobtitle",
    "jobdes",
    "benefits",
    "jobdes_clean",
    "jobdes_llm"
]

# Keep only variables that exist in the dataset
existing_vars = [v for v in keep_vars if v in df.columns]
df = df[existing_vars]

# =====================================================
# Step 6. Save
# =====================================================

df.to_excel(
    "analysis_subsample_clean.xlsx",
    index=False
)

print("Finished!")