from llm.processor import summarize_text


def text_processing(text: str) -> str:
    return summarize_text(text)
