# Day 3 – Array Searching & Basic Problems

This folder contains basic array searching and simple operations with Python solutions.  
Each file includes:  
- Core logic (implemented from scratch)  
- Example run  
- User input option  
- Alternative/advanced implementation (in comments)  

---

### 01_linear_search.py
Search for a target element in an array using **Linear Search** (check each element one by one).  
Alternative: Use Python’s built-in `.index()` (with error handling).  

### 02_binary_search.py
Search for a target element in a **sorted array** using **Binary Search** (iterative approach).  
Alternative: Recursive binary search implementation.  

### 03_max_element.py
Find the **maximum element** in an array using iteration.  
Alternative: Use Python’s built-in `max()`.  

### 04_min_element.py
Find the **minimum element** in an array using iteration.  
Alternative: Use Python’s built-in `min()`.  

### 05_first_occurrence.py
Find the **first occurrence index** of a target element in an array.  
Alternative: Use Python’s `.index()` (with error handling).  

### 06_last_occurrence.py
Find the **last occurrence index** of a target element in an array.  
Alternative: Use slicing (`[::-1]`) with `.index()`.  

### 07_count_occurrences.py
Count how many times a target element occurs in the array.  
Alternative: Use Python’s `.count()` method.  

### 08_find_sum.py
Find the **sum of all elements** in an array using iteration.  
Alternative: Use Python’s built-in `sum()`.  

### 09_find_average.py
Find the **average of elements** in an array using manual sum and length.  
Alternative: Use `sum(arr)/len(arr)`.  

### 10_peak_element.py
Find a **peak element** in an array (an element greater than or equal to its neighbors).  
Alternative: Use a binary search based method for **O(log n)** solution.  

---