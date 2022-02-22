from flask import Flask, request
from books import Books


APP = Flask(__name__)


def main():
    APP.run(host='127.0.0.1', port=8081, threaded=True)


@APP.route('/getbookdetails', methods=['GET'])
def find_books() -> None:
    gutenberg_id = request.args.get('book_id').split(',') if \
        request.args.get('book_id') is not None else None
    languages = request.args.get('languages').split(
        ',') if request.args.get(
        'languages') is not None else None
    mime_types = request.args.get('mime_types').split(
        ',') if request.args.get(
        'mime_types') is not None else None
    topics = request.args.get('topics').split(',') if request.args.get(
        'topics') is not None else None
    authors = request.args.get('authors').split(',') if request.args.get(
        'authors') is not None else None
    titles = request.args.get('titles').split(',') if request.args.get(
        'titles') is not None else None
    page_no = int(request.args.get('page_no')) if request.args.get(
        'page_no') is not None else 1
    book_obj = Books(gutenberg_id, languages, mime_types, topics, authors,
                     titles, page_no)
    return book_obj.get_books_data()


if __name__ == '__main__':
    main()




