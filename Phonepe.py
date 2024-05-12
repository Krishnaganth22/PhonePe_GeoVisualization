import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import json 
import os 
import git
import mysql.connector
import plotly.express as px

#Cloning the Phonepe Github data and getting datas in jason format

#Aggregate transaction 
path='C:/Users/sankara subramanian/Desktop/Krishna/Youtube_data/Phonepe_visual/pulse/data/aggregated/transaction/country/india/state/'
agg_trans_list=os.listdir(path)


data1={'State':[],'Year':[],'Quarter':[],'Transaction_type':[],'Transaction_count':[],'Transaction_amount':[]}

for i in agg_trans_list:
    path_i=path+i+"/"
    agg_year=os.listdir(path_i)
    for j in agg_year:
        path_j=path_i+j+"/"
        quart=os.listdir(path_j)
        for k in quart:
            path_k=path_j+k
            json_open=open(path_k,'r')
            Data=json.load(json_open)
            for a in Data['data']['transactionData']:
          
                Name=a['name']
                count=a['paymentInstruments'][0]['count']
                amount=a['paymentInstruments'][0]['amount']
                data1['State'].append(i)
                data1['Year'].append(j)
                data1['Quarter'].append(int(k.strip('.json')))
                data1['Transaction_type'].append(Name)
                data1['Transaction_count'].append(count)
                data1['Transaction_amount'].append(amount)
Final_Trans_data=pd.DataFrame(data1)
Final_Trans_data['State']=Final_Trans_data['State'].str.replace('Andaman-&-nicobar-islands','Andaman & Nicobar')
Final_Trans_data['State']=Final_Trans_data['State'].str.replace('-',' ')
Final_Trans_data["State"]=Final_Trans_data['State'].str.title()

#Aggregate users
path='C:/Users/sankara subramanian/Desktop/Krishna/Youtube_data/Phonepe_visual/pulse/data/aggregated/user/country/india/state/'
agg_user_list=os.listdir(path)


data2={'State':[],'Year':[],'Quarter':[],'Brands':[],'Transaction_count':[],'Percentage':[]}

for i in agg_user_list:
    path_i=path+i+'/'
    year=os.listdir(path_i)
    for j in year:
        path_j=path_i+j+'/'
        quarters=os.listdir(path_j)
        for k in quarters:
            path_k=path_j+k
            view=open(path_k,'r')
            try:
                opening=json.load(view)
                for  a in opening['data']["usersByDevice"]:
                    brand=a['brand']
                    count=a['count']
                    percent=a['percentage']
                    data2['State'].append(i)
                    data2['Year'].append(j)                                   
                    data2['Brands'].append(brand)
                    data2['Transaction_count'].append(count)
                    data2['Percentage'].append(percent)
                    data2['Quarter'].append(int(k.strip(".json")))
            except:
                pass 
        
