import config
from furtherpy.sample import date_conv_tool
from email_reader_repo.sample import email_tool
import get_news

# change send list to a Google sheet


def main():
    # Gets news
    headlines_list = get_news.get_headlines_and_link_cbs()
    # Formats email text
    headlines_printable = get_news.make_printable_headlines_and_link_cbs(headlines_list)
    subject = "News for " + date_conv_tool.get_readable("day")

    headlines_printable_ascii = headlines_printable.encode("ascii", errors="ignore")

    headlines_printable_decoded = str(headlines_printable_ascii.decode("ascii"))

    # Sends email
    email_tool.send_email(config.sender_email_address, config.sender_email_password,
                         config.rec_email_address, subject, headlines_printable_decoded)

    print("[send_news] Sent news update")


if __name__ == '__main__':
    main()
