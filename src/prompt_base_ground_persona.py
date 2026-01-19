# for bidder
SYSTEM_MESSAGE_PROFILER = """
You are {name}. {persona}You are attending an ascending-bid housing auction as a bidder. This auction will have some other bidders to compete with you in bidding wars. The price is gradually raised, bidders drop out until finally only one bidder remains, and that bidder wins the item at this final price. Remember: {desire_desc}.
Here are some must-know rules for this auction:
1. Your competitor Bidder 1 is looking to purchase a second home in a scenic vacation destination, ideally near beaches or mountains, where he can escape the daily routine and enjoy quality time with family. His goal is to create a relaxing retreat for vacations while also considering its long-term potential as a future retirement home. The ideal property offers breathtaking views, easy access to outdoor activities, and a peaceful atmosphere. Whether it’s a beachfront property for summer getaways or a mountain retreat for year-round relaxation, he seeks a home that blends comfort, convenience, and the perfect setting for lifelong memories.
2. Your competitor Bidder 2 is a 29-year-old graphic designer earning $70,000 annually with $25,000 in savings, he is deeply drawn to the energy and convenience of urban living. He thrives in a bustling city environment where cultural experiences, dining options, and entertainment venues are just steps away. The vibrancy of city life fuels his creativity, making proximity to art galleries, music venues, and trendy cafés essential. He seeks a home in a walkable neighborhood, ideally in the city center or near major transit hubs, ensuring easy access to work and leisure. His lifestyle prioritizes connectivity, diversity, and the dynamic pulse of metropolitan living.
3. Item Values: The true value of an item means its resale value in the broader market, which you don't know. You will have a personal estimation of the item value. However, note that your estimated value could deviate from the true value, due to your potential overestimation or underestimation of this item.
4. Winning Bid: The highest bid wins the item. Your profit from winning an item is determined by the difference between the item's true value and your winning bid. You should try to win an item at a bid as minimal as possible to save your budget.
5. Winner Pays: Note that only the winner pays for the bidding price of the item. Other bidder who participate in the bidding but lost do not have to pay at all.
""".strip()


_LEARNING_STATEMENT_PROFILER = " and your learnings and profilings from previous auctions"


INSTRUCT_PLAN_TEMPLATE_PROFILER = """
As {bidder_name}, you have a total budget of ${budget}. This auction has a total of {item_num} items to be sequentially presented, they are:
{items_info}

---

Please plan for your bidding strategy for the auction based on the information{learning_statement}. A well-thought-out plan positions you advantageously against competitors, allowing you to allocate resources effectively. With a clear strategy, you can make decisions rapidly and confidently, especially under the pressure of the auction environment. Remember: {desire_desc}. 
Remember to observe and learn other bidders' bidding habits overtime, and try to take advantage from their preference to maximize your gain.

After articulate your thinking, in you plan, assign a priority level to each item. Present the priorities for all items in a JSON format, each item should be represented as a key-value pair, where the key is the item name and the value is its priority on the scale from 1-3. An example output is: {{"Fixture Y": 3, "Module B": 2, "Product G": 2}}. The descriptions of the priority scale of items are as follows.
    * 1 - This item is the least important. Consider giving it up if necessary to save money for the rest of the auction.
    * 2 - This item holds value but isn't a top priority for the bidder. Could bid on it if you have enough budget.
    * 3 - This item is of utmost importance and is a top priority for the bidder in the rest of the auction.
""".strip()

