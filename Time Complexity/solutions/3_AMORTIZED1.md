# AMORTIZED1

## Problem Description

What is the time complexity of the following code :

```java
int j = 0;
for(int i = 0; i < n; ++i) {
    while(j < n && arr[i] < arr[j]) {
        j++;
    }
}
```

## Options

- [ ] O(n(logn)^2)
- [ ] O(nlogn)
- [ ] Can't say. Depends on the value of arr.
- [ ] O(n^2)
- [x] O(n)
