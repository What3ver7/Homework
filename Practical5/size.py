 #Define population data for UK countries and Chinese provinces.
 #Sort the population data.
 #Define corresponding labels for each region.
 #Create a figure with two subplots (side by side).
 #Plot a pie chart for UK countries with labels and percentages.
 #Set the title for the UK pie chart.
 #Plot a pie chart for Chinese provinces with labels and percentages.
 #Set the title for the China pie chart.
 #Display the charts.import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
uk_countries=[57.11,3.13,1.91,5.45]
china_province=[65.77,41.88,45.28,61.27,85.15]
uk=sorted(uk_countries)
china=sorted(china_province)
uk_country=["Northern Ireland","Wales","Scotland","England"]
china_province=["Fujian","Jiangxi","Anhui","Zhejiang","Jiangsu"]
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.pie(uk,labels=uk_country,autopct="%1.2f%%")
ax1.set_title("UK Countries Distribution")
ax2.pie(china,labels=china_province,autopct="%1.2f%%")
ax2.set_title("China Province Distribution")
plt.show()