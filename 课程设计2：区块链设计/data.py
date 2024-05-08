from web3 import Web3
from web3.contract import Contract

Peoples = ["李晓婷", "张伟豪", "王雅娜", "刘军宇", "陈雪婷", "杨宇航", "赵晓梅"]


def get_data(w3: Web3, contract: Contract) -> list:
    Ids = []
    Ids.append(get_supplier(w3, contract))
    Ids.append(get_producer(w3, contract))
    Ids.append(get_wholesaler(w3, contract))
    Ids.append(get_retailer(w3, contract))
    return Ids


def get_supplier(w3: Web3, contract: Contract):
    tx_hash1 = contract.functions.createObject(
        "提供商A",  # 名称
        "1234567890",  # 电话号码
        "https://so1.360tres.com/t0126bab79cfb5f11bb.jpg",  # 图片
        "原料供给",  # 类别
        "山东省青岛市市南区香港中路123号",  # 地址
        "This is a description for Object 1",  # 描述
    ).transact({"from": w3.eth.accounts[0]})
    w3.eth.wait_for_transaction_receipt(tx_hash1)

    tx_hash2 = contract.functions.createObject(
        "提供商 B",  # 名称
        "0987654321",  # 电话号码
        "https://so1.360tres.com/t0126bab79cfb5f11bb.jpg",  # 网站
        "原料供给",  # 类别
        "河南省郑州市金水区农业路1001号",  # 地址
        "This is a description for Object 2",  # 描述
    ).transact({"from": w3.eth.accounts[1]})
    w3.eth.wait_for_transaction_receipt(tx_hash2)

    return [0, 1]


def get_producer(w3: Web3, contract: Contract):
    tx_hash3 = contract.functions.createObject(
        "生产商 A",  # 名称
        "1234567890",  # 电话号码
        "https://th.bing.com/th/id/R.4b538dd6fe6e043524f9a526f24d3698?rik=TZeKw0LxwAe%2fAQ&riu=http%3a%2f%2fsheencity-bj.oss-cn-hangzhou.aliyuncs.com%2fofficial-site%2fpictures%2f2014-08%2f16%2f190c43f37cf24d8c3e13859d9d01bbf7.jpg&ehk=jIRvgyeJgU86%2fWgegSmdJs6qIYGz%2b1BvzS4GHv7ebCs%3d&risl=&pid=ImgRaw&r=0",  # 网站
        "产品生产",  # 类别
        "湖北省武汉市洪山区珞喻路1800号",  # 地址
        "This is a description for Object 1",  # 描述
    ).transact({"from": w3.eth.accounts[2]})
    w3.eth.wait_for_transaction_receipt(tx_hash3)

    tx_hash4 = contract.functions.createObject(
        "生产商 B",  # 名称
        "0987654321",  # 电话号码
        "https://th.bing.com/th/id/R.4b538dd6fe6e043524f9a526f24d3698?rik=TZeKw0LxwAe%2fAQ&riu=http%3a%2f%2fsheencity-bj.oss-cn-hangzhou.aliyuncs.com%2fofficial-site%2fpictures%2f2014-08%2f16%2f190c43f37cf24d8c3e13859d9d01bbf7.jpg&ehk=jIRvgyeJgU86%2fWgegSmdJs6qIYGz%2b1BvzS4GHv7ebCs%3d&risl=&pid=ImgRaw&r=0",  # 网站
        "产品生产",  # 类别
        "四川省成都市高新区天府大道中段999号",  # 地址
        "This is a description for Object 2",  # 描述
    ).transact({"from": w3.eth.accounts[3]})
    w3.eth.wait_for_transaction_receipt(tx_hash4)

    tx_hash5 = contract.functions.createObject(
        "生产商 C",  # 名称
        "0987654321",  # 电话号码
        "https://th.bing.com/th/id/R.4b538dd6fe6e043524f9a526f24d3698?rik=TZeKw0LxwAe%2fAQ&riu=http%3a%2f%2fsheencity-bj.oss-cn-hangzhou.aliyuncs.com%2fofficial-site%2fpictures%2f2014-08%2f16%2f190c43f37cf24d8c3e13859d9d01bbf7.jpg&ehk=jIRvgyeJgU86%2fWgegSmdJs6qIYGz%2b1BvzS4GHv7ebCs%3d&risl=&pid=ImgRaw&r=0",  # 网站
        "产品生产",  # 类别
        "辽宁省大连市中山区人民路456号",  # 地址
        "This is a description for Object 2",  # 描述
    ).transact({"from": w3.eth.accounts[4]})
    w3.eth.wait_for_transaction_receipt(tx_hash5)

    return [2, 3, 4]


