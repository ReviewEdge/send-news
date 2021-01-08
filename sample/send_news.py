import config
from furtherpy.sample import date_conv_tool
from email_reader_repo.sample import email_tool
import get_news
from spotify_controller_repo.sample import gsheets_tool

# change send list to a Google sheet


def get_email_list():
    service = gsheets_tool.authenticate_sheets_api()
    current_sheet_id = config.news_email_rec_sheets_id

    raw_email_list = gsheets_tool.get_all_sheets_data(service, current_sheet_id, "A:A")

    email_list = [val for sublist in raw_email_list for val in sublist]

    return email_list




def main():
    # Gets news
    headlines_list = get_news.get_headlines_and_link_cbs()
    # Formats email text
    headlines_printable = get_news.make_printable_headlines_and_link_cbs(headlines_list)
    subject = "News for " + date_conv_tool.get_readable("day")

    headlines_printable_ascii = headlines_printable.encode("ascii", errors="ignore")

    headlines_printable_decoded = str(headlines_printable_ascii.decode("ascii"))

    # Gets the wiki-a-day email list
    mailing_list = get_email_list()

    # Sends email to every address on list
    for rec_address in mailing_list:
        email_tool.send_email(config.sender_email_address, config.sender_email_password, rec_address,
                              subject, headlines_printable_decoded)

    print("[send_news] Sent news update")


if __name__ == '__main__':
    main()
