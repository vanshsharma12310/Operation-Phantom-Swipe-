
import hashlib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

HASH_FILE = BASE_DIR / "password_protected" / "password_hash.txt"
REPORT_DIR = BASE_DIR / "report"

REPORT_DIR.mkdir(exist_ok=True)

# Read the target hash
text = HASH_FILE.read_text(encoding="utf-8")
target_hash = text.split("Password Hash:")[1].splitlines()[0].strip()

# Small educational dictionary
passwords = [
    "123456",
    "admin",
    "welcome",
    "password123",
    "password",
    "qwerty"
]

found = None
attempts = 0

for candidate in passwords:
    attempts += 1

    candidate_hash = hashlib.md5(
        candidate.encode()
    ).hexdigest()

    if candidate_hash == target_hash:
        found = candidate
        break

if found:
    result = (
        "DICTIONARY ATTACK SIMULATION\n"
        f"Password found: {found}\n"
        f"Attempts: {attempts}\n"
        "Result: Match found\n"
    )
else:
    result = (
        "DICTIONARY ATTACK SIMULATION\n"
        "Password not found in dictionary.\n"
        f"Attempts: {attempts}\n"
    )

output_file = REPORT_DIR / "password_cracking_results.txt"
output_file.write_text(result, encoding="utf-8")

print(result)
