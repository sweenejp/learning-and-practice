from isbnlib import meta, desc, cover, classify, goom
import datetime

# \\n\\n<<<\\n{description}\\n<<<\\n
SERVICE = 'openl'

isbn = input("Type in ISNB: ")

current_time = datetime.datetime.now()
fmt = '%Y%m%d%H%M'

def isbn_to_book_desc(isbn):
    book = meta(isbn)
    description = desc(isbn)
    image = f"[img[http://covers.openlibrary.org/b/isbn/{isbn}-L.jpg]]"

    title = book["Title"]
    author = book["Authors"]
    year_published = book["Year"]

    tiddler_title = f'"{title}"'
    created = f'"{current_time.strftime(fmt)}00000"'
    modified = f'"{current_time.strftime(fmt)}00001"'
    text = f'"{title} by {author}\\n\\nPublished: {year_published}\n\n{image}"'
    tags = f'"Watched/Listened/Read"'
    start = '[{'
    end = '}]'
    type = '"text/vnd.tiddlywiki"'

    print(text)
#     tw5_code = f'{start}"created":{created},"text":{text},"type":{type},"title":{tiddler_title},"tags":{tags},"modified":{modified}{end}'
#
#     print(tw5_code)
#     file = open(f"{title}.json,", "w")
#     file.write(tw5_code)
#     file.close()
#
#
# isbn_to_book_desc(isbn)
