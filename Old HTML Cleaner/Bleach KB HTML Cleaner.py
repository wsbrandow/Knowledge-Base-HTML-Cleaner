while True:
    import re

    original = input("")
    TAG_RE = re.compile(r'<p[^>]+>')

    def remove_tags(text):
        return TAG_RE.sub('<p>', text)

    print(remove_tags(original))
