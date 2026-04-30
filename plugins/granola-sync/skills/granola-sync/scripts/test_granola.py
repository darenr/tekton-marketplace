import pytest
from granola import format_duration, format_transcript

def test_format_duration_valid():
    segments = [
        {"start_timestamp": "2023-10-27T10:00:00Z", "end_timestamp": "2023-10-27T10:01:00Z"},
        {"start_timestamp": "2023-10-27T10:01:00Z", "end_timestamp": "2023-10-27T10:05:00Z"}
    ]
    assert format_duration(segments) == 5

def test_format_duration_empty():
    assert format_duration([]) == 0

def test_format_duration_invalid_iso():
    segments = [
        {"start_timestamp": "invalid", "end_timestamp": "2023-10-27T10:05:00Z"}
    ]
    assert format_duration(segments) == 0

def test_format_duration_missing_keys():
    segments = [
        {"start_timestamp": "2023-10-27T10:00:00Z"},
        {"not_end": "2023-10-27T10:05:00Z"}
    ]
    assert format_duration(segments) == 0

def test_format_duration_none_values():
    segments = [
        {"start_timestamp": None, "end_timestamp": "2023-10-27T10:05:00Z"}
    ]
    assert format_duration(segments) == 0

def test_format_duration_type_error():
    segments = [
        {"start_timestamp": 12345, "end_timestamp": "2023-10-27T10:05:00Z"}
    ]
    assert format_duration(segments) == 0

def test_format_transcript_invalid_timestamp():
    segments = [
        {"text": "Hello", "source": "microphone", "start_timestamp": None},
        {"text": "World", "source": "system", "start_timestamp": "invalid"}
    ]
    result = format_transcript(segments, show_timestamps=True)
    assert "??:??:??" in result
