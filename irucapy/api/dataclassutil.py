from typing import Optional
import json


def from_json_maybe(json_text: str, dataclass_type: type) -> Optional[object]:
    """
    Convert a json string to a dataclass object.
    If the json string is invalid, return None.

    Parameters
    ----------
    json_text : str
        The json string to convert.
    dataclass_type : type
        The dataclass type to convert to.
    
    Returns
    -------
    obj : Optional[object]
        The converted dataclass object.
        If the json string is invalid, return None.
    """
    try:
        data = json.loads(json_text)
        obj = dataclass_type(**data)
        return obj
    except:
        return None
