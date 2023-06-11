class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        #Wanted to check all within one if but realized now it'll be better if check one at a time first to tell the
        #customer what the error is.
        #if flavor in self.flavors and scoops <= 1 and scoops <= 3:

        if flavor not in self.flavors:
            print("We don't have the flavor, sorry.")
            return None

        if scoops < 1 or scoops > 3:
            print("Please choose a number between 1-3 scoops: \n")
            return None

        print("Order created!")
        order = {"Customer": customer, "Flavor": flavor, "Scoops": scoops}

        self.orders.enqueue(order)

    def show_all_orders(self):
        print("All Pending Ice Cream Orders:")
        # print statement below was grabbed using chatGBT I couln't think of my own way to print the whole keys and values
        # together so I did research and found this.
        for order in self.orders.items:
                print(' '.join([f"{key}: {value}" for key, value in order.items()]))
        print()

    def next_order(self):
        print("Next Order Up!")
        order = self.orders.dequeue()
        #print statement below was grabbed using chatGBT I couln't think of my own way to print the whole keys and values
        #together so I did research and found this.
        print(' '.join([f"{key}: {value}" for key, value in order.items()]))
        print()


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()




