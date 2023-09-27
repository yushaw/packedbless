import Amazon.gifts_liner as gifts
import dataProcess.dataProcess as dp
import time

everyone = "https://www.amazon.com/gcx/Gifts-for-everyone/gfhz/events/"
everyone_path = './data/raw/amazon_everyone.xlsx'

forMan = "https://www.amazon.com/gcx/Gifts-for-Men/gfhz/category?categoryId=adult-male"
man_path = './data/raw/amazon_man.xlsx'

forWoman = "https://www.amazon.com/gcx/Gifts-for-Women/gfhz/category?categoryId=adult-female"
woman_path = './data/raw/amazon_woman.xlsx'

# gifts.get_gifts(everyone, everyone_path, 1000)
# gifts.get_gifts(forMan, man_path, 1000)
# gifts.get_gifts(forWoman, woman_path, 1000)
max_retries = 5
retry_delay = 3

for i in range(max_retries):
    try:
        dp.tagging(everyone_path)
        dp.translate(everyone_path)
        break
    except Exception as e:
        print(f"An error occurred: {e}. Retrying...")
        time.sleep(retry_delay)
else:
    print("Max retries reached. Exiting.")