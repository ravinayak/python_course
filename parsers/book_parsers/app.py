from parsers.book_parsers.pages.pages import Pages


def run():
    books = Pages.fetch_books()
    for book in books:
        print(book)

run()