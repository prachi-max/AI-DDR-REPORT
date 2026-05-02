import json
from services.openai_service import call_gpt


def load_prompt():
    with open("prompts/reasoning_prompt.txt", "r", encoding="utf-8") as f:
        return f.read()


def generate_reasoning(merged_data):
    prompt_template = load_prompt()

    # Convert Python → string for GPT
    merged_str = json.dumps(merged_data, indent=2)

    # Inject data into prompt
    prompt = prompt_template.replace("{merged_data}", merged_str)

    try:
        response = call_gpt(prompt, "Generate root cause, severity, and actions.")

        # Parse JSON response
        result = json.loads(response)
        return result

    except json.JSONDecodeError:
        print("⚠️ JSON parsing failed in reasoning. Retrying...")

        # Retry once with stricter instruction
        response = call_gpt(prompt, "Return ONLY valid JSON. No explanation.")

        try:
            result = json.loads(response)
            return result
        except:
            return [{
                "area": "Not Available",
                "issue": "Reasoning Error",
                "root_cause": "Not Available",
                "severity": "Not Available",
                "severity_reason": "Parsing failed",
                "recommended_action": "Not Available"
            }]