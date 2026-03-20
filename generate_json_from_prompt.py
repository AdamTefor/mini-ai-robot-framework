import json
from pathlib import Path

# Lire le prompt
prompt_file = Path("prompts/test_prompt.txt")
prompt_text = prompt_file.read_text(encoding="utf-8").lower()

# Dossier de sortie
output_dir = Path("input_data")
output_dir.mkdir(exist_ok=True)

# Détection simple de l'intention
if "login" in prompt_text:
    generated_json = {
        "test_name": "Test Login Valide Généré Par IA",
        "steps": [
            {
                "keyword": "Log To Console",
                "args": ["Début du test login généré par IA"]
            },
            {
                "keyword": "Should Be Equal",
                "args": ["1", "1"]
            },
            {
                "keyword": "Log To Console",
                "args": ["Fin du test login généré par IA"]
            }
        ]
    }
    output_filename = "test_case_generated_login_by_ai.json"

elif "logout" in prompt_text:
    generated_json = {
        "test_name": "Test Logout Généré Par IA",
        "steps": [
            {
                "keyword": "Log To Console",
                "args": ["Début du test logout généré par IA"]
            },
            {
                "keyword": "Should Be Equal",
                "args": ["2", "2"]
            },
            {
                "keyword": "Log To Console",
                "args": ["Fin du test logout généré par IA"]
            }
        ]
    }
    output_filename = "test_case_generated_logout_by_ai.json"

elif "dashboard" in prompt_text:
    generated_json = {
        "test_name": "Test Dashboard Généré Par IA",
        "steps": [
            {
                "keyword": "Log To Console",
                "args": ["Début du test dashboard généré par IA"]
            },
            {
                "keyword": "Should Be Equal",
                "args": ["3", "3"]
            },
            {
                "keyword": "Log To Console",
                "args": ["Fin du test dashboard généré par IA"]
            }
        ]
    }
    output_filename = "test_case_generated_dashboard_by_ai.json"

else:
    generated_json = {
        "test_name": "Test Générique Généré Par IA",
        "steps": [
            {
                "keyword": "Log To Console",
                "args": ["Début du test générique généré par IA"]
            },
            {
                "keyword": "Should Be Equal",
                "args": ["4", "4"]
            },
            {
                "keyword": "Log To Console",
                "args": ["Fin du test générique généré par IA"]
            }
        ]
    }
    output_filename = "test_case_generated_generic_by_ai.json"

# Sauvegarde JSON
output_file = output_dir / output_filename
with output_file.open("w", encoding="utf-8") as f:
    json.dump(generated_json, f, indent=2, ensure_ascii=False)

print("Prompt lu avec succès :")
print(prompt_text)
print(f"JSON généré : {output_file}")