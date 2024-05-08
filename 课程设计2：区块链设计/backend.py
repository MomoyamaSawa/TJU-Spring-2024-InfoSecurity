import random
import uuid
import time
from datetime import datetime, timedelta
from web3 import Web3, HTTPProvider
from data import get_data, Peoples

# 连接到Ganache
w3 = Web3(HTTPProvider("http://127.0.0.1:7545"))

# 确保我们已经连接到以太坊节点
assert w3.is_connected()

# 从文件中读取ABI
with open("Traceability.abi", "r", encoding="utf-8") as abi_definition:
    contract_abi = abi_definition.read()

# 从文件中读取字节码
with open("Traceability.bin", "r", encoding="utf-8") as bytecode_definition:
    contract_bytecode = bytecode_definition.read()

# 部署智能合约
Traceability = w3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
tx_hash = Traceability.constructor().transact({"from": w3.eth.accounts[0]})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract = w3.eth.contract(address=tx_receipt["contractAddress"], abi=contract_abi)

# 获取节点数据
ids_list = get_data(w3, contract)

START_TIME = datetime(2000, 1, 1)
END_TIME = datetime(2020, 12, 31)


def generate_random_datatime(start_date, time_between_dates: timedelta):
    random_number_of_days = random.randrange(time_between_dates.days)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date


def datetime_to_timestamp_string(dt: datetime):
    timestamp = time.mktime(dt.timetuple())
    return str(int(timestamp))


def new_product():
    # 随机原料提供
    _id = str(uuid.uuid4())
    date_time = generate_random_datatime(START_TIME, END_TIME - START_TIME)
    id0 = ids_list[0][random.randint(0, len(ids_list[0]) - 1)]
    tx_hash0 = contract.functions.createProduct(
        _id,
        datetime_to_timestamp_string(date_time),
        w3.eth.accounts[id0],
        Peoples[random.randint(0, len(Peoples) - 1)],
    ).transact({"from": w3.eth.accounts[id0]})
    w3.eth.wait_for_transaction_receipt(tx_hash0)

    # 随机产品生产
    date_time = generate_random_datatime(date_time, END_TIME - date_time)
    id1 = ids_list[1][random.randint(0, len(ids_list[1]) - 1)]
    tx_hash1 = contract.functions.transferProduct(
        _id,
        datetime_to_timestamp_string(date_time),
        w3.eth.accounts[id1],
        Peoples[random.randint(0, len(Peoples) - 1)],
    ).transact({"from": w3.eth.accounts[id0]})
    w3.eth.wait_for_transaction_receipt(tx_hash1)

    # 随机产品批发
    date_time = generate_random_datatime(date_time, END_TIME - date_time)
    id2 = ids_list[2][random.randint(0, len(ids_list[2]) - 1)]
    tx_hash2 = contract.functions.transferProduct(
        _id,
        datetime_to_timestamp_string(date_time),
        w3.eth.accounts[id2],
        Peoples[random.randint(0, len(Peoples) - 1)],
    ).transact({"from": w3.eth.accounts[id1]})
    w3.eth.wait_for_transaction_receipt(tx_hash2)

    # 随机是否零售
    if random.random() < 0.7:
        date_time = generate_random_datatime(date_time, END_TIME - date_time)
        id3 = ids_list[3][random.randint(0, len(ids_list[3]) - 1)]
        tx_hash3 = contract.functions.transferProduct(
            _id,
            datetime_to_timestamp_string(date_time),
            w3.eth.accounts[id3],
            Peoples[random.randint(0, len(Peoples) - 1)],
        ).transact({"from": w3.eth.accounts[id2]})
        w3.eth.wait_for_transaction_receipt(tx_hash3)

    return _id


def get_product(_id):
    product_info = contract.functions.getProduct(_id).call()
    return product_info


# 调用getObject函数
def get_object(address):
    object_info = contract.functions.getObject(address).call()
    return object_info


# if __name__ == "__main__":
#     test_id = new_product()
#     print(get_product(test_id))
#     print(get_object(w3.eth.accounts[0]))
