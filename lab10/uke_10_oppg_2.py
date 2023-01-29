# en hjelpefunksjon som jeg brukte først
# def find_difference(int1, int2):
#     difference = abs(int1 - int2)
#     if difference > 10:
#         return True
#     else: return False

# oppgave 2
def num_pairwise_diff_gt10(a):
    # tom telle variabel
    count = 0
    # løper gjennom listen med tall
    for i in range(1, len(a)):
        # regner ut differansen mellom to etterfølgende tall
        if abs(a[i]-a[i-1])> 10:
            count += 1
    # returnerer antall tall som har differanse større enn 10
    return count
