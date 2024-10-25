# Examples: Use of John The Ripper in Kali Linux
Find below some examples of how to use **John The Ripper** in **Kali Linux** to crack passwords like the ones generated in this repository.


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

## Dictionary Attack With Rules
```sh
john --wordlist=diccionario.txt --rules=all --format=md5crypt-long dataset_X.txt
```

This requires the file "john-local.conf" located at "/usr/share/john/john-local.conf" to have rules like the following:

```conf
# Rules John-local.conf

[List.Rules:E1]
d
[List.rules:E2]
\[ Az"54"
[List.Rules:E3]
r u
[list.Rules:E4]
f
[List.Rules:E5]
o0? A0"%"
```

These example rules are the following:

- **E1:** Duplicated word.

- **E2:** Inverted word without the first letter and with a 54 at the end.

- **E3:** Inverted word and capitalized.

- **E4:** Reflexed word.

- **E5:** Word with the first character changed for a "%" and with a "?" at the beginning.
