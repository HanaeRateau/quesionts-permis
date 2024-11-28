import re
import json

def parse_questions(text):
    # Updated regex pattern
    pattern = r'uestion[s]? (\d+(?:\s*et\s*\d+)?)\n*Vérifications\s+(?:intérieures|extérieures)\n\n([\S\s]*?)\n*Réponse\s*:\s*([\S\s]*?)\n*\n*Sécurité routière\n\n([\S\s]*?)\n*Réponse\s*:\s*([\S\s]*?)\n*Premiers secours\n\n([\S\s]*?)\n*Réponse\s*:\s*([\S\s]+?\n)\n*Q'
    
    # Find all matches
    matches = re.findall(pattern, text, re.MULTILINE)
    
    # Process matches into list of dictionaries
    results = []
    for match in matches:
        results.append({
            "question": match[0],
            "verification": {
                "details": match[1].strip(),
                "answer": match[2].strip()
            },
            "securite": {
                "details": match[3].strip(),
                "answer": match[4].strip()
            },
            "premier_secours": {
                "details": match[5].strip(),
                "answer": match[6].strip()
            }
        })
    
    return results


with open("questions.txt", encoding="utf8") as f:
    result = parse_questions(f.read())

with open("questions.json", 'w', encoding="utf8") as f_results:
    print(json.dumps(result, ensure_ascii=False, indent=2))
    f_results.write(json.dumps(result, ensure_ascii=False, indent=2))