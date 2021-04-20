'''
Unit Testing and Code Coverage
python -m unittest -v QueueTest.py 
Coverage Reports
pip install coverage
coverage run -m unittest -v QueueTest.py
coverage html -d coverage_html
'''
from Queue import ArrayQueue, LinkedQueue 
from QueueExceptions import QueueEmptyException, QueueFullException 
# Testing Framework
import unittest
ARRAY_DEFAULT_CAPACITY = 5 

class TestArrayQueue(unittest.TestCase): 

  '''
  Test enqueue method
  '''
  def testEnqueue(self): 
    self.array_queue = ArrayQueue(5) 

    for i in range(0,4): 
      self.array_queue.enqueue(i) 
      # assertEquals(expected, actual, "error message")
      #self.assertEqual(i+1,self.array_queue.size(), "Size of Queue should be {}. Actual: {}".format(i+1, self.array_queue.size())) 
      self.assertEqual(0,self.array_queue.front(), "Front element must be {}".format(0)) 
    
    # Observe Exceptions
    # with assertRaises(Exception Class):
    #    code that causes exception
    with self.assertRaises(QueueFullException):
      self.array_queue.enqueue(100) 

  def testDequeue(self): 
    self.array_queue = ArrayQueue(5) 
    for i in range(0,4): 
      self.array_queue.enqueue(i) 
      self.assertEqual(i+1, self.array_queue.size(), "Size of Queue should be {}".format(i+1)) 
    for i in range(0,4): 
      self.assertEqual(i, self.array_queue.dequeue(), "Queue must return {}".format(i)) 
    with self.assertRaises(QueueEmptyException): 
      self.array_queue.dequeue()    

  def testQueueEmptyException(self): 
    self.array_queue = ArrayQueue(5) 
    with self.assertRaises(QueueEmptyException): 
      self.array_queue.dequeue()

  def testQueueFullException(self): 
    self.array_queue = ArrayQueue(5) 

    with self.assertRaises(QueueFullException): 
        for i in range(0, 7): 
            self.array_queue.enqueue(i)  

  def testQueueDefaultCapacity(self): 
    self.assertEqual(ARRAY_DEFAULT_CAPACITY, ArrayQueue.DEFAULT_CAPACITY) 

if __name__ == '__main__': 
    unittest.main() 