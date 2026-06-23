from pathlib import Path

def test_json_header_structure():

    json_file = (
        Path(__file__).parents[2]
        / "inegi_playwright"
        / "relps_final.json"
    )

    with open(json_file, encoding="utf-8") as f:
        first_20_lines = "".join([next(f) for _ in range(20)])

    assert '"proveedor"' in first_20_lines
    assert '"numero"' in first_20_lines