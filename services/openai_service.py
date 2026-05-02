# import json

# USE_MOCK = True


# def call_gpt(prompt, user_input):
#     if USE_MOCK:
#         return mock_response(prompt, user_input)

#     return "API not enabled"


# def mock_response(prompt, user_input):
#     prompt_lower = prompt.lower()

#     # 🔹 EXTRACTION
#     if "extract structured observations" in prompt_lower:
#         return json.dumps([
#             {
#                 "area": "bedroom wall",
#                 "issue": "dampness",
#                 "details": "Not Available"
#             },
#             {
#                 "area": "ceiling",
#                 "issue": "cracks",
#                 "details": "Not Available"
#             }
#         ])

#     # 🔹 MERGE
#     elif "combining building inspection data" in prompt_lower:
#         return json.dumps([
#             {
#                 "area": "bedroom wall",
#                 "combined_issue": "dampness",
#                 "supporting_data": "Not Available",
#                 "conflict": "No",
#                 "conflict_details": ""
#             },
#             {
#                 "area": "ceiling",
#                 "combined_issue": "cracks",
#                 "supporting_data": "Not Available",
#                 "conflict": "No",
#                 "conflict_details": ""
#             }
#         ])

#     # 🔹 REASONING
#     elif "building diagnostics expert" in prompt_lower:
#         return json.dumps([
#             {
#                 "area": "bedroom wall",
#                 "issue": "dampness",
#                 "root_cause": "Possible water leakage",
#                 "severity": "High",
#                 "severity_reason": "Moisture can damage structure",
#                 "recommended_action": "Apply waterproofing"
#             },
#             {
#                 "area": "ceiling",
#                 "issue": "cracks",
#                 "root_cause": "Surface stress",
#                 "severity": "Medium",
#                 "severity_reason": "Visible damage but not critical",
#                 "recommended_action": "Seal cracks and monitor"
#             }
#         ])

#     # 🔹 FINAL REPORT
#     elif "detailed diagnostic report" in prompt_lower:
#         return """1. Property Issue Summary  
# Wall dampness and ceiling cracks observed.

# 2. Area-wise Observations  
# Bedroom wall: Dampness present.  
# Ceiling: Cracks observed.  

# 3. Probable Root Cause  
# Wall: Water leakage.  
# Ceiling: Structural stress.  

# 4. Severity Assessment  
# Wall: High (moisture risk)  
# Ceiling: Medium (visible damage)  

# 5. Recommended Actions  
# Apply waterproofing.  
# Seal ceiling cracks.  

# 6. Additional Notes  
# Image: Not Available  

# 7. Missing or Unclear Information  
# Not Available"""

#     return "[]"
import requests

def call_gpt(prompt, user_input):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt + "\n" + user_input,
                "stream": False
            }
        )

        return response.json()["response"]

    except Exception as e:
        return f"Error: {str(e)}"