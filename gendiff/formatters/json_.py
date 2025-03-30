import json
from typing import Any, Dict


def apply_json(data: Dict[str, Any]) -> str:
    return json.dumps(data, indent=4)