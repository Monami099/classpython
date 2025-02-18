import random
random_set={random.randint(15,45)for_in range(10)}
count_less_than_30=sum(1 for num in random_set if num<30)
filtered_set={num for num in random_set if num<=35}
print("original set:",random_set)
print("count of numbers less than 30:",count_less_than_30)
print("set after deleting numbers greater than 35:",filtered_set
