import pandas as pd
import json 
import os 
import git
import mysql.connector
from sqlalchemy import create_engine

#Data Cloning and Extraction and Insertion into My SQL database

!git clone https://github.com/PhonePe/pulse.git

path='C:/Users/sankara subramanian/Desktop/Krishna/Youtube_data/Phonepe_visual/pulse/data/aggregated/transaction/country/india/state/'
agg_trans_list=os.listdir(path)
agg_trans_list

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
Final_Trans_data


path='C:/Users/sankara subramanian/Desktop/Krishna/Youtube_data/Phonepe_visual/pulse/data/aggregated/user/country/india/state/'
agg_user_list=os.listdir(path)
agg_user_list

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
Final_user_data

    
path='C:/Users/sankara subramanian/Desktop/Krishna/Youtube_data/Phonepe_visual/pulse/data/map/transaction/hover/country/india/state/'
map_trans_list=os.listdir(path)
map_trans_list
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
Final_map_data.info()


            
path='C:/Users/sankara subramanian/Desktop/Krishna/Youtube_data/Phonepe_visual/pulse/data/map/user/hover/country/india/state/'
map_user_list=os.listdir(path)
map_user_list


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



path='C:/Users/sankara subramanian/Desktop/Krishna/Youtube_data/Phonepe_visual/pulse/data/top/transaction/country/india/state/'
top_trans_list=os.listdir(path)
top_trans_list


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
Final_top_data


path='C:/Users/sankara subramanian/Desktop/Krishna/Youtube_data/Phonepe_visual/pulse/data/top/user/country/india/state/'
top_user_list=os.listdir(path)
top_user_list


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
Top_user_data


mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='Phonepe'
    )
mycursor=mydb.cursor(buffered=True)

engine=create_engine('mysql+mysqlconnector://root:''@localhost/Phonepe')

table_1='''Create table if not exists agg_trans (
                                               State varchar(100),
                                               Year int,Quarter int,
                                               Transaction_type varchar(100),
                                               Transaction_count bigint,
                                               Transaction_amount bigint)'''
mycursor.execute(table_1)
mydb.commit()

Final_Trans_data.to_sql('agg_trans',con=engine,if_exists='append',index=False)

table2='''Create table if not exists agg_user (State varchar(100),
                                            Year int,
                                            Quarter int,
                                            Brands varchar(100),
                                            Transaction_count bigint,
                                            Percentage float)'''
mycursor.execute(table2)
mydb.commit()

Final_user_data.to_sql('agg_user',con=engine,if_exists='append',index=False)


table3='''Create table if not exists map_trans(State varchar(100),
                                            Year int,
                                            Quarter int,
                                            District varchar(100),
                                            Transaction_count bigint,
                                            Transaction_amount float)'''
mycursor.execute(table3)
mydb.commit()
Final_map_data.to_sql('map_trans',con=engine,if_exists='append',index=False)

table4='''Create table if not exists map_user (State varchar(100),
                                                Year int,
                                                Quarter int,
                                                District varchar(100),
                                                Registred_user bigint,
                                                App_opens bigint)'''
mycursor.execute(table4)
mydb.commit()

map_user_data.to_sql('map_user',con=engine,if_exists='append',index=False)

table5='''Create table if not exists top_trans_pin(State varchar(100),
                                                Year int,
                                                Quarter int,
                                                Pincodes bigint,
                                               Transaction_count bigint,
                                                Transaction_amount bigint)'''
mycursor.execute(table5)
mydb.commit()

Final_top_data.to_sql('top_trans_pin',con=engine,if_exists='append',index=False)


table6='''Create table if not exists top_user_pin(State varchar(100),
                                                Year int,
                                                Quarter int,
                                                Pincodes bigint,
                                                Registered_users bigint)'''
mycursor.execute(table6)
mydb.commit()

Top_user_data.to_sql('top_user_pin',con=engine,if_exists='append',index=False)
