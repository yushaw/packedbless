import Amazon.gifts as gifts

everyone = "https://www.amazon.com/gcx/Gifts-for-everyone/gfhz/events/"
everyone_path = './data/amazon_everyone.xlsx'

forMan = "https://www.amazon.com/gcx/Gifts-for-Men/gfhz/category?categoryId=adult-male"
man_path = './data/amazon_man.xlsx'

forWoman = "https://www.amazon.com/gcx/Gifts-for-Women/gfhz/category?categoryId=adult-female"
woman_path = './data/amazon_woman.xlsx'

gifts.get_gifts(everyone, everyone_path, 50)
gifts.get_gifts(forMan, man_path, 50)
gifts.get_gifts(forWoman, woman_path, 50)
