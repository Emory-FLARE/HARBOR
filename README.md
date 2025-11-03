# HARBOR
HARBOR: exploring persona dynamics in multi-agent competition

### Data & Configuration
1. Clone the repo and install packages in your preferred conda or virtual env
<pre>
git clone https://github.com/Emory-FLARE/HARBOR
pip install -r requirements.txt
</pre>
2. Configure the Bidders in the `data/bidders.jsonl`. Below is an example:
<pre>
{"name": "Bidder 0","trait": "Rural Home Seekers","is_profiler": true, "use_external_reason":true,"model_name": "claude-3-5-sonnet-20241022","budget": 1000000,"desire": "maximize_profit","plan_strategy": "adaptive","temperature": 0,"overestimate_percent": 10,"correct_belief": true,"enable_learning": false,"persona": "You are a dedicated farmer with a combined annual income of $95,000 and $70,000 in savings, you are seeking a spacious property in a rural setting that aligns with both your professional and personal aspirations. You value the peace and serenity of country living, where open land and fresh air provide the perfect backdrop for a sustainable, self-sufficient lifestyle. Your ideal home is surrounded by fertile farmland, offering ample space to expand your agricultural operations. Proximity to essential farming resources, like feed suppliers and markets, is important, but above all, you prioritize a quiet, nature-filled environment away from urban congestion."}
{"name": "Bidder 1","trait": "Urban Dwellers","is_profiler": false, "use_external_reason":false,"model_name": "claude-3-5-sonnet-20241022","budget": 1000000,"desire": "maximize_profit","plan_strategy": "adaptive","temperature": 0,"overestimate_percent": 10,"correct_belief": true,"enable_learning": false,"persona": "You are a 29-year-old graphic designer earning $70,000 annually with $25,000 in savings, you are deeply drawn to the energy and convenience of urban living. You thrive in a bustling city environment where cultural experiences, dining options, and entertainment venues are all within easy reach. The vibrancy of city life fuels your creativity, making proximity to art galleries, music venues, and trendy cafés essential. You seek a home in a walkable neighborhood, ideally in the city center or near major transit hubs, ensuring easy access to work and leisure. Your lifestyle prioritizes connectivity, diversity, and the dynamic pulse of metropolitan living."}
</pre>
You can set 2~5 agents for controllable performance. Here is the usage of each field in configuring an agent.
<pre>
name: the unique name for each bidder.
trait: the tag used to label a long persona description.
is_profiler: true/false, set to true to make this bidder capable of profiling others.
use_external_reason: true/false, set to true if you have customarily trained open-source models.
model_name: the model backing up for this agent, normally claude-3-5-sonnet or gpt-3.5.
budget: the initial budget the bidder has when entering the auction.
desire: fix to maximize_profit in our study (you can set it to max_items to encourage item acquisition), the bidder aims to profit from this auction.
plan_strategy: fix to "adaptive" to enable agents to change their priority based on auction dynamics.
temperature: generation temperature for the LLM.
overestimate_percentage; int, for example, if set to 10, the bidder would estimate the value of an item 10% higher than that item's true price, which is hidden from everyone.
enable_learning: true/false, only useful if you are conducting several auctions in a row, then when set to true, the bidders can learn from experience from previous rounds of auctions.
persona: a long descriptive persona string used in prompt injection to affect the bidder's preferences.
</pre>
Please find a list of bidders/personas to choose from in `data/bidders_pool.json`.

3. Configure the Houses (Auction Items) in the `data/houses.jsonl`. Below is an example:
<pre>
{"trait": "Rural Home Seekers", "name": "Construction 1", "price": 200000, "id": 1, "true_value": 500000, "desc": "This 4-bedroom, 3-bath rural retreat offers a perfect blend of charm and functionality on a spacious lot ideal for farming or a peaceful lifestyle. Featuring an updated kitchen, hardwood floors, high ceilings, and a two-story living room, it combines modern comfort with rustic appeal. Equipped with a modern HVAC system, water heater, and access to nearby trails and parks, it\u2019s perfect for those seeking tranquility in the countryside."}
{"trait": "First-Time Homebuyers", "name": "Home 1", "price": 160000, "id": 2, "true_value": 400000, "desc": "Ideal for first-time homebuyers, this charming 3-bedroom, 2-bath home offers 1,500 sq. ft. of comfortable living space in a peaceful suburban neighborhood. Updated modern kitchen and bathrooms (2020) and a recently replaced HVAC system (2018) ensure convenience and low maintenance. The property features a 2-car garage and a manageable yard, perfect for a busy lifestyle. Close to parks, shopping, and highways, it combines safety (neighborhood rating: 8) with accessibility. A budget-friendly choice to start your homeownership journey!"}
{"trait": "Relocation for Work", "name": "Property 1", "price": 170000, "id": 3, "true_value": 425000, "desc": "Ideal for professionals relocating for work, this 3-bedroom, 2-bath urban home offers convenience and comfort just minutes from downtown. Built in 2000, the 1,800 sq. ft. property features a modern kitchen, hardwood floors, high ceilings, and a spacious living room. Recent updates to the HVAC system and water heater ensure year-round comfort. Located in a safe neighborhood near parks, shopping, and major highways, with a low HOA fee and a two-car garage, this home is perfect for easy commuting and hassle-free living."}
</pre>
The house in the auction has several tunable parameters:
<pre>
trait: same set of strings as the trait in Bidder, this is only used as labelling purposes to control the alignment between bidders and perferred houses.
name: the name of the house for short references in auctions.
price: the starting price of this house.
true_value: the true value of the house.
desc: a long description of this house, used to align with the bidders' persona.
</pre>
Please find a list of houses to choose from in `data/houses_pool.jsonl`.
### Run Simulation
Confirm you have the bidder and houses configuration in `data` folder. In HARBOR's directory terminal
<pre>
export OPENAI_API_KEY="your openai key"
python3 run_auction.py --repeat 1 --threads 3 --profile --strategy --folder data
</pre>
### Acknowledge
The implementation of HARBOR has built upon the great work of AucArena <url>https://github.com/jiangjiechen/auction-arena/tree/main</url>. Please visit their work if you wish to conduct more modifications.
