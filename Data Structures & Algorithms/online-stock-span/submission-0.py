class StockSpanner:

    def __init__(self):
        self.p_stack = []
        self.s_stack = []

    def next(self, price: int) -> int:
            span = 1
            if not self.p_stack:
                self.p_stack.append(price)
                self.s_stack.append(span)
                return span
            
            if self.p_stack[-1] > price:
                self.p_stack.append(price)
                self.s_stack.append(span)
            else:
                while self.p_stack and self.p_stack[-1] <= price:
                    self.p_stack.pop()
                    span += self.s_stack.pop()
                self.p_stack.append(price)
                self.s_stack.append(span)

            return span  



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)