INSTRUCT_STRATEGY_TEMPLATE_WITH_PROFILE = """
The auctioneer says: "{auctioneer_msg}"

Here is your current status:
{prev_status}

Here is your current priority scale of all the items:
{current_plan}
The descriptions of the priority scale are as follows.
    * 1 - This item is the least important. Consider giving it up if necessary to save money for the rest of the auction.
    * 2 - This item holds value but isn't a top priority for the bidder. Could bid on it if you have enough budget.
    * 3 - This item is of utmost importance and is a top priority for the bidder in the rest of the auction.

Here is a profiling of your competitors' personas. A higher weight for a particular item type suggests that a bidder is more likely to bid on items of that type:
{currrent_profile}

Use the knowledge of your competitors' personas, your current status, and your priority list to make a **strategic** decision. Remember, {desire_desc}. Consider the following **key bidding practices**:
1. **Do not let competitors win items too easily**—forcing them to bid higher weakens their future purchasing power.  
2. **Exploit competitor weaknesses**—if a competitor values an item, consider bidding on it to drain their budget.  
3. **Only the winning bidder pays**—losing bidders pay nothing, so well-placed aggressive bids can weaken competitors.  
4. **Know when to stop**—if the profit margin is ≤ $300, it may not be worth pursuing.

You must select one of the following six strategic actions:  
A. **Increase the bid if this item is a top priority.**  
B. **Increase the bid to drain competitors’ budgets, especially if a competitor highly values this item.**  
C. **Increase the bid if your budget allows without compromising future rounds.**  
D. **Quit to conserve budget for higher-priority items.**  
E. **Quit because the profit margin is no longer attractive (i.e., profit margin ≤ $300).**  
F. **Quit to avoid a costly bidding war.**  

State your choice in the format:  
**"I chose to [action] because [reason]."**  
Make sure to **elaborate** on why you chose this action, considering your competitors’ profiles, your current status, and your priority list.
""".strip()

INSTRUCT_STRATEGY_TEMPLATE = """
The auctioneer says: "{auctioneer_msg}"

Here is your current status:
{prev_status}

Here is your current priority scale of all the items:
{current_plan}
The descriptions of the priority scale are as follows.
    * 1 - This item is the least important. Consider giving it up if necessary to save money for the rest of the auction.
    * 2 - This item holds value but isn't a top priority for the bidder. Could bid on it if you have enough budget.
    * 3 - This item is of utmost importance and is a top priority for the bidder in the rest of the auction.

Use the knowledge of your current status and your priority list to make a **strategic** decision. Remember, {desire_desc}. Consider the following **key bidding practices**:
1. **Do not let competitors win items too easily**—forcing them to bid higher weakens their future purchasing power.  
2. **Exploit competitor weaknesses**—if a competitor values an item, consider bidding on it to drain their budget.  
3. **Only the winning bidder pays**—losing bidders pay nothing, so well-placed aggressive bids can weaken competitors.  
4. **Know when to stop**—if the profit margin is ≤ $300, it may not be worth pursuing.

You must select one of the following six strategic actions:
A. **Increase the bid if this item is a top priority.**  
B. **Increase the bid to drain competitors’ budgets, especially if a competitor highly values this item.**  
C. **Increase the bid if your budget allows without compromising future rounds.**  
D. **Quit to conserve budget for higher-priority items.**  
E. **Quit because the profit margin is no longer attractive (i.e., profit margin ≤ $300).**  
F. **Quit to avoid a costly bidding war.**  

State your choice in the format:  
**"I chose to [action] because [reason]."**  
Make sure to **elaborate** on why you chose this action, considering your current status and your priority list.
""".strip()

INSTRUCT_BID_TEMPLATE_PROFILER = """
Now, the auctioneer says: "{auctioneer_msg}"

---

As {bidder_name}, you have to decide whether to bid on this item or withdraw and explain why, according to your plan{learning_statement}. Remember, {desire_desc}.

Here are some common practices of bidding:
1. Showing your interest by bidding with or slightly above the starting price of this item, then gradually increase your bid.
2. Think step by step of the pros and cons and the consequences of your action (e.g., remaining budget in future bidding) in order to achieve your primary objective.

Here is some professional strategic bidding advice to help you make your decision: "{strategic_reasoning}"

Follow the decision from the strategic bidding advice, then make your final decision clearly. You should either withdraw (saying "I'm out!") or make a higher bid for this item (saying "I bid $xxx!").
""".strip()


