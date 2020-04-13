import send_news
from furtherpy.sample import files_tool
import time


print("\n[forever_send_news] Starting send_news.py")
while 1:
    try:
        send_news.main()

    except Exception as e:
        # saves error file
        files_tool.basic_write_file("send_news_crash_report", "send_news crashed with the exception: " + str(e))

        print("\n[forever_send_news] The error: '" + str(e) +
              "' occurred while running send_news.py.\nTrying again...\n")

        # waits to restart loop
        time.sleep(60)

    # Waits set amount of hours to send news update
    hours_wait = 3
    time.sleep(3600 * hours_wait)
