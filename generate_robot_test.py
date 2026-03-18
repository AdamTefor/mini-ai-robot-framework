from pathlib import Path

# Dossier de sortie
output_dir = Path("generated_tests")
output_dir.mkdir(exist_ok=True)

# Nom du fichier généré
output_file = output_dir / "generated_login_test.robot"

# Contenu Robot généré automatiquement
robot_content = """*** Test Cases ***
Test Généré Automatiquement
    Log To Console    Test généré automatiquement depuis Python
    Should Be Equal    2    2
"""

# Écriture du fichier
output_file.write_text(robot_content, encoding="utf-8")

print(f"Fichier généré avec succès : {output_file}")