INSTRUCT_SUMMARIZE_TEMPLATE_PROFILER = """
Here is the history of the bidding war of {cur_item}:
"{bidding_history}"

The auctioneer concludes: "{hammer_msg}" 

---

{win_lose_msg} 
As {bidder_name}, you have to update the status of the auction based on this round of bidding. Here's your previous status:
``` 
{prev_status}
```

Summarize the notable behaviors of all bidders in this round of bidding for future reference. Then, update the status JSON regarding the following information:
- 'remaining_budget': The remaining budget of you, expressed as a numerical value.
- 'total_profits': The total profits achieved so far for each bidder, where a numerical value following a bidder's name. No equation is needed, just the numerical value.
- 'winning_bids': The winning bids for every item won by each bidder, listed as key-value pairs, for example, {{"bidder_name": {{"item_name_1": winning_bid}}, {{"item_name_2": winning_bid}}, ...}}. If a bidder hasn't won any item, then the value for this bidder should be an empty dictionary {{}}.
- Only include the bidders mentioned in the given text. If a bidder is not mentioned (e.g. Bidder 4 in the following example), then do not include it in the JSON object.

After summarizing the bidding history, you must output the current status in a parsible JSON format. An example output looks like:
```
{{"remaining_budget": 8000, "total_profits": {{"Bidder 1": 1300, "Bidder 2": 1800, "Bidder 3": 0}}, "winning_bids": {{"Bidder 1": {{"Item 2": 1200, "Item 3": 1000}}, "Bidder 2": {{"Item 1": 2000}}, "Bidder 3": {{}}}}}}
```
""".strip()

INSTRUCT_LEARNING_TEMPLATE_PROFILER = """
Review and reflect on the historical data provided from a past auction. 

{past_auction_log}

Here are your past learnings:

{past_learnings}

Based on the auction log, formulate or update your learning points that could be advantageous to your strategies in the future. Your learnings should be strategic, and of universal relevance and practical use for future auctions. Consolidate your learnings into a concise numbered list of sentences.
""".strip()

### This is long term memory, called every once in a repeat. Right after general learning.
### Long mem stored as a sentence discription of bidders.
INSTRUCT_LONG_MEMORY = """
As {bidder_name}, analyze the behavior of other bidders based on the engagement history of each bidder.

{past_engagement} 

Here is the information for all the items:
{items_info}

Here is your assessment of each bidder’s priority ranking for all items, with 3 indicating the highest priority:
{other_bidder_preferences}

Using data from the engagement history, formulate or update a profile for each bidder, focusing on discovering what type of houses they like to bid on. Consider what type of features the bidder is looking for in a house. Summarize the these knowledge of each bidder in a concise, descriptive sentence. Consolidate them into a list of sentences.
""".strip()

# INSTRUCT_LONG_MEMORY = """
# As {bidder_name}, analyze the behavior of other bidders based on previous auction log.

# {past_auction_log}

# Here is your assessment of each bidder’s priority ranking for all items, with 3 indicating the highest priority.:
# {other_bidder_preferences}

# Using data from the previous auction logs, formulate or update a profile for each bidder, focusing on their housing preferences. Summarize the profile for each bidder in a concise, descriptive sentence. Consolidate them into a list of sentences.
# """.strip()


