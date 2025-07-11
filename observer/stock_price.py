from pattern import Subject, Observer


class EmailClient(Observer):
    def update(self, message: str):
        print(f"[Email] {message}")


class MobileApp(Observer):
    def update(serlf, message):
        print(f"[Mobile App notification] {message}")


class StockMarket(Subject):
    def set_price(self, stock_name: str, price: float):
        self.notify(f"{stock_name} is now ${price:.2f}")


if __name__ == "__main__":
    stock_market = StockMarket()

    email = EmailClient()
    mobile = MobileApp()

    stock_market.attach(email)
    stock_market.attach(mobile)

    stock_market.set_price("NICA", 1200)
