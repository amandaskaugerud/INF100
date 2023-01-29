n = int(input())
languages = [int(x) for x in input().split(" ")]

last_saw_value = dict()

min_distance_between_same_language_speakers = n
for i in range(n):
    j = last_saw_value.get(languages[i],-1)
    if j>= 0:
        distance_i_j = i - j
        if distance_i_j < min_distance_between_same_language_speakers:
            min_distance_between_same_language_speakers = distance_i_j
    last_saw_value[languages[i]] = i
print(min_distance_between_same_language_speakers)