MIRROR_PROMPT = """Explain what parts of meaning were lost due to compression,
summarization, or omission in the text below. Be specific.

Text:
{input}
"""

HALLUCINATION_PROMPT = """Assess whether the claim below is likely hallucinated.
Return two parts: reasoning and risk (low/medium/high).

Claim:
{input}
"""