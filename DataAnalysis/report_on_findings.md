## TBA
The idea behind this project is to collect Spotify data every week, which will make possible to perform analysis, including changes throughout the time. At the moment, it is impossible to do, so further analysis performed for one week only at the moment of working on this project. When more data is accumulated, time dimension can be introduced.
### Mode: major or minor?
First thing I checked whether some countries' charts are occupied by song in major or minor mode. I created a barplot showing count of parameter mode per country. Because mode is either 1 for major or 0 for minor, it is easy to understand and analyze. Turns out, countries that have major songs dominating chart are primarily from Asia: among top 10 major-dominated charts, 9 are from  East and South-East Asia, and 10th being Iceland: these countries have 37-41 songs in major mode (out of 50). Bottom 10 countries group has 8 european countries, plus South Africa and Israel. Bottom entry belongs to Turkey - clear outlier, with only 10 songs in major mode - very dominated by minor mode music.
### Mode vs Danceability
To further investigate tendency with major and minor mode, a scatterplot was created. It showed sum of mode vs median danceability, grouped by country. It revealed interesting details. It appears that countries can be divided for three groups:  
- Countries with many major songs: medium danceability descreases the more major songs are in the chart. This hints us, that music that people like to listen to there is more cheerful and not necessarily for dancing
- Countries with few major songs: more major songs increase danceability. This can indicate that major songs tend to be dance songs.
- other countries that don't necessarily have any connection between 
###
