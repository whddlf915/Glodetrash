class Kiwoom():
    def __init__(self):
        self.stock_dict = {"네이버":6000, "애플":15000, "다음":3000, "넷플릭스":5000, "구글":100000, "삼성":3000, \
                      "LG":1000, "키움":500, "호랑":8000, "셀트리온":8500, "코난":6050, "컬링":1000, "하이원":3200}
        self.stock_num = {"네이버": 10, "애플": 10, "다음": 10, "넷플릭스": 10, "구글": 10, "삼성": 10, \
                           "LG": 10, "키움": 10, "호랑": 10, "셀트리온": 10, "코난": 10, "컬링": 10, "하이원": 10}
        self.global_list = ["넷플릭스", "애플", "구글"]

class Condition(Kiwoom):
    def __init__(self):
        super().__init__()
        self.sell_filteting()

    def sell_filteting(self):
        for key, price in self.stock_dict.items():
            if price <= 5000:
                print("%s: %d" % (key, price))
            for list in self.global_list:
                if key == list:
                    self.stock_num.update({key: self.stock_num.get(key)/2})
        print(self.stock_num)

Condition()
