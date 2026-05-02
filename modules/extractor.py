import json
from services.openai_service import call_gpt

# Load prompt from file
def load_prompt():
    with open("prompts/extraction_prompt.txt", "r", encoding="utf-8") as f:
        return f.read()


def extract_observations(text, document_type="Inspection Report"):

    # 🔥 IMPORTANT: Limit text size here
    text = text[:1500]

    prompt_template = load_prompt()

    # Replace placeholders
    prompt = prompt_template.replace("{document_type}", document_type)
    prompt = prompt.replace("{input_text}", text)

    try:
        response = call_gpt(prompt, "Extract structured observations.")

        # Convert to JSON
        data = json.loads(response)

        return data

    except json.JSONDecodeError:
        print("⚠️ JSON parsing failed. Retrying once...")

        # Retry once
        response = call_gpt(prompt, "Return ONLY valid JSON.")
        
        try:
            data = json.loads(response)
            return data
        except:
            return [{
                "area": "Not Available",
                "issue": "Parsing Error",
                "details": "Not Available"
            }]