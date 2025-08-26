# Day 4 – Sorting Algorithms

This folder contains implementations of common sorting algorithms in Python.  
Each file includes:  
- Core logic (basic version)  
- Example run with user input  
- Alternative/advanced implementation (in comments)  

---

### 01_bubble_sort.py  
Sort an array using **Bubble Sort** (repeatedly swapping adjacent elements).  
Alternative: Use Python’s built-in `sorted()`.

### 02_selection_sort.py  
Sort an array using **Selection Sort** (repeatedly selecting the minimum).  
Alternative: Use `min()` to extract the smallest element each iteration.

### 03_insertion_sort.py  
Sort an array using **Insertion Sort** (build sorted array one element at a time).  
Alternative: Use `bisect` module for efficient insertions.

### 04_quick_sort.py  
Sort an array using **Quick Sort** (divide and conquer).  
Alternative: In-place partition-based quicksort.

### 05_merge_sort.py  
Sort an array using **Merge Sort** (divide and merge).  
Alternative: Use `heapq.merge`.

### 06_counting_sort.py  
Sort an array using **Counting Sort** (count occurrences of elements).  
Alternative: Use `collections.Counter`.

### 07_heap_sort.py  
Sort an array using **Heap Sort** (max-heap approach).  
Alternative: Use Python’s built-in `heapq`.

### 08_shell_sort.py  
Sort an array using **Shell Sort** (generalized insertion sort with gaps).  
Alternative: Use Python’s `sorted()`.

### 09_radix_sort.py  
Sort an array using **Radix Sort** (digit by digit stable sort).  
Alternative: Use `sorted()` with digit-based key.

### 10_bucket_sort.py  
Sort an array using **Bucket Sort** (distribute elements into buckets, then sort each).  
Alternative: Use `numpy` for bucket concatenation.

---
