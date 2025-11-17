# backend/consent_rag.py

def explain_consent(consent_id: str, target_language: str = "English"):
    """
    TEMP STUB for Role 3.
    Teammate will replace this with Pathway + LLM implementation.
    """
    return {
        "sections": [
            {
                "title": f"About the procedure ({target_language})",
                "text": "This is a simple explanation of the procedure in your language.",
            },
            {
                "title": "Risks",
                "text": "There is a small risk of bleeding or infection.",
            },
        ],
        "quiz": [
            {
                "question": "What is one possible risk?",
                "options": ["Bleeding", "Free ice cream", "New superpowers"],
                "correct_index": 0,
            }
        ],
    }


def explain_term(term: str, target_language: str = "English"):
    """
    TEMP STUB for Role 3.
    Teammate will replace this with LLM JSON output.
    """
    return {
        "english": f'{term}: a simple explanation in English for patients.',
        "translated": f'{term}: translated explanation in {target_language}.',
    }
