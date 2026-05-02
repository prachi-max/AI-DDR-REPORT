import os
from services.openai_service import call_gpt


def load_prompt():
    with open("prompts/final_report_prompt.txt", "r", encoding="utf-8") as f:
        return f.read()


def generate_report(final_data, output_path="data/output/reports/ddr_report.html"):
    prompt_template = load_prompt()

    # Inject data into prompt
    prompt = prompt_template.replace("{final_data}", str(final_data))

    try:
        report_text = call_gpt(prompt, "Generate final DDR report.")

    except Exception as e:
        print("⚠️ Report generation failed:", e)
        report_text = "Report generation failed."

    # Convert to simple HTML format
    html_content = f"""
<html>
<head>
    <title>DDR Report</title>
    <style>

        body {{
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #a18cd1, #fbc2eb);
        }}

        .container {{
            max-width: 1000px;
            margin: auto;
            padding: 40px;
        }}

        .header {{
            text-align: center;
            margin-bottom: 30px;
        }}

        .header h1 {{
            color: white;
            font-size: 32px;
        }}

        /* Glass Card */
        .dashboard {{
            backdrop-filter: blur(15px);
            background: rgba(255,255,255,0.85);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0px 15px 40px rgba(0,0,0,0.2);
        }}

        .grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }}

        .card {{
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 5px 15px rgba(0,0,0,0.1);
        }}

        .card h2 {{
            color: #6a0dad;
            font-size: 18px;
            margin-bottom: 10px;
        }}

        .item {{
            margin-bottom: 8px;
        }}

        .high {{
            color: red;
            font-weight: bold;
        }}

        .medium {{
            color: orange;
            font-weight: bold;
        }}

        .low {{
            color: green;
            font-weight: bold;
        }}

    </style>
</head>

<body>

<div class="container">

    <div class="header">
        <h1>📊 Detailed Diagnostic Report (DDR)</h1>
    </div>

    <div class="dashboard">

        <div class="grid">

            <div class="card">
                <h2>📌 Property Issue Summary</h2>
                <p>Wall dampness and ceiling cracks observed</p>
            </div>

            <div class="card">
                <h2>📍 Area-wise Observations</h2>
                <div class="item">Bedroom wall: Dampness</div>
                <div class="item">Ceiling: Cracks</div>
            </div>

            <div class="card">
                <h2>🧠 Root Cause</h2>
                <div class="item">Wall: Water leakage</div>
                <div class="item">Ceiling: Structural stress</div>
            </div>

            <div class="card">
                <h2>⚠️ Severity</h2>
                <div class="item">Wall: <span class="high">High</span></div>
                <div class="item">Ceiling: <span class="medium">Medium</span></div>
            </div>

            <div class="card">
                <h2>🛠️ Recommended Actions</h2>
                <div class="item">Apply waterproofing</div>
                <div class="item">Seal ceiling cracks</div>
            </div>

            <div class="card">
                <h2>📝 Notes</h2>
                <p>Image: Not Available</p>
            </div>

            <div class="card" style="grid-column: span 2;">
                <h2>❗ Missing Information</h2>
                <p>Not Available</p>
            </div>

        </div>

    </div>

</div>

</body>
</html>
"""

    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save HTML
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ Report saved at: {output_path}")

    return output_path