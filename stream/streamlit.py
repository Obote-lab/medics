import streamlit as st
import plotly.express as px
import pandas as pd 
import os 
import warnings
warnings.filterwarnings('ignore')
import plotly.figure_factory as ff
from streamlit_option_menu import option_menu
from numerize.numerize import numerize


# setting the page title/icon etc
st.set_page_config(page_title = "Health Facilities Services", page_icon=":syringe:", layout='wide')
# image
st.image(r"C:\Users\opote\Desktop\final project\final\geofinal\stream\data\istockphoto-1142386936-612x612.jpg", caption="The World of Data Analytics")
# setting the heading of the web page
st.title(":hospital:  Health Facilities Services in Homa Bay County")
# pushing the heading to the right position
st.markdown('<style>div.block-container{padding-top: 1rem;}</style>', unsafe_allow_html=True)


# user browse and upload file
fl = st.file_uploader(":file_folder: Upload Your File", type=(["csv","txt","xlsx","xlx","json","shp","pdf","kml"]))
if fl is not None:
	filename = fl.name
	st.write(filename)
	df = pd.read_csv(filename, encoding = "ISO-8859-1")

else:
	os.chdir(r"C:\Users\opote\Desktop\final_project\geofinal\geofinal\stream\data")
	df = pd.read_csv(r"combined_health_facilities.csv", encoding = "ISO-8859-1")


st.sidebar.image(r"C:\Users\opote\Desktop\final project\final\geofinal\stream\data\istockphoto-1222192727-612x612.jpg", caption="Web Data Representation")

# picking date
col1, col2 = st.columns((2))
df['date launched'] = pd.to_datetime(df['date launched'])

# getting the min and max dates
startDate = pd.to_datetime(df['date launched']).min()
endDate = pd.to_datetime(df['date launched']).max()
with col1:
	date1 = pd.to_datetime(st.date_input("Start Date(Launched Earliest)", startDate))

with col2:
	date2 = pd.to_datetime(st.date_input("Start Date(Launched Latest)", endDate))
# filtering the data
df = df[(df["date launched"] >= date1) & (df["date launched"] <= date2)].copy()


# making a side bar with filtering techniques
st.sidebar.header("Choose Your Filter: ")
# create for the constituencies
Constituency = st.sidebar.multiselect("Pick Your Constituency", df['constituency'].unique())
if not Constituency:
	df2 = df.copy()
else:
	df2 = df[df['constituency'].isin(Constituency)]

# create for sub_counties
sub_co = st.sidebar.multiselect("Pick Your Sub_County", df2['sub_county'].unique())
if not sub_co:
	df3= df2.copy()
else:
	df3 = df2[df2['sub_county'].isin(sub_co)]

# create for division
div  = st.sidebar.multiselect("Select Your Division", df3['division'].unique())
# filter the data based on Contituency, sub county and division
if not Constituency and not sub_co and not div:
	filtered_df = df
elif not sub_co and not div:
	filtered_df = df[df['constituency'].isin(Constituency)]
elif not Constituency and not div:
	filtered_df = df[df['sub_county'].isin(sub_co)]
elif sub_co and div:
	filtered_df = df3[df['sub_county'].isin(sub_co) & df3['division'].isin(div)]
elif Constituency and div:
	filtered_df = df3[df['constituency'].isin(Constituency) & df3['division'].isin(div)]
elif Constituency and sub_co:
	filtered_df = df3[df['constituency'].isin(Constituency) & df3['sub_county'].isin(sub_co)]
elif div:
	filtered_df = df3[df3['division'].isin(div)]
else:
	filtered_df = df3[df3['constituency'].isin(Constituency) & df3['sub_county'].isin(sub_co) & df3['division'].isin(div)]

# creation of of a column chart for category and Constituency
category_df = filtered_df.groupby(by=['categories'], as_index = False)['Beds'].sum()

with col1:
	st.subheader("Hospital Categories")
	fig = px.bar(category_df, x = 'categories', y = "Beds", text = ['Beds {:,.0f}'.format(x) for x in category_df['Beds']],
		template="seaborn")
	st.plotly_chart(fig,use_container_width=True, height=200)

with col2:
	st.subheader("No.of Beds/Keph Level per Constituency")
	fig = px.pie(filtered_df, values='Beds', names = 'constituency', hole=0.5)
	fig.update_traces(text=filtered_df['Keph level'], textposition='inside')
	st.plotly_chart(fig,use_container_width=True)

# the actual data
cl1, cl2 = st.columns(2)

