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
    mu_vals.append(3*(i+1));
    dev_vals.append(mu_vals[i]*dev_factor);
    
    
optimal_mean_reward = max(mu_vals)*num_days;     # Maximum reward possible


print("\nThe mean of the arm distributions are - ",mu_vals,"\n");
print("The deviation of the arm distributions are - ",dev_vals,"\n");  

#==============================================================================

# Algorithm - Epsilon Greedy
# Defining the function that calculates the rewards for Epsilon Greedy algorithm
def epsilon_greedy(num_of_rounds,num_of_arms):
    epsilon=0.1;
    reward=[];
    cumulative_reward_history=np.zeros((1,num_of_arms));
    avg_cumulative_reward_history=np.zeros((1,num_of_arms));
    arm_history_count=np.ones((1,num_of_arms));
    
    # Exploring all arms once before starting the toss for explore vs exploit
    for j in range(0,num_of_arms):
        r=arm_reward_samples(mu_vals[j],dev_vals[j]);
        reward.append(r);
        cumulative_reward_history[0,j]=r;
    del j
    # Tossing to decide whether to explore or exploit and proceeding as such
    d=rand.uniform(0,1);
    
    for i in range(num_of_arms,num_of_rounds):
        
        # Exploring (Very less probable)
        if (d <= epsilon):
            index=rand.randint(0,2);
            r=arm_reward_samples(mu_vals[index],dev_vals[index]);
            reward.append(r);
            arm_history_count[0,index]=arm_history_count[0,index]+1;
            cumulative_reward_history[0,index]=cumulative_reward_history[0,index]+r;
            
        # Exploiting  (Most of the times)   
        elif(d > epsilon):
            # Checking which arm has yeilded maximum average reward till mow
            for j in range(0,num_of_arms):
                m=cumulative_reward_history[0,j];
                n=arm_history_count[0,j];
                avg_cumulative_reward_history[0,j] = m/n;
            del j
        #Exploiting that arm which has yeilded maximum average reward till now        
        index=np.argmax(avg_cumulative_reward_history);
            
        r=arm_reward_samples(mu_vals[index],dev_vals[index]);
        reward.append(r);
        arm_history_count[0,index]=arm_history_count[0,index]+1;
        cumulative_reward_history[0,index]=cumulative_reward_history[0,index]+r;
         
    del i 
    return sum(reward);

#==============================================================================
# Calling the Algorithm and estimating the average regret under it

# Calculating the mean regret for epsilon greedy algorithm
epsilon_greedy_rewards=[];
for j in range(0,1000):
    r3=epsilon_greedy(num_rounds,num_arms);
    epsilon_greedy_rewards.append(r3);
       
mean_of_e_greedy_regret=optimal_mean_reward - np.mean(epsilon_greedy_rewards);
# moegr =  "M"ean  "O"f "E"psilon "G"reedy "R"egret
moegr=mean_of_e_greedy_regret/optimal_mean_reward;
print("The regret for Epsilon Greedy policy is : ",moegr);

del j