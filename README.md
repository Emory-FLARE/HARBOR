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
{"name": "Bidder 1","trait": "Urban Dwellers","is_profiler": false, "use_external_reason":false,"model_name": "claude-3-5-sonnet-20241022","budget": 1000000,"desire": "maximize_profit","plan_strategy": "adaptive","temperature": 0,"overestimate_percent": 10,"correct_belief": true,"enable_learning": false,"persona": "You are a 29-year-old graphic designer earning $70,000 annually with $25,000 in savings, you are deeply drawn to the energy and convenience of urban living. You thrive in a bustling city environment where cultural experiences, dining options, and entertainment venues are just steps away. The vibrancy of city life fuels your creativity, making proximity to art galleries, music venues, and trendy cafés essential. You seek a home in a walkable neighborhood, ideally in the city center or near major transit hubs, ensuring easy access to work and leisure. Your lifestyle prioritizes connectivity, diversity, and the dynamic pulse of metropolitan living."}
</pre>
You can set 2~5 agents for containable performance, here are the usage of each field configuring an agent.
<pre>
name: the unique name for each bidder
trait: the tag 
</pre>
### Run Simulation

### 
