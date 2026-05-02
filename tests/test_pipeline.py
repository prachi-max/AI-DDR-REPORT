from modules.pdf_processor import extract_text_from_pdf
from modules.extractor import extract_observations
from modules.merger import merge_data
from modules.reasoning import generate_reasoning
from modules.report_generator import generate_report


def run_real_pipeline():
    # Step 1: Load real PDFs
    inspection_text = extract_text_from_pdf("data/input/inspection_report.pdf")
    thermal_text = extract_text_from_pdf("data/input/thermal_report.pdf")

    # Step 2: Extraction
    inspection_data = extract_observations(inspection_text, "Inspection Report")
    thermal_data = extract_observations(thermal_text, "Thermal Report")

    # Step 3: Merge
    merged_data = merge_data(inspection_data, thermal_data)

    # Step 4: Reasoning
    reasoning = generate_reasoning(merged_data)

    # Step 5: Final Report
    report_path = generate_report(reasoning)

    print("✅ DDR Generated:", report_path)


if __name__ == "__main__":
    run_real_pipeline()