with cl1:
	with st.expander("Hospital Categories ViewData"):
		st.image(r"C:\Users\opote\Desktop\final project\final\geofinal\stream\data\istockphoto-1295180758-612x612.jpg",caption="The Total Number of Beds per Category")
		st.write(category_df.style.background_gradient(cmap="Blues"))
		csv = category_df.to_csv(index = False).encode('utf-8')
		st.download_button("Download Data", data = csv, file_name = "Hospital Categories.csv",mime="text/csv",
                            help = "Click here to Download the Data as a CSV file")

with cl2:
	with st.expander("Beds per Constituency ViewData"):
		st.image(r"C:\Users\opote\Desktop\final project\final\geofinal\stream\data\istockphoto-1327568875-612x612.jpg",caption="Data Analytics on the Number of Beds per Constituency")
		Constituency = filtered_df.groupby(by='constituency', as_index=False)['Beds'].sum()
		st.write(Constituency.style.background_gradient(cmap="Greens"))
		csv = Constituency.to_csv(index = False).encode('utf-8')
		st.download_button("Download Data", data = csv, file_name = "Hospital Beds per Constituency.csv",mime="text/csv",
                            help = "Click here to Download the Data as a CSV file")

# visualizing the data based on time series
filtered_df['month_year'] = filtered_df['date launched'].dt.to_period("M")
st.subheader("Time Series Analysis")

linechart = pd.DataFrame(filtered_df.groupby(filtered_df['month_year'].dt.strftime('%Y : %b'))['Cots'].sum()).reset_index()
fig2 = px.line(linechart, x='month_year',y='Cots', labels={'Cots':'Number'}, height=500, width=1000, template='gridon')
st.plotly_chart(fig2, use_container_width=True)

with st.expander("ViewData for Time Series: "):
	st.write(linechart.T.style.background_gradient(cmap='Oranges'))
	csv = linechart.to_csv(index=False).encode("utf-8")
	st.download_button('Download Data', data=csv,file_name='Time Series.csv', mime='text/csv')

# creation of a treemap based on Constituency , category and Beds
st.subheader("Hierachical View of Hospitals based on operation Authority")
fig3 = px.treemap(filtered_df,path=['Regulatory body','categories','constituency'],values='Beds', hover_data=['Cots'],color='constituency')
fig3.update_layout(width=800, height=650)
st.plotly_chart(fig3, use_container_width=True)

chart1, chart2 =  st.columns((2))
with chart1:
	st.subheader("Beds per Keph Level")
	fig = px.pie(filtered_df, values='Beds', names = 'Keph level', template='plotly_dark')
	fig.update_traces(text=filtered_df['Keph level'], textposition='inside')
	st.plotly_chart(fig, use_container_width=True)

with chart2:
	st.subheader("Beds per Constituency")
	fig = px.pie(filtered_df, values='Beds', names = 'constituency', template='gridon')
	fig.update_traces(text=filtered_df['constituency'], textposition='inside')
	st.plotly_chart(fig, use_container_width=True)
# creating of table
st.subheader(":point_right: Sample Table of important spatial data")
with st.expander("Summary Table"):
	df_sample = df[0:15][['Code','Name','Keph level','Ward','latitude', 'longitude']]
	fig = ff.create_table(df_sample, colorscale="viridis")
	st.plotly_chart(fig, use_container_width=True)

	st.markdown("Month Wise launch Constituency Table")
	filtered_df['month'] = filtered_df['date launched'].dt.month_name()
	category_yr = pd.pivot_table(data = filtered_df, values='Cots', index=['Regulatory body'], columns="month")
	st.write(category_yr.style.background_gradient(cmap='Reds'))

# create scatter plot
data1 = px.scatter(filtered_df, x='Beds', y='Cots',size = "Code")
data1['layout'].update(title= "Relationship btw Beds And Cots Using Scatter Plot", 
									titlefont=dict(size=20),xaxis=dict(title='Beds',titlefont=dict(size=15)),
									yaxis=dict(title="Cots",titlefont=dict(size=19)))

st.plotly_chart(data1, use_container_width=True)

with st.expander("ViewData"):
	st.image(r"C:\Users\opote\Desktop\final project\final\geofinal\stream\data\istockphoto-700664792-612x612.jpg",caption="Hey User!! You can Download The Entire Dataset By just a Click on the Button Bellow")
	st.write(filtered_df.iloc[:250,1:50:2].style.background_gradient(cmap='gist_earth_r'))
# Dowload the original dataset
csv = df.to_csv(index=False).encode('utf-8')
st.download_button('Download Entire Dataset', data=csv, file_name="Whole Dataset.csv", mime='text/csv')