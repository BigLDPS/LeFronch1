#Implement quicksort in file to make it extremely easy, not sure how to import either :)
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

#imports 
import unittest

class TestQuickSort(unittest.TestCase):

    #empty defn
    def test_empty_list(self):
        self.assertEqual(quicksort([]), [])

    #only ojne element
    def test_single_element(self):
        self.assertEqual(quicksort([1]), [1])


    #presorted
    def test_sorted_list(self):
        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    #repeating
    def test_duplicate_elements(self):
        self.assertEqual(quicksort([4, 5, 4, 3, 4, 2, 1]), [1, 2, 3, 4, 4, 4, 5])

    #regular
    def test_unsorted_list(self):
        self.assertEqual(quicksort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])




# Run the unit tests
if __name__ == "__main__":
    unittest.main()
