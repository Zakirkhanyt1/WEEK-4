class AuctionItem:
    def __init__(self, item_number, description, reserve_price):
        self.item_number = item_number
        self.description = description
        self.reserve_price = reserve_price
        self.num_bids = 0
        self.highest_bid = 0
        self.sold = False

    def place_bid(self, buyer_number, bid_amount):
        if bid_amount > self.highest_bid:
            self.highest_bid = bid_amount
            self.num_bids += 1
            print(f"Bid placed successfully! Current highest bid for Item #{self.item_number}: ${self.highest_bid}")
        else:
            print("Error: Bid must be higher than the current highest bid. Place a higher bid.")

    def mark_as_sold(self):
        if self.highest_bid >= self.reserve_price:
            self.sold = True


# Task 1 – Auction Set Up
def auction_setup():
    auction_items = []

    while len(auction_items) < 10:
        try:
            item_number = int(input(f"Enter item number for item #{len(auction_items) + 1}: "))
            description = input("Enter item description: ")
            reserve_price = float(input("Enter reserve price: "))

            if reserve_price <= 0:
                raise ValueError("Reserve price must be greater than zero.")

            item = AuctionItem(item_number, description, reserve_price)
            auction_items.append(item)

            print(f"Item #{len(auction_items)} added to the auction.\n")

        except ValueError as e:
            print(f"Error: {e}\nPlease enter valid input.\n")

    return auction_items


# Task 2 – Buyer Bids
def handle_buyer_bids(auction_items):
    while True:
        try:
            item_number = int(input("Enter the item number you want to bid on (0 to exit): "))
            if item_number == 0:
                break

            item = next((x for x in auction_items if x.item_number == item_number), None)
            if item:
                print(f"Item #{item.item_number} - {item.description}")
                print(f"Current highest bid: ${item.highest_bid}")
                buyer_number = int(input("Enter your buyer number: "))
                bid_amount = float(input("Enter your bid amount: "))

                item.place_bid(buyer_number, bid_amount)

            else:
                print("Error: Item not found. Please enter a valid item number.")

        except ValueError:
            print("Error: Please enter valid numerical values for item number, buyer number, and bid amount.")


# Task 3 – End of Auction
def end_of_auction(auction_items):
    total_fee = 0
    items_sold = 0
    items_not_meeting_reserve = 0
    items_with_no_bids = 0

    print("\nEnd of Auction Results:")

    for item in auction_items:
        if item.sold:
            item.mark_as_sold()
            items_sold += 1
            auction_fee = 0.1 * item.highest_bid
            total_fee += auction_fee
            print(f"Item #{item.item_number} - Sold for ${item.highest_bid}. Auction Fee: ${auction_fee}")
        else:
            if item.num_bids == 0:
                items_with_no_bids += 1
                print(f"Item #{item.item_number} - No bids received.")
            else:
                items_not_meeting_reserve += 1
                print(f"Item #{item.item_number} - Highest bid: ${item.highest_bid}. Did not meet reserve price.")

    print("\nSummary:")
    print(f"Total Auction Fee: ${total_fee}")
    print(f"Items Sold: {items_sold}")
    print(f"Items Not Meeting Reserve Price: {items_not_meeting_reserve}")
    print(f"Items with No Bids: {items_with_no_bids}")


# Main Program
auction_items_list = auction_setup()
handle_buyer_bids(auction_items_list)
end_of_auction(auction_items_list)
