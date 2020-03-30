import requests
from bs4 import BeautifulSoup


def get_headlines_and_link_cbs():
    page = requests.get("https://www.cbsnews.com")
    soup = BeautifulSoup(page.content, 'html.parser')

    latest_news_section = soup.find("section", {"id": "component-latest-news"})

    news_pieces = latest_news_section.findAll("article", {"class": "item"})

    news_pieces_data = []
    counter = 0
    for i in news_pieces:
        piece = news_pieces[counter]

        piece_title = piece.find("h4").text.strip()
        piece_link = piece.find("a", {"class": "item__anchor"})["href"]

        news_pieces_data.append([piece_title, piece_link])

        counter += 1

    return news_pieces_data


def make_printable_headlines_and_link_cbs(news_data):
    printable_headlines_and_link = ""
    for news_piece in news_data:
        printable_headlines_and_link += news_piece[0] + "\n" + news_piece[1] + "\n\n"

    return printable_headlines_and_link


# Lays out the code flow, runs sample if called directly
def main():
    headlines_list = get_headlines_and_link_cbs()
    headlines_printable = make_printable_headlines_and_link_cbs(headlines_list)

    print(headlines_list)
    print(headlines_printable)


# runs main (sample) if called directly
if __name__ == '__main__':
    main()