INSTRUCT_REPLAN_TEMPLATE_PROFILER = """
The current status of you and other bidders is as follows:
```
{status_quo}
```

Here are the remaining items in the rest of the auction:
"{remaining_items_info}"

As {bidder_name}, considering the current status{learning_statement}, review your strategies. Adjust your plans based on the outcomes and new information to achieve your primary objective. This iterative process ensures that your approach remains relevant and effective. Please do the following:
1. Always remember: {desire_desc}.
4. Determine and explain if there's a need to update the priority list of remaining items based on the current status and the priority of other bidders. 
5. Present the updated priorities in a JSON format, each item should be represented as a key-value pair, where the key is the item name and the value is its priority on the scale from 1-3. An example output is: {{"Fixture Y": 3, "Module B": 2, "Product G": 2}}. The descriptions of the priority scale of items are as follows.
    * 1 - This item is the least important. Consider giving it up if necessary to save money for the rest of the auction.
    * 2 - This item holds value but isn't a top priority for the bidder. Could bid on it if you have enough budget.
    * 3 - This item is of utmost importance and is a top priority for the bidder in the rest of the auction.
""".strip()

### This is the short memory, short mem stored as priority list on items
INSTRUCT_PROFILE_TEMPLATE = """
Here is the history of the bidding war of {cur_item}:
"{bidding_history}"

You are {bidder_name}. You are given a persona list: ["First-Time Homebuyers", "Upgrade to a Larger Home", "Downsizing", "Investment Buyers", "Relocation for Work", "Vacation Homes", "Eco-Conscious Buyers", "Urban Dwellers", "Rural Home Seekers", "Multigenerational Living"].
Given the bidding history you have seen so far, complete the below steps:
1. Study the bidding history, focus on how many times {target_bidder} rasied price for this item and what are the wining bids so far for each bidder. These 2 factors often say something about a person.
2. Based on {target_bidder}'s willingness to raise the price for this item, combining this items description: {house_desc}, predict the bidders' persona from the given persona list.
3. If the bidder does not show any interests for this item at all, you can reduce the weights on the personas that closely match with this item, even to the negatives. 
4. Formulate your predictionn into how much weight each persona plays in {target_bidder}'s bidding. Present the prediction in the JSON format like this {{"{target_bidder}": {{"First-Time Homebuyers": 0.2, "Upgrade to a Larger Home": 0.1, "Downsizing": 0.1...}}}} where the key is the persona type and the value is the weight of that persona type.
5. Make sure the range of each weights are within the range of -1 to 1. Make sure the output dictionary has 10 keys, each representing a persona type from the given list.
If {target_bidder} does not make any informative actions for a prediction, output an dictionary like {{"{target_bidder}": {{"First-Time Homebuyers": 0.0, "Upgrade to a Larger Home": 0.0, "Downsizing": 0.0...}}}} where all weights are 0. 
"""

INSTRUCT_REPROFILE_TEMPLATE = """
Here is the history of the bidding war of {cur_item}:
"{bidding_history}"

Here is the past prediction on {target_bidder}'s persona conposition:
"{old_predict}"

Given the bidding history you have seen so far, complete the below steps:
1. Study the bidding history, focus on how many times {target_bidder} rasied price for this item and what are the wining bids so far for each bidder. These 2 factors often say something about a person.
2. Based on {target_bidder}'s willingness to raise the price for this item, combining this items description: {house_desc}, update the bidders' persona based on the given persona list.
3. If the bidder does not show any interests for this item at all, you can reduce the weights on the personas that closely match with this item, even to the negatives. 
4. When updating the persona estimation, do not make drastic changes. For example, do not reduce a high weight persona into the lowest weight in a single update. 
5. Formulate your updated prediction into how much weight each persona plays in {target_bidder}'s bidding. Present the prediction in the JSON format like this {{"{target_bidder}": {{"First-Time Homebuyers": 0.2, "Upgrade to a Larger Home": 0.1, "Downsizing": 0.1...}}}} where the key is the persona type and the value is the weight of that persona type.
6. Make sure the range of each weights are within the range of -1 to 1. Make sure the output dictionary has 10 keys, each representing a persona type from the given list.
If {target_bidder} does not make any informative actions for a prediction, keep the prediction unchanged and output the unchanged result. 
"""

INSTRUCT_STRATEGY_TEMPLATE_TOM = """"""
