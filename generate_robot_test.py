import json
from pathlib import Path

# Dossiers
input_dir = Path("input_data")
output_dir = Path("generated_tests")
output_dir.mkdir(exist_ok=True)

# Nettoyer les anciens fichiers Robot générés par IA
for old_file in output_dir.glob("test_case_generated_*.robot"):
    old_file.unlink()
    print(f"Ancien fichier Robot supprimé : {old_file}")

# Lire tous les fichiers JSON
json_files = list(input_dir.glob("*.json"))

if not json_files:
    print("Aucun fichier JSON trouvé dans input_data/")
    exit()

for json_file in json_files:
    with json_file.open("r", encoding="utf-8") as f:
        data = json.load(f)

    test_name = data["test_name"]
    steps = data["steps"]

    robot_lines = ["*** Test Cases ***", test_name]

    for step in steps:
        keyword = step["keyword"]
        args = "    ".join(step["args"])
        robot_lines.append(f"    {keyword}    {args}")

    robot_content = "\n".join(robot_lines)

    output_file = output_dir / f"{json_file.stem}.robot"
    output_file.write_text(robot_content, encoding="utf-8")

    print(f"Fichier - généré : {output_file}")

print("Génération terminée avec succès.")