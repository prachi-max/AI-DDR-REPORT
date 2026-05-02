import json
from services.openai_service import call_gpt


import os

def load_prompt():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    prompt_path = os.path.join(base_dir, "prompts", "merge_prompt.txt")

    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()

def merge_data(inspection_data, thermal_data):
    prompt_template = load_prompt()

    # Convert Python → string (important for GPT)
    inspection_str = json.dumps(inspection_data, indent=2)
    thermal_str = json.dumps(thermal_data, indent=2)

    # Replace placeholders
    prompt = prompt_template.replace("{inspection_data}", inspection_str)
    prompt = prompt.replace("{thermal_data}", thermal_str)

    try:
        response = call_gpt(prompt, "Merge both datasets into unified insights.")

        # Parse JSON response
        merged = json.loads(response)
        return merged

    except json.JSONDecodeError:
        print("⚠️ JSON parsing failed in merger. Retrying...")

        # Retry once with stricter instruction
        response = call_gpt(prompt, "Return ONLY valid JSON. No explanation.")

        try:
            merged = json.loads(response)
            return merged
        except:
            return [{
                "area": "Not Available",
                "combined_issue": "Merge Error",
                "supporting_data": "Not Available",
                "conflict": "No",
                "conflict_details": "Parsing failed"
            }]