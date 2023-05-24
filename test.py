from datetime import datetime, timedelta
from Parking import Parking_record, CoinPaymentMachine
import Parking



# 測試 Parking_record 類別
def test_parking_record():
    record = Parking_record()
    

    # 模擬停車 1 小時
    Parking.start_time = datetime(2023, 5, 22,9, 30, 0)
    Parking.end_time = datetime(2023, 5, 22,9, 30, 0) + timedelta(hours=1)  
    assert record.end_parking() == 30  

    # 模擬停車 3 小時
    Parking.start_time = datetime(2023, 5, 22,9, 30, 0)
    Parking.end_time = datetime(2023, 5, 22,9, 30, 0) + timedelta(hours=3)    
    assert record.end_parking() == 90

    # 模擬假日停車 3 小時
    Parking.start_time = datetime(2023, 5, 20,9, 30, 0)
    Parking.end_time = datetime(2023, 5, 20,9, 30, 0) + timedelta(hours=3)    
    assert record.end_parking() == 120

# 測試 CoinPaymentMachine 類別
def test_coin_payment_machine():
    record = Parking_record()
    machine = CoinPaymentMachine(record)

    # 測試插入不被接受的硬幣
    machine.insert_coin(1)
    assert machine.total_amount == 0  # 未接受的硬幣，總金額不應有變化

    # 測試插入被接受的硬幣
    machine.insert_coin(5)
    assert machine.total_amount == 5  # 插入 5 元硬幣

    # 測試取消支付
    machine.cancel_payment()
    assert machine.total_amount == 0  # 取消支付後，總金額歸零

    #模擬停車 2 小時，並插入足夠金額進行支付
    Parking.start_time = datetime(2023, 5, 22,9, 30, 0)
    Parking.end_time = datetime(2023, 5, 22,9, 30, 0) + timedelta(hours=2) 
    machine.insert_coin(50)  # 插入 50 元硬幣
    machine.insert_coin(10)  # 插入 10 元硬幣
    payment_result = machine.make_payment()
    assert payment_result == (60, 0)  # 停車費用為 60 元

    # 模擬停車 4 小時，但插入金額不足
    Parking.start_time = datetime(2023, 5, 22,9, 30, 0)
    Parking.end_time = datetime(2023, 5, 22,9, 30, 0) + timedelta(hours=4) 
    machine.insert_coin(10)  # 插入 10 元硬幣
    payment_result = machine.make_payment()
    assert payment_result == (None, None)  # 插入金額不足，支付失敗