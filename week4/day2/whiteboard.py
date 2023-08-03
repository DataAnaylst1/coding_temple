# You are playing an RPG game. Currently your experience points (XP) total is equal to experience. To reach the next level your XP should be at least at threshold. If you kill the monster in front of you, you will gain more experience points in the amount of the reward.
# Given values experience, threshold and reward, check if you reach the next level after killing the monster.
# Example
# For experience = 10, threshold = 15, and reward = 5, the output should be
# solution(experience, threshold, reward) = true;
# For experience = 10, threshold = 15, and reward = 4, the output should be
# solution(experience, threshold, reward) = false.

#Understand
# My experience points, (XP) has to equal out to the threshold
# I need to determine if the reward equals the difference between my current level of experience versus the threshold given
# If it is not, I need to return False,
# If it is, I need to return True

#Plan
# I could do a conditional statement, boolean with True or False outcome,
# Have parameters set with experience, threshold and reward
#if threshold minus experience equals reward,
# if experience plus reawrd is greater than or equal to threshold
# Return True

# Execute



def outcome(xp:int, reward:int, threshold:int):
#     if xp + reward >= threshold:
#         return True
#     return False
# print(outcome(10,4,15))
    return xp + reward >= threshold
print(outcome(10,4,15))
