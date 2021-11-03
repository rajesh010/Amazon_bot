from booking.sale_checker import Discount_manager

vaar = (str(input("In what mode you want to run: a for auto and m for manual \n")))
with Discount_manager() as bot:  
 if (vaar == 'a'):
     link_to_be_searched = "https://www.amazon.de/-/en/S3L46N/dp/B07ZZVWB4L/"
 else: link_to_be_searched = (str(input("Type the link to search the deal(amazon link) \n")))

bot.land_first_page(link_to_be_searched)
bot.implicitly_wait(15)
bot.agree_fn()
rand_var = (float(input("What is the price below which you want to get notified of? \n")))
bot.price_check(rand_var)

    