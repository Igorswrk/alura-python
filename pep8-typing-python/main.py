from normal_queue import NormalQueue
from priority_queue import PriorityQueue

# queue_test = NormalQueue()
# queue_test.update_queue()
# queue_test.update_queue()
# queue_test.update_queue()
# print(queue_test.call_customer(10))

queue_test_2 = PriorityQueue()
queue_test_2.update_queue()
queue_test_2.update_queue()
queue_test_2.update_queue()
print(queue_test_2.call_customer(10))
print(queue_test_2.call_customer(1))
print(queue_test_2.statistic('13/10/2000', 100, 'detail'))