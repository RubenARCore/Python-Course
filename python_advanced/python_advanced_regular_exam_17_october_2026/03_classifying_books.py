def classify_books (*args, **kwargs):
    fiction = []
    non_fiction = []
    fiction_books = []
    non_fiction_books = []
    result = []

    for genre, title in args:
        if genre == "fiction":
            fiction.append(title)
        else:
            non_fiction.append(title)

    for isbn, title in kwargs.items():
        if title in fiction:
            fiction_books.append(f"{isbn}#{title}")
        else:
            non_fiction_books.append(f"{isbn}#{title}")

    fiction_books.sort()
    non_fiction_books.sort(reverse=True)

    if fiction_books:
        result.append("Fiction Books:")
        for book in fiction_books:
            result.append(f"~~~{book}")

    if non_fiction_books:
        result.append("Non-Fiction Books:")
        for book in non_fiction_books:
            result.append(f"***{book}")


    return "\n".join(result)


print(classify_books(
    ("non_fiction", "The Art of War"),
    ("fiction", "The Great Gatsby"),
    ("non_fiction", "A Brief History of Time"),
    ("fiction", "Brave New World"),
    FF1234HH="The Great Gatsby",
    NF3845UU="A Brief History of Time",
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))