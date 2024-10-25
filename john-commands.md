# Examples: Use of John in Kali Linux
Find below some examples of how to use **John** in **Kali Linux** to crack passwords like the ones generated in this repository.


## Brute Force With Mask (Only Lowercase)
```sh
john --mask='?l?l?l?l?l?l?l?l' --min-length=3 --max-length=8 --format='md5crypt-long' dataset_X.txt
```

## Brute Force With Mask (Only Uppercase)
```sh
john --mask='?u?u?u?u?u?u?u?u' --min-length=3 --max-length=8 --format='md5crypt-long' dataset_X.txt
```

## Brute Force With Incremental (Only Numbers)
```sh
john --incremental=digits --format='md5crypt' dataset_X.txt
```

## Brute Force With Mask (Lowercase and Uppercase, Numbers, Symbols)
```sh
john --mask='?a?a?a?a?a?a?a?a' --min-length=3 --max-length=8 --format='md5crypt-long' dataset_X.txt
```