import json
from pathlib import Path

# Dossiers
input_dir = Path("input_data")
output_dir = Path("generated_tests")
output_dir.mkdir(exist_ok=True)

# Supprimer les anciens fichiers Robot
for old_file in output_dir.glob("*.robot"):
    old_file.unlink()
    print(f"Ancien fichier Robot supprimé : {old_file}")

# Nom du fichier Robot final combiné
output_file = output_dir / "generated_suite.robot"

# Lire tous les fichiers JSON
json_files = list(input_dir.glob("*.json"))

if not json_files:
    print("Aucun fichier JSON trouvé dans input_data/")
    exit()

robot_lines = ["*** Test Cases ***"]

for json_file in json_files:
    with json_file.open("r", encoding="utf-8") as f:
        data = json.load(f)

    test_name = data["test_name"]
    steps = data["steps"]

    robot_lines.append(test_name)

    for step in steps:
        keyword = step["keyword"]
        args = "    ".join(step["args"])
        robot_lines.append(f"    {keyword}    {args}")

    robot_lines.append("")

robot_content = "\n".join(robot_lines)

# Écrire le fichier unique
output_file.write_text(robot_content, encoding="utf-8")

print(f"Fichier Robot combiné généré : {output_file}")