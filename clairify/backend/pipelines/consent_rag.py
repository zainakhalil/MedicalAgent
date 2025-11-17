import os

def explain_consent(consent_id: str, language="English"):
    path = f"../backend/data/consents/colonoscopy_en.txt"
    with open(path, "r") as f:
        original = f.read()

    return {
        "consent_id": consent_id,
        "language": language,
        "sections": [
            {"title": "What is this?", "text": "A colonoscopy is a camera test to check inside your colon."},
            {"title": "Risks", "text": "Bleeding, infection, perforation, sedation reaction."},
            {"title": "Benefits", "text": "Detect cancer early, remove polyps, find causes of bleeding."},
            {"title": "Alternatives", "text": "Stool tests, scans, or waiting."}
        ],
        "original_text": original
    }

def explain_term(term: str, language="English"):
    lookup = {
        "colonoscopy": "A test where a camera is used to look inside your colon.",
        "hypokalemia": "Low potassium level in the blood.",
        "MRI": "Magnetic scan that takes detailed images."
    }
    base = lookup.get(term.lower(), f"{term}: ask your doctor for details.")
    return {"english": base, "translated": f"[{language}] {base}"}
