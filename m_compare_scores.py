#medium level

# given a list of "matches" where matches[i] = [winner, loser]
# return a list "answer" of size 2 where answer[0] = list of all players who never lost
# and answer[1] = list of all players that have lost exactly one match.

def find_winners(matches: list[list[int]]) -> list[list[int]]:
    if not check_string(matches):
        raise Exception("Sorry, the input matches are not correct.")

    players_defeats = {}
    for m in matches:
        if m[0] not in players_defeats:
            players_defeats[m[0]] = 0
        else:
            pass

        m[1]
        if m[1] not in players_defeats:
            players_defeats[m[1]] = 1
        else:
            players_defeats[m[1]] += 1

    # another way; less lines, a little more runtime:
    # for winner, loser in matches:
    #     players_defeats.setdefault(winner, 0)

    #     players_defeats.setdefault(loser, 0)
    #     players_defeats[loser] += 1

    answer = [[], []]
    for player, defeat in players_defeats.items():
        if defeat >= 2:
            continue
        elif defeat == 1:
            answer[1].append(player)
        else:
            answer[0].append(player)

    for a in answer:
        a.sort()
    return answer


def check_string(m: list[list[int]]) -> bool:
    a = len(m)
    if not 1 <= len(m) <= 10**5:
        return False

    for i in m:
        if len(i) != 2:
            return False
        if i[0] == i[1]:
            return False
        if not 1 <= i[0] <= 10**5 or not 1 <= i[1] <= 10**5:
            return False

    return True

match1 = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
match2 = [[2,3],[1,3],[5,4],[6,4]]

print(find_winners(match1))
print(find_winners(match2))