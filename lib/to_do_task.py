def to_do(text):
    if "#TODO" not in text:
        raise Exception("This does not have a TODO")
    else:
        return text