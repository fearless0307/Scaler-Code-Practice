# NESTED_CMPL2

## Problem Description

What is the time complexity of the following code :

```java
int a = 0;
for (i = 0; i < N; i++) {
    for (j = N; j > i; j--) {
        a = a + i + j;
    }
}
```

## Options

- [ ] O(N*log(N))
- [x] O(N*N)
- [ ] O(N * Sqrt(N))
- [ ] O(N)
