import math

def alpha_beta(curDepth, nodeIndex, maxTurn, scores, targetDepth, alpha, beta):
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        maxScore = float('-inf')
        for neighbor in range(nodeIndex * 2, nodeIndex * 2 + 2):
            score = alpha_beta(curDepth + 1, neighbor, False, scores, targetDepth, alpha, beta)
            maxScore = max(maxScore, score)
            alpha = max(alpha, maxScore)
            if beta <= alpha:
                break  # Beta cut-off
        return maxScore

    else:
        minScore = float('inf')
        for neighbor in range(nodeIndex * 2, nodeIndex * 2 + 2):
            score = alpha_beta(curDepth + 1, neighbor, True, scores, targetDepth, alpha, beta)
            minScore = min(minScore, score)
            beta = min(beta, minScore)
            if beta <= alpha:
                break  # Alpha cut-off
        return minScore

# Driver code
scores = [3, 5, 2, 9, 12, 5, 23, 23]

treeDepth = math.log(len(scores), 2)

print("The optimal value with alpha-beta pruning is:", end=" ")
print(alpha_beta(0, 0, True, scores, treeDepth, float('-inf'), float('inf')))