def get_wholesaler(w3: Web3, contract: Contract):
    tx_hash6 = contract.functions.createObject(
        "批发商 A",  # 名称
        "1234567890",  # 电话号码
        "https://th.bing.com/th/id/OIP.8kkIMYOSk7ZTT1LzOym8OwHaFj?rs=1&pid=ImgDetMain",  # 网站
        "批发销售",  # 类别
        "福建省厦门市思明区湖滨南路789号",  # 地址
        "This is a description for Object 3",  # 描述
    ).transact({"from": w3.eth.accounts[5]})
    w3.eth.wait_for_transaction_receipt(tx_hash6)

    tx_hash7 = contract.functions.createObject(
        "批发商 B",  # 名称
        "0987654321",  # 电话号码
        "https://th.bing.com/th/id/OIP.8kkIMYOSk7ZTT1LzOym8OwHaFj?rs=1&pid=ImgDetMain",  # 网站
        "批发销售",  # 类别
        "广西壮族自治区南宁市青秀区民族大道1010号",  # 地址
        "This is a description for Object 4",  # 描述
    ).transact({"from": w3.eth.accounts[6]})
    w3.eth.wait_for_transaction_receipt(tx_hash7)
    return [5, 6]


def get_retailer(w3: Web3, contract: Contract):
    # Retailer 1
    tx_hash1 = contract.functions.createObject(
        "零售商 1",  # 名称
        "1234567890",  # 电话号码
        "https://th.bing.com/th/id/OIP.kIlmhfvXSDtxWUu9GEwWEwHaFG?rs=1&pid=ImgDetMain",  # 网站
        "零售销售",  # 类别
        "北京市朝阳区光华路58号",  # 地址
        "This is a description for Object 5",  # 描述
    ).transact({"from": w3.eth.accounts[7]})
    w3.eth.wait_for_transaction_receipt(tx_hash1)

    # Retailer 2
    tx_hash2 = contract.functions.createObject(
        "零售商 2",  # 名称
        "0987654321",  # 电话号码
        "https://th.bing.com/th/id/OIP.kIlmhfvXSDtxWUu9GEwWEwHaFG?rs=1&pid=ImgDetMain",  # 网站
        "零售销售",  # 类别
        "上海市浦东新区世纪大道2001号",  # 地址
        "This is a description for Object 6",  # 描述
    ).transact({"from": w3.eth.accounts[8]})
    w3.eth.wait_for_transaction_receipt(tx_hash2)

    # Retailer 3
    tx_hash3 = contract.functions.createObject(
        "零售商 3",  # 名称
        "1234567890",  # 电话号码
        "https://th.bing.com/th/id/OIP.kIlmhfvXSDtxWUu9GEwWEwHaFG?rs=1&pid=ImgDetMain",  # 网站
        "零售销售",  # 类别
        "广东省深圳市福田区华强北路1002号",  # 地址
        "This is a description for Object 7",  # 描述
    ).transact({"from": w3.eth.accounts[9]})
    w3.eth.wait_for_transaction_receipt(tx_hash3)

    # Retailer 4
    tx_hash4 = contract.functions.createObject(
        "零售商 4",  # 名称
        "0987654321",  # 电话号码
        "https://th.bing.com/th/id/OIP.kIlmhfvXSDtxWUu9GEwWEwHaFG?rs=1&pid=ImgDetMain",  # 网站
        "零售销售",  # 类别
        "江苏省南京市鼓楼区中山北路888号",  # 地址
        "This is a description for Object 8",  # 描述
    ).transact({"from": w3.eth.accounts[10]})
    w3.eth.wait_for_transaction_receipt(tx_hash4)

    # Retailer 5
    tx_hash5 = contract.functions.createObject(
        "零售商 5",  # 名称
        "1234567890",  # 电话号码
        "https://th.bing.com/th/id/OIP.kIlmhfvXSDtxWUu9GEwWEwHaFG?rs=1&pid=ImgDetMain",  # 网站
        "零售销售",  # 类别
        "浙江省杭州市西湖区西溪路666号",  # 地址
        "This is a description for Object 9",  # 描述
    ).transact({"from": w3.eth.accounts[11]})
    w3.eth.wait_for_transaction_receipt(tx_hash5)

    return [7, 8, 9, 10, 11]
