# -*- coding: utf-8 -*-
"""introduction-to-collections.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zn6ymIQi8fgT7Vy5ooei_WRRc7wTUliV
"""

age_01 = 39
age_02 = 30
age_03 = 27
age_04 = 18

print(age_01)
print(age_02)
print(age_03)
print(age_04)

ages = [39, 30, 27, 18]
type(ages)

len(ages)

ages[0]

ages

ages.append(15)

ages

ages[4]

for age in ages:
  print(age)

ages.remove(30)

ages

ages.append(15)

ages

ages.remove(15)

ages

ages.append(27)
ages.remove(27)
ages

28 in ages

15 in ages

if 15 in ages:
  ages.remove(15)

ages

ages.clear()
ages

ages = [39, 18, 15, 27]
ages

"""*Adicionando elementos em uma lista :*

```
# Adicionando 1 elemento em 1 posicao 
```
"""

ages.insert(0, 20)
ages

"""

```
# Adicionando varios elementos em 1 lista, ou elementos de uma lista em outra lista.
```

"""

new_ages = [19, 21, 40]
ages.extend(new_ages)
ages

"""
```
# Descobrindo idades do proximo ano
```
"""

ages_next_year = []
for age in ages:
    ages_next_year.append(age + 1)
ages_next_year

"""

```
# List comprehension
```

"""

ages_next_year = [(age + 1) for age in ages]
ages_next_year

[(age) for age in ages if age > 21]

def next_year(age):
  return age + 1

[next_year(age) for age in ages if age > 21]
