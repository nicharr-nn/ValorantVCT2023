# VALORANT Champions Tour 2023 Player Performance
VALORANT is a free-to-play first-person 5v5 character-based tactical FPS tactical hero shooter developed and published by Riot Games. This project is a comprehensive tool for analyzing VALORANT player performance in the VALORANT Champions Tour 2023 (VCT2023). It allows users to analyze player statistics and match performance to gain a deeper understanding of the player's strengths, weaknesses, and contributions to their team's success.

## Data Sources
https://www.kaggle.com/datasets/vkay616/valorant-vct-2023-player-performance

(I edited the data in column CL (clutch won/lost), which the owner of this dataset wrote by using "/". This caused Excel to interpret it as a date. So, I edited it to be normal text and changed "/" to ":")

## Python Version
Requires Python >= 3.10

## Current Features
- Display player statistics table
- Display graphs (bar, pie, histogram, and boxplot) based on user input

## How to run the application
1. Clone the repository
2. Install the required packages by running the following command in the terminal:
```bash
pip install -r requirements.txt
```
3. Run the application by executing the following command:
```bash
python main.py
```