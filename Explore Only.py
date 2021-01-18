#==============================================================================
# This code is modelled for a simple MAB problem where the distribution of the 
# rewards are assumed to be normally distributed. The number of player is only
# one.
#==============================================================================

# Importing the useful libraries
import numpy as np
import random as rand
import matplotlib.pyplot as plot 

#==============================================================================

# Defining the function to pick an arm(RV form the distribution) randomly
def arm_reward_samples(mu,sd):
    RV=np.random.normal(mu,sd);
    return RV;

#==============================================================================

# Taking the momdel parameters as entry here
num_rounds = 300;     # No. of rounds to be played / Time till which we survey

dev_factor = 0.5;            # Deviation of each reward ddistribution from its mean
num_arms = 3;         # Number of restaurants / arms

#==============================================================================

# Deciding the mean and variance of the arm distributions  and then getting the 
# theoretical already known optimal regret as well

# Getting the Mean and SD of distribution of each restaurant / arm
dev_vals=[];
mu_vals=[];
for i in range(0,num_restaurants):
    mu_vals.append(2*(i+1)/4);
    dev_vals.append(mu_vals[i]*dev_factor);
    
    
optimal_mean_reward = max(mu_vals)*num_days;     # Maximum reward possible


print("\nThe mean of the arm distributions are - ",mu_vals,"\n");
print("The deviation of the arm distributions are - ",dev_vals,"\n");  

#==============================================================================

# Algorithm - Explore Only
# Defining the function that calculates the rewards for explore only algorithm     
def only_exploration(num_of_rounds):
    reward=[];
    for i in range(0,num_of_rounds):
        a=rand.randint(0,num_arms-1);
        reward.append(arm_reward_samples(mu_vals[a],dev_vals[a]));
    
    return sum(reward);
    del reward,i

#==============================================================================

# Calling the Algorithm and estimating the average regret under it

# Calculating mean regret for explore only algorithm
explore_alone_rewards=[];
for j in range(0,1000):
    r1=only_exploration(num_rounds);
    explore_alone_rewards.append(r1);

mean_of_explore_alone_regret=optimal_mean_reward - np.mean(explore_alone_rewards);
# moeear = "M"ean  "O"f  "E"xplor"E"  "A"lone  "R"egret
moeear=mean_of_explore_alone_regret/optimal_mean_reward;
print("The regret for Explore Only policy is : ",moeear);
del j