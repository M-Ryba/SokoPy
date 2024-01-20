def sort_leaderboard(leaderboard, level_number):
    level_scores = leaderboard[str(level_number)]
    ln = len(level_scores)
    for i in range(ln-1):
        for j in range(ln-i-1):
            if level_scores[j][1] > level_scores[j+1][1]:
                level_scores[j], level_scores[j+1] = level_scores[j+1], level_scores[j]
    return leaderboard
