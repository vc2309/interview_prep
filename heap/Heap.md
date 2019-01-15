# Heap

## Structure
- Heap is a collection of elements of a homogeneous type, ordered such that the root element is always the extreme (max/min) element.
- The tree is always complete to the left most element.
- Usually implemented using an array.

## Applications
- Priority queues :  supports insert(), delete() and extractmax(), decreaseKey() operations in O(logn) time
- Order statistics : Kth smallest/largest elements, top k elements etc