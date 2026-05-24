import os
import re

replacements = {
    r'rgba\(13,\s*188,\s*130,': 'rgba(59,130,246,',
    r'rgba\(95,\s*255,\s*202,': 'rgba(147,197,253,',
    r'rgba\(144,\s*253,\s*210,': 'rgba(191,219,254,',
    r'rgba\(1,\s*45,\s*34,': 'rgba(23,37,84,',
    r'rgba\(0,\s*255,\s*191,': 'rgba(34,211,238,',
    r'rgba\(0,\s*255,\s*217,': 'rgba(34,211,238,',
    r'rgba\(121,\s*249,\s*255,': 'rgba(165,243,252,',
    r'rgba\(0,\s*255,\s*94,': 'rgba(59,130,246,',
    r'rgba\(34,\s*197,\s*94,': 'rgba(59,130,246,',
    r'rgba\(71,\s*255,\s*194,': 'rgba(96,165,250,',
    r'rgba\(7,\s*255,\s*173,': 'rgba(59,130,246,',
    r'green-400': 'blue-400',
    r'emerald-50': 'blue-50'
}

for root, _, files in os.walk('/home/coherent/Project/REACT/React_Portfolio-master/src'):
    for file in files:
        if file.endswith(('.astro', '.css', '.md', '.ts', '.tsx', '.js', '.jsx')):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            original_content = content
            for old, new in replacements.items():
                content = re.sub(old, new, content)
            if content != original_content:
                print(f"Updated {filepath}")
                with open(filepath, 'w') as f:
                    f.write(content)
