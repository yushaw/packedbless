import crawler

everyone = "https://www.amazon.com/gcx/Gifts-for-everyone/gfhz/events/"
everyone_path = './data/raw/amazon_everyone.xlsx'

forMan = "https://www.amazon.com/gcx/Gifts-for-Men/gfhz/category?categoryId=adult-male"
man_path = './data/raw/amazon_man.xlsx'

forWoman = "https://www.amazon.com/gcx/Gifts-for-Women/gfhz/category?categoryId=adult-female"
woman_path = './data/raw/amazon_woman.xlsx'

crawler.crawl_forAmazon_withoutTagging(forWoman, woman_path, 1000)