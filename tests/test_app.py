import pytest
from form_utils import detect_type, match_template

def test_detect_type():
    assert detect_type("27.05.2025") == "date"
    assert detect_type("2025-05-27") == "date"
    assert detect_type("+7 900 123 45 67") == "phone"
    assert detect_type("test@mail.com") == "email"
    assert detect_type("Some text") == "text"

def test_match_template_found(monkeypatch):
    monkeypatch.setattr("form_utils.db.all", lambda: [
        {
            "name": "Проба",
            "f_name1": "email",
            "f_name2": "date"
        }
    ])
    args = {"f_name1": "vasya@pukin.ru", "f_name2": "27.05.2025"}
    assert match_template(args) == "Проба"

def test_match_template_not_found(monkeypatch):
    monkeypatch.setattr("form_utils.db.all", lambda: [])
    args = {"a": "27.05.2025", "b": "+7 123 456 78 90"}
    assert match_template(args) == {"a": "date", "b": "phone"}
