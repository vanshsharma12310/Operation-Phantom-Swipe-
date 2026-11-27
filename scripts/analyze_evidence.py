
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = BASE_DIR / "artifacts"
REPORT_DIR = BASE_DIR / "report"

REPORT_DIR.mkdir(exist_ok=True)

results = []

patterns = {
    "Email Addresses": r'[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}',
    "Card-like Numbers": r'\b(?:\d[ -]?){13,19}\b',
    "GPS Coordinates": r'Latitude:\s*-?\d+(?:\.\d+)?|Longitude:\s*-?\d+(?:\.\d+)?',
    "Suspicious Keywords": r'(?i)\b(?:delete|transfer|suspicious|fraud|transaction)\b'
}

for file_path in sorted(EVIDENCE_DIR.rglob("*")):
    if not file_path.is_file() or file_path.name == "README.md":
        continue

    content = file_path.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    results.append(f"\nFILE: {file_path.name}")

    for category, pattern in patterns.items():
        matches = re.findall(pattern, content)

        if matches:
            results.append(f"\n{category}:")
            for match in matches:
                results.append(f"- {match}")

output = "\n".join(results)

output_file = REPORT_DIR / "analysis_results.txt"
output_file.write_text(output, encoding="utf-8")

print(output)
print("\nForensic analysis completed!")
