import json
from pathlib import Path

def test_json_types():
    json_file = Path(__file__).parents[2] / "inegi_playwright" / "relps_final.json"

    with open(json_file, encoding="utf-8") as f:
        content = f.read()

    # Find the end of the JSON array.
    end_idx = content.rfind("]")
    json_part = content[:end_idx + 1]

    data = json.loads(json_part)

    for record in data[:20]:
        assert isinstance(record["proveedor"], str)
        assert isinstance(record["numero"], list)