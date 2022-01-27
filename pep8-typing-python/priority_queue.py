class PriorityQueue:
    code: int = 0
    queue = []
    customers_served = []
    current_password: str = ''

    def generate_current_password(self) -> None:
        self.current_password = f'PR{self.code}'

    def reset_queue(self) -> None:
        if self.code >= 100:
            self.code = 0
        else:
            self.code += 1

    def update_queue(self) -> None:
        self.reset_queue()
        self.generate_current_password()
        self.queue.append(self.current_password)

    def call_customer(self, cashier: int) -> str:
        current_customer = self.queue.pop(0)
        self.customers_served.append(current_customer)

        return f'Current customer: {current_customer}, go to cashier {cashier}'

    def statistic(self, day: str, bank_agency: int, flag: str) -> dict:
         if flag != 'detail':
             statistic = {f'{bank_agency} - {day} : {len(self.customers_served)}'}
         else:
             statistic = {}
             statistic['day'] = day
             statistic['bank agency'] = bank_agency
             statistic['customers served'] = self.customers_served
             statistic['quantity customers served'] = len(self.customers_served)

         return statistic
