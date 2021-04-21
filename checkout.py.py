#initial SKU unit price
ipd_price = 549.99
mbp_price = 1399.99
atv_price = 109.5
vga_price = 30


class Checkout():

    def __init__(self):
        self.count_ipd = 0
        self.count_mbp = 0
        self.count_atv = 0
        self.count_vga = 0
        self.sku_list = []

    def scan(self, item):
        isValid = True

        if (item == 'ipd'):
            self.count_ipd += 1
        elif (item == 'mbp'):
            self.count_mbp += 1
        elif (item == 'atv'):
            self.count_atv += 1
        elif (item == 'vga'):
            self.count_vga += 1
        else:
            isValid = False
            print("invalid SKU: %s" % item)

        if isValid:
            self.sku_list.append(item)

    def total(self):

        # opening day special 1: have a 3 for 2 deal on Apple TVs,buy 2 get 1 free
        totaldiscount = self.count_atv // 3 * atv_price

        # opening day special 2: the price of super ipad have a discount that the price will drop to $499.99each
        if self.count_ipd > 4:
            totaldiscount = totaldiscount + self.count_ipd * (ipd_price - 499.99)

        # opening day special 3: get VGA free of charge with every Macbook pro
        if self.count_mbp >= self.count_vga:
            totaldiscount = totaldiscount + self.count_vga * vga_price
        else:
            totaldiscount = totaldiscount + self.count_mbp * vga_price

        # we calculate the total expect using the following formula:
        # total=originaltotal-special day dicount1-special day discount2-special day discount3
        originaltotal = self.count_ipd * ipd_price + self.count_mbp * mbp_price + self.count_atv * atv_price + self.count_vga * vga_price
        total = originaltotal - totaldiscount
        return print('SKU Scanned: %s \nTotal expected: $%.2f' % (', '.join(self.sku_list), total))

#testing case 1
co= Checkout()
co.scan('atv')
co.scan('atv')
co.scan('atv')
co.scan('vga')
co.total()

#testing case 2
co= Checkout()
co.scan('atv')
co.scan('ipd')
co.scan('ipd')
co.scan('atv')
co.scan('ipd')
co.scan('ipd')
co.scan('ipd')
co.total()

#testing case 3
co= Checkout()
co.scan('mbp')
co.scan('vga')
co.scan('ipd')
co.total()

#test case 4 invalid item
co= Checkout()
co.scan('mbp')
co.scan('vga')
co.scan('ipd')
co.scan('ipod')
co.scan('vga')
co.scan('ipd')
co.total()