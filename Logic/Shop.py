class Shop:
    offers = [
        {
            'ID': 4,
            'OfferTitle': 'ОСОБАЯ АКЦИЯ',
            'Cost': 10,
            'OldCost': 0,
            'OfferView': 0,
            'Multiplier': 1,
            'SkinID': 52,
            'BrawlerID': 0,
            'ShopType': 0,
            'ShopDisplay': 0,
            'Timer': 0,
            'Purchased': False
        }

    ]

    gold = [
        {
            'Cost': 20,
            'Amount': 150
        },

        {
            'Cost': 50,
            'Amount': 400
        },

        {
            'Cost': 140,
            'Amount': 1200
        },

        {
            'Cost': 280,
            'Amount': 2600
        }

    ]
    
    tickets = [
        {
            'Cost': 10,
            'Amount': 6
        },

        {
            'Cost': 30,
            'Amount': 20
        },

        {
            'Cost': 80,
            'Amount': 60
        }

    ]

    boxes = [
        {
            'Name': 'Big Box',
            'Cost': 30,
            'Multiplier': 1
        },

        {
            'Name': 'Mega Box',
            'Cost': 80,
            'Multiplier': 1
        }

    ]


    token_doubler = {

        'Cost': 50,
        'Amount': 1000
    }

    def EncodeShopOffers(self):
        count = len(Shop.offers)
        self.writeVint(count)
        for i in range(count):
            item = Shop.offers[i]
            self.writeVint(1)
            self.writeVint(item['ID']) # ItemID
            self.writeVint(item['Multiplier']) # Ammount
            self.writeScId(16, item['BrawlerID'])
            self.writeVint(item['SkinID']) # ItemID

            self.writeVint(item['ShopType'])  # [0 = Offer, 2 = Skins 3 = Star Shop]

            self.writeVint(item['Cost'])  # Cost
            self.writeVint(item['Timer']) # Timer

            self.writeVint(item['OfferView']) # Offer View | 0 = Absolutely "NEW", 1 = "NEW", 2 = Viewed
            self.writeVint(100)
            self.writeBoolean(item['Purchased'])  # is Offer Purchased

            self.writeBoolean(False)
            self.writeVint(item['ShopDisplay'])  # [0 = Normal, 1 = Daily Deals]
            #self.writeBoolean(False)
            self.writeVint(item['OldCost'])  # Cost
            self.writeVint(0)

            self.writeInt(0)
            self.write_string_reference(item['OfferTitle']) # Offers name

            self.writeBoolean(False)
