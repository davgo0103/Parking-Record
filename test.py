import pytest
from datetime import datetime, timedelta
from Parking import Parking_record, CoinPaymentMachine

# 測試 Parking_record 類別
def test_parking_record():
    record = Parking_record()
    record.start_parking()

    # 模擬停車 1 小時
    end_time = datetime.now() + timedelta(hours=1)
    record.start_time = end_time - timedelta(minutes=60)
    assert record.end_parking() == 30  # 平日停車費率為 15，1小時應該是 30 元

    # 模擬週末停車 3 小時
    end_time = datetime.now() + timedelta(hours=3)
    record.start_time = end_time - timedelta(minutes=180)
    assert record.end_parking() == 60  # 週末停車費率為 20，3小時應該是 60 元

# 測試 CoinPaymentMachine 類別
def test_coin_payment_machine():
    record = Parking_record()
    machine = CoinPaymentMachine(record)

    # 測試插入不被接受的硬幣
    machine.insert_coin(1)
    assert machine.total_amount == 0  # 未接受的硬幣，總金額不應有變化

    # 測試插入被接受的硬幣
    machine.insert_coin(5)
    assert machine.total_amount == 5  # 插入 5 元硬幣，總金額應該是 5

    # 測試取消支付
    machine.cancel_payment()
    assert machine.total_amount == 0  # 取消支付後，總金額應該歸零

    # 模擬停車 2 小時，並插入足夠金額進行支付
    record.start_parking()
    end_time = datetime.now() + timedelta(hours=2)
    record.start_time = end_time - timedelta(minutes=120)
    machine.insert_coin(50)  # 插入 50 元硬幣
    payment_result = machine.make_payment()
    assert payment_result == (60, 10)  # 停車費用為 60 元，找零 10 元

    # 模擬停車 4 小時，但插入金額不足進行支付
    record.start_parking()
    end_time = datetime.now() + timedelta(hours=4)
    record.start_time = end_time - timedelta(minutes=240)
    machine.insert_coin(10)  # 插入 10 元硬幣
    payment_result = machine.make_payment()
    assert payment_result == (None, None)  # 插入金額不足，支付失敗