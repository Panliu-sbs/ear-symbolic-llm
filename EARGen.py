
"""
EARGen: Convert Natural Language Input to EAR Triplets and Algebraic Expressions
Author: Pan Liu, Yihao Li
"""

import re

# 示例实体、属性、关系抽取（可替换为更复杂的 NLP 模块）
def extract_ear_elements(text):
    entities = re.findall(r'\b[A-Z][a-zA-Z0-9_]*\b', text)
    attributes = re.findall(r'(\bexecution time\b|\bseverity\b|\bstatus\b)', text, flags=re.I)
    relations = []
    if "depends on" in text:
        parts = text.split("depends on")
        if len(parts) == 2:
            relations.append(('Rdep', parts[0].strip(), parts[1].strip('. ')))
    if "must be less than" in text:
        value = re.findall(r'less than ([0-9]+)', text)
        if value:
            relations.append(('Rconstr', 'TotalTime', f'TotalTime < {value[0]}'))
    return entities, attributes, relations

# EAR triplet 到 Algebra 表达式转换
def map_to_algebra(triplets):
    algebra = []
    for rtype, subj, obj in triplets:
        if rtype == 'Rdep':
            algebra.append(f"{subj} ⋅ {obj}")
        elif rtype == 'Rconstr':
            algebra.append(f"{subj} / {{{obj}}}")
    return ' ⋅ '.join(algebra)

# 主函数
def generate_ear_prompt(text):
    entities, attributes, relations = extract_ear_elements(text)
    algebra_expr = map_to_algebra(relations)
    return {
        'Entities': entities,
        'Attributes': attributes,
        'Relations': relations,
        'Algebraic Expression': algebra_expr
    }

# 示例
if __name__ == "__main__":
    input_text = "ModuleA depends on ModuleB. The total execution time must be less than 10 seconds."
    result = generate_ear_prompt(input_text)
    for key, val in result.items():
        print(f"{key}: {val}")
