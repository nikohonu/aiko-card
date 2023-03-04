import json
import tempfile
import urllib.request
from pathlib import Path


def request(action, **params):
    return {"action": action, "params": params, "version": 6}


def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode("utf-8")
    response = json.load(
        urllib.request.urlopen(
            urllib.request.Request("http://localhost:8765", requestJson)
        )
    )
    if len(response) != 2:
        raise Exception("response has an unexpected number of fields")
    if "error" not in response:
        raise Exception("response is missing required error field")
    if "result" not in response:
        raise Exception("response is missing required result field")
    if response["error"] is not None:
        raise Exception(response["error"])
    return response["result"]


def add_card(
    deck_name,
    model_name,
    sentence_field,
    translation_field,
    picture_field,
    sentence,
    translation,
    picture,
):
    with tempfile.NamedTemporaryFile(suffix=".webp", delete=False) as tmp:
        picture_path = Path(tmp.name)
        picture_name = picture_path.stem
        picture.save(picture_path, "WebP", quality=20)
        invoke(
            "guiAddCards",
            note={
                "deckName": deck_name,
                "modelName": model_name,
                "fields": {sentence_field: sentence, translation_field: translation},
                "picture": [
                    {
                        "path": str(picture_path),
                        "filename": picture_name,
                        "fields": [picture_field],
                    }
                ],
            },
        )
