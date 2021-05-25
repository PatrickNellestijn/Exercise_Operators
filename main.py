# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
#vergelijking0
#spain_total_area = 505307
#switzerland_total_area = 41277
#print(spain_total_area > switzerland_total_area)

#vergelijking1_The language spoken the most in Switzerland is the same as in Spain
language_spoken_spain = "Castilian Spanish"
language_spoken_switzerland = "German"
print(language_spoken_spain == language_spoken_switzerland)
#vergelijking2_The most prevalent religion in Switzerland is the same as in Spain
prevalent_religion_spain = "Roman Catholic"
prevalent_religion_switserland = "Roman Catholic"
print(prevalent_religion_spain <= prevalent_religion_switserland)
#vergelijking3_The name length of Spain's capital does not equal that of Switzerland
capital_spain = "Madrid"
capital_switserland = "Bern"
len_cap_spain = len(capital_spain)
len_cap_switserland = len(capital_switserland)
print(len_cap_spain is not len_cap_switserland)
#vergelijking4_Switzerland's GDP is greater than Spain's GDP
gdp_spain = 1778000000000000
gdp_switserland = 580000000000
print(gdp_switserland > gdp_spain)
#vergelijking5_The population growth is less than 1% in Switzerland and Spain
population_growth_spain = 0.67
population_growth_switserland = 0.66
print((population_growth_spain < 1) and (population_growth_switserland < 1))
#vergelijking6_At least one of the two countries has a population count of over 10 million
population_spain = 50000000
population_switserland = 8400000
print((population_spain > 10000000) or (population_switserland > 10000000))
#vergelijking7_Exactly one of the two countries has a population count of over 10 million
population_spain = 50000000
population_switserland = 8400000
print((population_spain > 10000000) or (population_switserland > 10000000))
