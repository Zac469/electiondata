🗳️ Election Data Collection 🇦🇺
🎯 Rationale
This project is focused on collecting and tracking election data up until Election Day in late May 2025. The file will include:

Scrapes of Wikipedia polling data
Snowflake data loads
Streamlit app code to publish and share the results
The purpose of this project is to understand how Australia's electoral system works. By gathering and analyzing this data, we will be able to simulate potential election outcomes and explore how different factors might influence the results.

🏛️ Electoral Structure
🏠 House of Representatives (Lower House)
151 electorates, each electing one member.
🏛️ Senate (Upper House)
Each state elects 6 Senators (or 12 in a double dissolution), and each territory elects 2 Senators.

✅ House of Representatives – Preferential Voting
Each voter ranks candidates in order of preference (1, 2, 3, etc.). To win, a candidate must secure more than 50% of the vote. If no candidate reaches this, the lowest-ranked candidate is eliminated, and their votes are transferred to the next preference. This continues until a candidate reaches a majority.
Example Count
First-preference votes are counted.
If no one has 50%, the lowest candidate is eliminated, and their votes are redistributed.
This repeats until a candidate secures a majority.

🗳️ Senate – Proportional Representation
The Senate uses a quota-based system. To win a seat, a candidate must reach a quota.
Voting Options:
Vote Above the Line (ATL): Select at least 6 parties.
Vote Below the Line (BTL): Select at least 12 individual candidates.
Example Count:
First-preference votes are counted.
If a candidate reaches the quota, they are elected. Any surplus votes are distributed proportionally.
The lowest-ranked candidates are eliminated, and votes are transferred.
This process continues until all seats are filled.

Other useful predictors
https://au.yougov.com/elections/au/2025
https://www.pollbludger.net/fed2025/Overview.htm?
