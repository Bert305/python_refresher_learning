



class Payment:
    def __init__(self, price):
        self.price = price + price * 0.10 # add 10% tax to price
    # half off sale during black friday    
    def half_price(self):
        return self.price / 2
    # point_of_sale method applies a 5% discount at point of sale
    def point_of_sale(self):
        return self.price * 0.95 # apply 5% discount at point of sale
        

book = Payment(10) # create an instance of the Payment class
video_game = Payment(70) # create an instance of the Payment class
black_friday = book.half_price() # create an instance of book and apply half_price method
points_back = video_game.point_of_sale() # create an instance of video_game and apply point_of_sale method
print(points_back) # print the price of the video game after applying point of sale.
print(book.price) # print the final price with tax
print(video_game.price) # print the final price with tax
print(black_friday) # print the price of the book during black friday sale
        