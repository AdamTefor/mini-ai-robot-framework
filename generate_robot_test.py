import json
from pathlib import Path

# Fichier JSON source
input_file = Path("input_data/test_case_login.json")

# Dossier de sortie
output_dir = Path("generated_tests")
output_dir.mkdir(exist_ok=True)

# Fichier Robot généré
output_file = output_dir / "generated_from_json.robot"

# Lire le JSON
with input_file.open("r", encoding="utf-8") as f:
    data = json.load(f)

test_name = data["test_name"]
steps = data["steps"]

# Construire le contenu Robot
robot_lines = ["*** Test Cases ***", test_name]

for step in steps:
    keyword = step["keyword"]
    args = "    ".join(step["args"])
    robot_lines.append(f"    {keyword}    {args}")

robot_content = "\n".join(robot_lines)

# Écrire le fichier Robot
output_file.write_text(robot_content, encoding="utf-8")

print(f"Fichier Robot généré : {output_file}")