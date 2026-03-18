from pathlib import Path

print("Début du script...")

output_dir = Path("generated_tests")
output_dir.mkdir(exist_ok=True)

output_file = output_dir / "generated_login_test.robot"

robot_content = """*** Test Cases ***
Test Généré Automatiquement
    Log To Console    Test généré automatiquement depuis Python
    Should Be Equal    2    2
"""

output_file.write_text(robot_content, encoding="utf-8")

print(f"Fichier généré avec succès : {output_file.resolve()}")
print(f"Le fichier existe ? {output_file.exists()}")