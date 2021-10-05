## Data analysis of Spotify data in Quick Sight
The idea behind this project is to collect Spotify data every week, which will make possible to perform analysis that will take into account changes throughout the time. Naturally, at this stage it is impossible to do, so I performed analysis for one week only (week 39, 2021) at the moment of working on this project. When more data is accumulated, time dimension can be introduced.

### Mode: major or minor?
First thing I checked whether some countries' charts are occupied by song in major or minor mode. I created a barplot showing count of parameter mode per country. Because mode is either 1 for major or 0 for minor, sum(mode) is easy to interpret. Turns out, countries that have major songs dominating chart are primarily from Asia: among top 10 major-dominated charts, 9 are from  East and South-East Asia, and 10th being Iceland. These countries have 37-41 songs in major mode (out of 50). Bottom 10 countries group has 8 european countries, plus South Africa and Israel. Bottom entry belongs to Turkey - clear outlier, with only 10 songs in major mode - very dominated by minor mode music. One country (Poland) had only 43 tracks in chart - in the future there needs to be a check implemented in the Spotify API calls to control that there are always 50 songs in chart.

<img src="https://github.com/ksenia-tabakova/spotify_project/blob/main/DataAnalysis/sum_of_mode_by_country.png" width="600">

### Mode vs Danceability
To further investigate tendency with major and minor mode, I made a scatterplot of mode vs median danceability grouped by country. It revealed interesting details. It appears that countries can be divided for three groups:  
- Countries with many major songs: medium danceability descreases the more major songs are in the chart. This hints us, that music that people like to listen to there is more cheerful but not necessarily the best for dancing.
- Countries with few major songs: more major songs increase danceability. This can indicate that major songs tend to be dance songs.
- Other countries that don't show any connection between.  
- 
<img src="https://github.com/ksenia-tabakova/spotify_project/blob/main/DataAnalysis/Mode-vs-danceability-per-country.png" width="600">

### Mean tempo vs position

On the average, top 3 songs have higher tempo than any other positions (10-15 BPM higher than closest entry is at the position 7). On average people in the selected for analysis countries streamed greater tempo songs.

<img src="https://github.com/ksenia-tabakova/spotify_project/blob/main/DataAnalysis/average-tempo-by-position.png" width="600">

### Geographic distribution of valence
Spotify provides interesting metric on valence - a measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry). Map showing median valence gives insights into geographic distribution of this metric. Latino world together with Spain generally have higher median valence values, with Brazil clearly standing out with highest median valence. South-East Asia, USA and South Africa form group of countries with lower median valence. Rest of the countries are somewhere in ebtween.


## Future work
- Once time dimension will be added, it will be possible to track how studied parameters change from week to week, from season to season and so on. 
- More countries should be included into analysis - current set lacks true representativeness of music preferences across the globe.
