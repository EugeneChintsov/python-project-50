import json
from typing import Dict, Any


def apply_json(diff_dictionary: Dict[str, Any]) -> str:
    return json.dumps(diff_dictionary, indent=4)