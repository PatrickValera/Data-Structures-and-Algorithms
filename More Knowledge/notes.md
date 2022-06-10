Binary Search Steps

1. calculate mid index 
2. if arr[mid] is equal to target return index
3. if target is less than arr[mid] binary search left side of mid element
4. otherwise, binary search right sid of mid element

5. recursively do this until start index overflows or exceed end index.


Bit wise operators

<<n shift bits left by n. Same as muliplying by 2^n
>>n shift bits right by n. Same as dividing by 2^n.
& compares to bits. Evaluates to 1 if BOTH bits are 1.
| compares two bits. Evalutes to 1 if one bit is 1.
^ compares two bits. Evaluates to 1 if both have different values.
~ reverses 1 to 0 and vice versa.