Final_user_data=pd.DataFrame(data2)
Final_user_data['State']=Final_user_data['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
Final_user_data['State']=Final_user_data['State'].str.replace('-',' ')
Final_user_data['State']=Final_user_data['State'].str.title()

#Map Transaction data   
path='C:/Users/sankara subramanian/Desktop/Krishna/Youtube_data/Phonepe_visual/pulse/data/map/transaction/hover/country/india/state/'
map_trans_list=os.listdir(path)


data3={'State':[],'Year':[],'Quarter':[],'District':[],'Transaction_Count':[],'Transaction_amount':[]}

for i in map_trans_list:
    path_i=path+i+'/'
    year=os.listdir(path_i)
    for j in year:
        path_j=path_i+j+'/'
        file=os.listdir(path_j)
        for k in file:
            path_k=path_j+k
            view=open(path_k,'r')
            opening=json.load(view)            
            for a in opening['data']['hoverDataList']:
                Name=a['name']
                count=a['metric'][0]['count']
                amount=a['metric'][0]['amount']
                data3['State'].append(i)
                data3['Year'].append(j)
                data3['Quarter'].append(k.strip('.json'))
                data3['District'].append(Name)
                data3['Transaction_Count'].append(count)
                data3['Transaction_amount'].append(amount)
               
Final_map_data=pd.DataFrame(data3)
Final_map_data['State']=Final_map_data['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
Final_map_data['State']=Final_map_data['State'].str.replace('-',' ')
Final_map_data['State']=Final_map_data['State'].str.title()
Final_map_data['District']=Final_map_data['District'].str.title()

#Map user Data
path='C:/Users/sankara subramanian/Desktop/Krishna/Youtube_data/Phonepe_visual/pulse/data/map/user/hover/country/india/state/'
map_user_list=os.listdir(path)



data4={'State':[],'Year':[],'Quarter':[],'District':[],'Registred_user':[],'App_opens':[]}
for i in map_user_list:
    path_i=path+i+'/'
    year=os.listdir(path_i)
    for j in year:
        path_j=path_i+j+'/'
        file=os.listdir(path_j)
        for k in file:
            path_k=path_j+k
            view=open(path_k,'r')
            opening=json.load(view)            
            for a in opening['data']['hoverData'].items():
                Name=a[0]
                users=a[1]['registeredUsers']
                opens=a[1]['appOpens']
                data4['State'].append(i)
                data4['Year'].append(j)
                data4['Quarter'].append(k.strip('.json'))
                data4['District'].append(Name)
                data4['Registred_user'].append(users)
                data4['App_opens'].append(opens)
map_user_data=pd.DataFrame(data4)
map_user_data['State']=map_user_data['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
map_user_data['State']=map_user_data['State'].str.replace('-',' ')
map_user_data['State']=map_user_data['State'].str.title()
map_user_data['District']=map_user_data['District'].str.title()


#Top Transaction data
            
path='C:/Users/sankara subramanian/Desktop/Krishna/Youtube_data/Phonepe_visual/pulse/data/top/transaction/country/india/state/'
top_trans_list=os.listdir(path)



data5={'State':[],'Year':[],'Quarter':[],'Pincodes':[],'Transaction_count':[],'Transaction_amount':[]}
for i in top_trans_list:
    path_i=path+i+'/'
    year=os.listdir(path_i)
    for j in year:
        path_j=path_i+j+'/'
        file=os.listdir(path_j)
        for k in file:
            path_k=path_j+k
            view=open(path_k,'r')
            opening=json.load(view)            
            for a in opening['data']['pincodes']:
                pin=a['entityName']
                count=a['metric']['count']
                amount=a['metric']['amount']
                data5['State'].append(i)
                data5['Year'].append(j)
                data5['Quarter'].append(k.strip('.json'))
                data5['Pincodes'].append(pin)
                data5['Transaction_count'].append(count)
                data5['Transaction_amount'].append(amount)
Final_top_data=pd.DataFrame(data5)
Final_top_data['State']=Final_top_data['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
Final_top_data['State']=Final_top_data['State'].str.replace('-',' ')
Final_top_data['State']=Final_top_data['State'].str.title()

#Top user Data
path='C:/Users/sankara subramanian/Desktop/Krishna/Youtube_data/Phonepe_visual/pulse/data/top/user/country/india/state/'
top_user_list=os.listdir(path)



data6={'State':[],'Year':[],'Quarter':[],'Pincodes':[],'Registered_users':[]}
for i in top_user_list:
    path_i=path+i+'/'
    year=os.listdir(path_i)
    for j in year:
        path_j=path_i+j+'/'
        file=os.listdir(path_j)
        for k in file:
            path_k=path_j+k
            view=open(path_k,'r')
            opening=json.load(view)            
            for a in opening['data']['pincodes']:
                pin=a['name']
                users=a['registeredUsers']               
                data6['State'].append(i)
                data6['Year'].append(j)
                data6['Quarter'].append(k.strip('.json'))
                data6['Pincodes'].append(pin)
                data6['Registered_users'].append(users)
           
Top_user_data=pd.DataFrame(data6)
Top_user_data['State']=Top_user_data['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
Top_user_data['State']=Top_user_data['State'].str.replace('-',' ')
Top_user_data['State']=Top_user_data['State'].str.title()





#Sql set up
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='Phonepe'
    )
mycursor=mydb.cursor(buffered=True)

#Dashboard Configuration
st.set_page_config(page_title='Phonepe Pulse Visualization',page_icon=':phone:',layout='wide',initial_sidebar_state='expanded')
st.sidebar.image("https://storiesflistgv2.blob.core.windows.net/stories/2017/06/phonepe_mainbanner2.jpg")
st.sidebar.header(":white[Phonepe Pulse]")

#Setting side bar options to access the app
with st.sidebar:
    selected= option_menu(None,['Home','Explore',"Data Visualization",'Insights'],
                        icons=['house','graph-up-arrow','bar-chart-line','exclamation-circle'],
                        default_index=0,
                        orientation='vertical',
                        styles={"nav-link": {"font-size": "15px", "text-align": "centre", "margin": "2px",
                                                "--hover-color": "#6739b7"},
                                   "icon": {"font-size": "20px"},
                                  "nav-link-selected": {"background-color": "#6739b7"}})
    
#If Home is selected it displays the usage of the app
if selected == "Home":
    st.sidebar.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*w-wizVCoOO_xSiKgv4hjZQ.gif", width=295)

    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEvbmVAQ6q_9-BLqG990Ag4sB6L7cJIZ5UNw&usqp=CAU", width=250)


    st.title(" :violet[Phonepe Pulse Data Visualization and Exploration ]")
    st.markdown("## :violet[A User-Friendly Tool Using Streamlit and Plotly]")
    col1, col2 = st.columns([3, 2], gap="medium")
    with col1:
        st.write(' ')
        st.markdown('### :violet[Domain :]Fintech')
        st.markdown('''### :violet[Overview :] This app gives you a clear data about the transactions and brands around the nation. You can select the year and can visually see the data as pie charts and barcharts.Also goe-visualization is used to view map which shows data of every nook and corner of India.THANK YOU ''')
        phonepe='https://play.google.com/store/apps/details?id=com.phonepe.app&hl=en_IN&shortlink=2kk1w03o&c=consumer_app_icon&pid=PPWeb_app_download_page&af_xp=custom&source_caller=ui&pli=1'
        button=st.button('Download App')
        if button:
            st.markdown(f'Download [Phonepe App]({phonepe})')

    with col2:
        st.write(' ')
        st.write(' ')
        st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExb20ydHlvcmVwdmU1dHpvdWNja3M4N3VwYmo3a2xyYnI3c2h1dm0wOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KX5nwoDX97AtPvKBF6/giphy.gif", width=500)

#If Explore is selected could view the Top Transactions and Users
if selected=='Explore':
    options=range(2018,2024)
    Year=st.sidebar.selectbox(label=('**Year**'),options=options)
    Quarter=st.sidebar.slider(label='**Quarter**',min_value=1,max_value=4)
    Type=st.sidebar.selectbox(label='**Type**',options=('Transaction','Users'))
    column1,column2=st.columns([1,1.5],gap='large')

    with column1:
        st.image('https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3JpMDB3cWs5MGt1dDRibXJheTE3ZWN1b3o0d3BqMzFocGhxdjNveiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iicDrNGWxHmDrIni6j/giphy.gif')
    with column2:
        st.markdown('''
                    ### : Insights:
                    - Overall ranking of a particular Year and Quarter.
                    - Top 10 State, District based on Total number of transaction and Total amount spent on phonepe.
                    - Top 10 State, District based on Total phonepe users and their app opening frequency.
                    - Top 10 mobile brands and its percentage based on the how many people use phonepe.
                    ''')                
    if Type=='Transaction':
        coll1,coll2= st.columns([1.1,1.2],gap='medium')

        with coll1:
            st.markdown('### :violet[State]')
            mycursor.execute('''Select State,sum(Transaction_count) as Total_transaction_count ,sum(Transaction_amount) as Total_amount
                                FROM agg_trans where year = %s and quarter = %s group by State order by Total_amount desc limit 10''',(Year,Quarter))
            tab=mycursor.fetchall()
            df=pd.DataFrame(tab,columns=['State','Transaction_count','Transaction_amount'])
            chart1=px.pie(df,values='Transaction_amount',names='State',title='TOP 10 TRANSACTION AMOUNT ',
                        color_discrete_sequence=px.colors.sequential.Agsunset,
                        hover_data=['Transaction_count'],
                        labels={'Transaction_count':'Transaction_count'})
            chart1.update_traces(textposition='inside',textinfo='percent+label')
            st.plotly_chart(chart1,use_container_width=True)

           

            st.markdown('### :blue[Categories all over India]')
            mycursor.execute('''Select Transaction_type as Category,sum(Transaction_amount) as Total_amount from agg_trans
                            where year=%s and quarter=%s group by Transaction_type order by Total_amount DESC''',(Year,Quarter) )
            tab=mycursor.fetchall()
            df=pd.DataFrame(tab,columns=['Category','Total_amount'])
            st.table(df)
            

            


        with coll2:
            st.markdown('### :green[Districts]')
            mycursor.execute('''SELECT District, sum(Transaction_count) as Total_count, sum(Transaction_amount) as Total_amount from map_trans
                             WHERE year= %s and quarter= %s group by District order by Total_amount DESC limit 10''',(Year,Quarter))
            tab=mycursor.fetchall()
            df=pd.DataFrame(tab,columns=['Districts','Total_Count','Total_Amount'])
            chart2=px.pie(df,values='Total_Amount',names='Districts',title='TOP 10 DISTRICT-WISE TRANSACTION',
                          color_discrete_sequence=px.colors.sequential.Agsunset,
                          hover_data=['Total_Count'],
                          labels={'Total_Count':'Total_Count'})
            chart2.update_traces(textposition='inside',textinfo='percent+label')
            st.plotly_chart(chart2,use_container_width=True)

            st.markdown(':violet[Top10 data Pin wise]')
            mycursor.execute('''SELECT state,Pincodes,Transaction_amount from top_trans_pin where year=%s and Quarter=%s 
                                group by state order by Transaction_amount DESC limit 10''',(Year,Quarter))
            df=pd.DataFrame(mycursor.fetchall(),columns=['State','Pincodes','Transaction_amount'])
            st.table(df)
    if Type=='Users':
        coll1,coll2,coll3=st.columns([0.7,0.9,1],gap='medium')
        with coll1:
            st.markdown(':violet[Brands bar chart]')
            if Year ==2023 and Quarter in [1,2,3,4]:
                st.markdown('SORRY! No data to display')
            elif Year==2022 and Quarter in [2,3,4]:
                st.markdown('SORRY1 No data to display')
            else:
                mycursor.execute('''Select Brands,SUM(Transaction_count) as Count, AVG(Percentage)*100 as Percentage
                                 FROM agg_user where Year = %s and Quarter = %s group by Brands order by Count Desc limit 10''',(Year,Quarter))
                tab=mycursor.fetchall()
                df=pd.DataFrame(tab,columns=['Brands','Count','AVG_Percent'])
                chart=px.bar(df,title='TOP 10 BRANDS',orientation='h',x='Count',y='Brands',
                             color='AVG_Percent',color_discrete_sequence=px.colors.sequential.Agsunset)
                st.plotly_chart(chart,use_container_width=True)

            st.markdown(':violet[Brands pie chart]')
            if Year ==2023 and Quarter in[1,2,3,4]:
                st.markdown('SORRY! No data to display')
            elif Year ==2022 and Quarter in[2,3,4]:
                st.markdown('SORRY! No data to display')
            else:
                mycursor.execute('''Select Brands,SUM(Transaction_count) as Count, Percentage*100 as Percentage
                                 FROM agg_user where Year = %s and Quarter = %s group by Brands order by Count Desc limit 10''',(Year,Quarter))
                tab=mycursor.fetchall()
                df=pd.DataFrame(tab,columns=['Brands','Count','Percentage'])
                chart=px.pie(df,title='BRANDS COUNT AND PERCENT ',names='Brands',values='Count',hover_data='Percentage',
                             width=500,hole=0.5,color_discrete_sequence=px.colors.sequential.Agsunset)
                st.plotly_chart(chart)

            
        with coll2:
            st.markdown(':violet[District]')
            mycursor.execute('''Select District, Registred_user, App_opens from map_user where Year=%s and Quarter= %s group by District
                             order by Registred_user DESC limit 10''',(Year,Quarter))  
            tab=mycursor.fetchall()
            df=pd.DataFrame(tab,columns=['District','Registred_user','App_opens'])
            df.Registred_user=df.Registred_user.astype(float)

            chart=px.bar(df,title='TOP 10 USERS DISTRICT WISE ',x='Registred_user',y='District',orientation='h',color='Registred_user',
                         color_continuous_scale=px.colors.sequential.Mint)
            st.plotly_chart(chart)
        
        with coll3:
            st.markdown(':violet[STATE]')
            mycursor.execute('''Select state,sum(Registred_user) as Total_users,sum(App_opens) as Total_APP_OPENS from map_user
                             where Year=%s and Quarter=%s group by state order by Total_users DESC limit 10 ''',(Year,Quarter))
            tab=mycursor.fetchall()
            df=pd.DataFrame(tab,columns=['State','Total_users','Total_APP_OPENS'])
            fig=px.pie(df,values='Total_users',names='State',title='TOP 10 STATES',color_discrete_sequence=px.colors.sequential.Agsunset,
                       hover_data={'Total_APP_OPENS':'Total_APP_OPENS'})
            fig.update_traces(textposition='inside',textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)

#If Data Visualization is selected it shows the geovisualization maps for better understanding
if selected =='Data Visualization':
    options=range(2018,2024)
    Year=st.sidebar.selectbox(label=('**Year**'),options=options)
    Quarter=st.sidebar.slider(label='**Quarter**',min_value=1,max_value=4)
    Type=st.sidebar.selectbox(label='**Type**',options=('Transaction','Users'))
    column1,column2=st.columns(2)

    if Type== 'Transaction':
        with column1:
            st.markdown(':violet[Overall State-Transaction amount]')
            mycursor.execute('''Select State,sum(Transaction_amount) as Total_amount 
                            FROM map_trans where Year=%s and Quarter= %s group by state order by state ''',(Year,Quarter))
            df1=pd.DataFrame(mycursor.fetchall(),columns=['State','Total_amount'])
            df2=Final_map_data["State"].unique()
            df1.State=df2
            

            fig=px.choropleth(df1, 
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Total_amount',
                            color_continuous_scale='sunset'
                            )

            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig, use_container_width=True)
        
        with column2:
            st.markdown(':violet[Overall state- Transaction count]')
            mycursor.execute('''SELECT state,sum(Transaction_count) as Total_transaction from map_trans where Year=%s and Quarter=%s 
                             group by state order by Total_transaction desc''',(Year,Quarter))
            df1=pd.DataFrame(mycursor.fetchall(),columns=['State','Total_transaction'])
            
            df2=Final_map_data['State'].unique()
            df1.State=df2

            fig=px.choropleth(df1,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Total_transaction',
                            color_continuous_scale='sunset')
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig, use_container_width=True)

        st.markdown(":violet[Top Payment Type]")
        mycursor.execute(''' SELECT Transaction_type,sum(Transaction_count) as Total_count,sum(Transaction_amount) as Total_amount
                         FROM agg_trans where Year=%s and Quarter =%s group by Transaction_type order by Transaction_type''',(Year,Quarter))
        df=pd.DataFrame(mycursor.fetchall(),columns=['Transaction_type','Total_count','Total_amount'])

        plot=px.bar(df, x='Transaction_type',y='Total_count',title='Transaction type vs Total_transaction',
                    orientation='v',color='Transaction_type',color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(plot,use_container_width=False)

        st.markdown('# ')
        st.markdown('# ')
        st.markdown('# ')
        st.markdown('## :violet[Select State to explore] ')
        selected_state= st.selectbox('',('Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
                                        'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                                        'Dadra & Nagar Haveli & Daman & Diu', 'Delhi', 'Goa', 'Gujarat',
                                        'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand',
                                        'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh',
                                        'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland',
                                        'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim',
                                        'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                                        'Uttarakhand', 'West Bengal'),index=30)
        mycursor.execute('''SELECT state,year,quarter,district,sum(transaction_count) as Total_transaction,sum(Transaction_amount) as Total_Amount
                         FROM map_trans where year=%s and quarter=%s and State=%s group by State,District,Year,Quarter order by State, District''',(Year,Quarter,selected_state))
        df1=pd.DataFrame(mycursor.fetchall(),columns=['State','Year','Quarter','District','Total_transaction','Total_amount'])

        plot=px.bar(df1,title=selected_state,
                    x='Total_transaction',
                    y='District',
                    orientation='h',
                    color='Total_amount',
                    color_continuous_scale=px.colors.sequential.algae)
        st.plotly_chart(plot,use_container_width=True)

    if Type=='Users':
        st.markdown('## :violet[Overall state-Users app opening range]')
        mycursor.execute('''SELECT state,sum(Registred_user) as Total_users, sum(App_opens) as Total_App_opens from map_user
                         where year=%s and Quarter=%s group by State order by state''',(Year,Quarter))
        df1=pd.DataFrame(mycursor.fetchall(),columns=['State','Total_users','Total_App_opens'])
        df1.Total_App_opens = df1.Total_App_opens.astype(float)
        plot=px.choropleth(df1,
                           geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Total_App_opens',
                            color_continuous_scale='sunset')

        plot.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(plot, use_container_width=True)

        st.markdown('## :violet[Select any State to Explore]')
        selected_state=st.selectbox('',
                                    ('Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
                                        'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                                        'Dadra & Nagar Haveli & Daman & Diu', 'Delhi', 'Goa', 'Gujarat',
                                        'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand',
                                        'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh',
                                        'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland',
                                        'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim',
                                        'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                                        'Uttarakhand', 'West Bengal'),index=30)
        mycursor.execute('''SELECT state,year,quarter,district,sum(Registred_user) as Total_users,sum(App_opens) as Total_App_opens
                         FROM map_user where year=%s and quarter=%s and State=%s group by State,District,Year,Quarter order by State, District''',(Year,Quarter,selected_state))
        df1=pd.DataFrame(mycursor.fetchall(),columns=['State','Year','Quarter','District','Total_users','Total_App_opens'])

        plot=px.bar(df1,title=selected_state,x='Total_users',y='District',orientation='h',
                    color='Total_users',color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(plot,use_container_width=True)

# This gives user some 10 insights from the data
if selected=='Insights':

    st.markdown(':video[10 Insights from this data]')

    select_question=st.selectbox('Select to know important facts',
                                 ('1.Which state tops all over India in 2023 and what is the reason behind it?',
                                  '2.What is the most used transaction type in all over India in 2023 and its Amount?',
                                  '3.What are the top three brands used in India in 2018 vs 2021',
                                  '4.Which State and district has most number of users in 2018 vs 2023?',
                                  '5.Which state has more users in the year 2023?',
                                  '6.Which district in Tamilnadu has the highest transactions and Amount and the reason behind it?',
                                  '7.Which state tops in year 2022 in transactions and the district contribute the highest?',
                                  '8.Which state has a drastic growth in year last quarter of 2022 and What is its status in 2023?',
                                  '9.Which 3 districts shares a max users in Tamilnadu in 2023?',
                                  '10.Which is the brand which has low counts in 2022'))
    if select_question=='1.Which state tops all over India in 2023 and what is the reason behind it?':
        st.markdown('''Karnataka tops in all over India in 2023, it may be because of the new industries opened and more working people contributes more transaction
                    3.241376424 trillion of transaction amount!''')
        
    elif select_question=='2.What is the most used transaction type in all over India in 2023 and its Amount?':
        st.markdown('In 2023 Peer-to-peer payment type has the most number of Transaction amount. 15.9 Trillion of amount is the total transaction in 2023 via peer to peer type')

    elif select_question=='3.What are the top three brands used in India in 2018 vs 2021':
        st.markdown('''In 2018 Xiaomi,Samsung and Vivo has most number of users in all the quarters and in 2021 the same three brands but from Jul-Sep and Oct-Dec 
                    chech also:https://techobserver.in/news/gadget/vivo-overtakes-samsung-in-india-what-lies-ahead-for-smartphone-maker-2416, 
                    Sales of the Vivo V15 Pro account for 28 percent  of this sector of the market. These sales are a big part of the reason that Vivo has made such big gains in the overall market.''')

    elif select_question=='4.Which State and district has most number of users in 2018 vs 2023?':
        st.markdown(''' Bengaluru urban district in Karnataka  shares the most number of user about 1.6 crores in both 2018 and 2023, 
                    which shows that it is the electronic city so that many working people would contribute Phonepe Transactions''') 
    
    elif select_question=='5.Which state has more users in the year 2023':
        st.markdown('''Maharashtra registred more users in Year 2023 sharing 6.5 Crores in all quarters!''')

    elif select_question=='6.Which district in Tamilnadu has the highest transactions and Amount and the reason behind it?':
        st.markdown('''Chennai has the more number of transactions in Tamilnadu 84 billion amount and the reason behind it is the large 
                    population and the number of IT industries and Production companies were located which paves way for more employment!''')

    elif select_question=='7.Which state tops in year 2022 in transaction amount and the district contribute the highest?':
        st.markdown('''Telegana has highest transaction amount about 2.9 Trillion and the district contributes more is Rangareddy 191 million transaction Counts''')   

    elif select_question=='8.Which state has a drastic growth in year last quarter of 2022 and What is its status in 2023?':
        st.markdown('In 2022 last Quarter Karnataka has most number of Appopens and in 2023 the Appopens has reduced 1billion till last quarter of 2023')

    elif select_question=='9.Which 3 districts shares a max users in Tamilnadu in 2023':
        st.markdown(''' 1.Chennai- 3.2 million users,2.Thiruvallur -2.6 million and 3. Coimbatore- 2.27 million in 2023 in Tamilnadu!''')

    elif select_question=='10.Which is the brand which has lowest in Top 10 in 2022':
        st.markdown('Huawei is the last of top 10 because its spares were not available in India in wide, so its users were down in2022')
        
            

    





