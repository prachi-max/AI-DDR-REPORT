import os
from flask import Blueprint, render_template, request
from modules.pdf_processor import extract_text_from_pdf
from modules.extractor import extract_observations
from modules.merger import merge_data
from modules.reasoning import generate_reasoning
from modules.report_generator import generate_report
from flask import send_file

upload_bp = Blueprint("upload", __name__)

@upload_bp.route("/report")
def view_report():
    return send_file("data/output/reports/ddr_report.html")
@upload_bp.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@upload_bp.route("/upload", methods=["POST"])
def upload_files():
    inspection_file = request.files["inspection"]
    thermal_file = request.files["thermal"]

    # Save files
    inspection_path = os.path.join("data/input", inspection_file.filename)
    thermal_path = os.path.join("data/input", thermal_file.filename)

    inspection_file.save(inspection_path)
    thermal_file.save(thermal_path)

    # Pipeline
    inspection_text = extract_text_from_pdf(inspection_path)
    thermal_text = extract_text_from_pdf(thermal_path)

    inspection_data = extract_observations(inspection_text, "Inspection Report")
    thermal_data = extract_observations(thermal_text, "Thermal Report")

    merged = merge_data(inspection_data, thermal_data)
    reasoning = generate_reasoning(merged)

    report_path = generate_report(reasoning)

    print("🚀 Upload started")
    print("Step 1: Extracting text")
    print("Step 2: Extraction AI")
    print("Step 3: Merge")
    print("Step 4: Reasoning")
    print("Step 5: Report")

    return render_template("index.html", report_path=report_path)

