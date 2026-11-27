
import hashlib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

EVIDENCE_DIR = BASE_DIR / "artifacts"
HASH_DIR = BASE_DIR / "hashes"

HASH_DIR.mkdir(exist_ok=True)

results = []

for file_path in sorted(EVIDENCE_DIR.rglob("*")):
    if file_path.is_file() and file_path.name != "README.md":

        sha256 = hashlib.sha256()

        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                sha256.update(chunk)

        file_hash = sha256.hexdigest()

        results.append(f"{file_path.name} : {file_hash}")

        print(file_path.name, file_hash)

output_file = HASH_DIR / "SHA256SUMS.txt"
output_file.write_text("\n".join(results) + "\n")

print("Hash generation completed!")
