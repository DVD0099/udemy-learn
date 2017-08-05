
# coding: utf-8

# In[29]:

from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

ticker=input("Enter a ticker symbol: ")

start_entry=input("Enter a start date in YYYY-MM-DD: ")
year,month,day=map(int,start_entry.split("-"))
start=datetime.date(year,month,day)

end_entry=input("Enter a end date in YYYY-MM-DD: ")
year2,month2,day2=map(int,end_entry.split("-"))
end=datetime.date(year2,month2,day2)

#end_entry=input("Enter ")

#start=datetime.datetime(2012,11,1)
#end=datetime.datetime(2017,5,10)

df=data.DataReader(name=ticker,data_source="google",start=start,end=end)


def inc_dec(c,o):
    if c > o:
        value="Increase"
    elif c < o:
        value = "Decrease"
    else:
        value="Equal"
    return value

df["Status"]=[inc_dec(c,o) for c, o in zip(df.Close,df.Open)]

df["Middle"]=abs((df.Open+df.Close)/2)
df["Height"]=abs((df.Close-df.Open))
df["Ticker"]="GOOG"


p=figure(x_axis_type='datetime', width=1000,height=300,responsive=True)
p.title.text="Candlestick Chart"
p.grid.grid_line_alpha=0.3

hours_12=12*60*60*1000

p.segment(df.index,df.High,df.index,df.Low,line_color="black")

p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"],
       hours_12,df.Height[df.Status=="Increase"],fill_color="#32CD32",line_color="black")

p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"],
       hours_12,df.Height[df.Status=="Decrease"],fill_color="#FF3333",line_color="black")

script1, div1 = components(p) #tuple that has length of 2
cdn_js=CDN.js_files
cdn_css=CDN.css_files

output_file("CS.html")
show(p)


# In[31]:

#cdn_js


# In[32]:

#cdn_css
