

def annotate_text(text, named_entities):
    annotated_text = []
    end = 0
    for named_entity in named_entities:
        start = named_entity["start"]
        if text[end:start]:
            annotated_text.append(text[end:start])
        end = named_entity["end"]
        entity = named_entity["entity"]
        annotated_text.append((text[start:end], entity))
    return annotated_text

        
    # "This ",
    # ("is", "verb"),
    # " some ",
    # ("annotated", "adj"),
    # ("text", "noun"),
    # " for those of ",
    # ("you", "pronoun"),
    # " who ",
    # ("like", "verb"),
    # " this sort of ",
    # ("thing", "noun"),
    # "."
    