import datetime
end_time =  None
start_time = None
class Parking_record:
    def __init__(self):
        self.weekday = 15               # 平日停車費率(30m)
        self.weekend = 20               # 週末停車費率(30m)
        self.weekday_max = 300          # 平日最高收費
        self.weekend_max = 420          # 週末最高收費
        

    def start_parking(self):
        start_time = datetime.datetime.now()
        

    def end_parking(self):
        
        parking_duration = end_time - start_time
        parking_minutes = round(parking_duration.total_seconds() / 60)

        if end_time.weekday() < 5:       # 平日
            parking_rate = self.weekday
            max_charge = self.weekday_max
        else:                            # 週末
            parking_rate = self.weekend
            max_charge = self.weekend_max

        parking_fee = min(parking_minutes // 30, max_charge) * parking_rate

        return parking_fee

class CoinPaymentMachine:
    def __init__(self, parking_lot):
        self.parking_lot = parking_lot
        self.accepted_coins = [5, 10, 50]
        self.total_amount = 0

    def insert_coin(self, coin):
        if coin in self.accepted_coins:
            self.total_amount += coin

    def cancel_payment(self):
        self.total_amount = 0

    def make_payment(self):
        parking_fee = parking.end_parking()
        if self.total_amount >= parking_fee:
            change = self.total_amount - parking_fee
            self.total_amount = 0
            return parking_fee, change
        else:
            return None,None


parking = Parking_record()
payment_machine = CoinPaymentMachine(parking)



