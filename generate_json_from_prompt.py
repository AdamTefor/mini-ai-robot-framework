import json
from pathlib import Path

# Lire le prompt
prompt_file = Path("prompts/test_prompt.txt")
prompt_text = prompt_file.read_text(encoding="utf-8")

# Dossier de sortie
output_dir = Path("input_data")
output_dir.mkdir(exist_ok=True)

# Logique IA simulée
# Pour l'instant, on transforme toujours le prompt en JSON standard
generated_json = {
    "test_name": "Test Login Valide Généré Par IA",
    "steps": [
        {
            "keyword": "Log To Console",
            "args": ["Début du test généré par IA"]
        },
        {
            "keyword": "Should Be Equal",
            "args": ["1", "1"]
        },
        {
            "keyword": "Log To Console",
            "args": ["Fin du test généré par IA"]
        }
    ]
}

# Sauvegarde JSON
output_file = output_dir / "test_case_generated_by_ai.json"
with output_file.open("w", encoding="utf-8") as f:
    json.dump(generated_json, f, indent=2, ensure_ascii=False)

print("Prompt lu avec succès :")
print(prompt_text)
print(f"JSON généré : {output_file}")