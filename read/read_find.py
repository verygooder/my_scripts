from read import *
from colorama import init, Fore
from sys import argv


def get_search_soup(key_word):
    '''input search key word, return search page soup'''
    url_root = "http://readfree.me/search/?q="
    url = url_root + key_word
    soup = get_soup(url)
    return soup


def show_books(soup):
    '''execute soup, extract books info, and show them'''
    books_soup = extract_books(soup)
    books = [Book(i) for i in books_soup]
    books = sorted(books, key=lambda x: float(x.score), reverse=False)
    init(autoreset=True)
    style = Fore.GREEN
    for book in books:
        book.score = str(book.score)
        print(book.score, style + book.name, book.author, book.link)


def run():
    key_word = argv[1]
    soup = get_search_soup(key_word)
    show_books(soup)


if __name__ == '__main__':
    run()
