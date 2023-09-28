import crawler

everyone = "https://www.amazon.com/gcx/Gifts-for-everyone/gfhz/events/"
everyone_path = './data/raw/amazon_everyone.xlsx'

forMan = "https://www.amazon.com/gcx/Gifts-for-Men/gfhz/category?categoryId=adult-male"
man_path = './data/raw/amazon_man.xlsx'

forWoman = "https://www.amazon.com/gcx/Gifts-for-Women/gfhz/category?categoryId=adult-female"
woman_path = './data/raw/amazon_woman.xlsx'

handmade = "https://www.amazon.com/gcx/Gift-shop/gfhz/events/?_encoding=UTF8&categoryId=handmade-EGgiftshop"
handmade_path = './data/raw/amazon_handmade.xlsx'

crawler.crawl_forAmazon_withoutTagging(handmade, handmade_path, 1000, 5)