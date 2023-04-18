#!/usr/bin/env python
# coding: utf-8

# In[28]:


from pyvis.network import Network
import pandas as pd


# In[29]:


path = "/Users/stephanielin/Desktop/TLTLab/"


# In[30]:


keyword_category = pd.read_excel( "assets/dictionary 2.0.xlsx",index_col=0).iloc[:,0:1]


# In[31]:


keywords = pd.read_excel("assets/dictionary 2.0.xlsx")["traget n-gram"].tolist()


# In[32]:


positive_file_names_2021 = ['Student1_Positive_SA','Student2_Positive_SA','Student3_Positive_SA','Student4_Positive_SA','Student5_Positive_SA','Student6_Positive_SA','Student7_Positive_SA']
year2021_df = []
for i in range(len(positive_file_names_2021)):
    temp_df = pd.read_csv("Sentiment_Map/Positive_Map/2021/"+positive_file_names_2021[i]+".csv",index_col=0)
    temp_df.reset_index(drop=True, inplace=True)
    year2021_df.append(temp_df)


# In[33]:


student_names_2021 = ['Student1','Student2','Student3','Student4','Student5','Student6','Student7']


# In[34]:


positive_file_names_2022 = ['Student1_Positive_SA','Student2_Positive_SA','Student3_Positive_SA','Student4_Positive_SA','Student5_Positive_SA','Student6_Positive_SA','Student7_Positive_SA','Student8_Positive_SA','Student9_Positive_SA','Student10_Positive_SA','Student11_Positive_SA','Student12_Positive_SA']
year2022_df = []
for i in range(len(positive_file_names_2022)):
    temp_df = pd.read_csv("Sentiment_Map/Positive_Map/2022/"+positive_file_names_2022[i]+".csv",index_col=0)
    temp_df.reset_index(drop=True, inplace=True)
    year2022_df.append(temp_df)


# In[35]:


student_names_2022 = ['Student1','Student2','Student3','Student4','Student5','Student6','Student7','Student8','Student9','Student10','Student11','Student12']


# In[36]:


positive_file_names_2023 = ['Student1_Positive_SA','Student2_Positive_SA','Student3_Positive_SA','Student4_Positive_SA','Student5_Positive_SA','Student6_Positive_SA','Student7_Positive_SA','Student8_Positive_SA','Student9_Positive_SA','Student10_Positive_SA','Student11_Positive_SA','Student12_Positive_SA']
year2023_df = []
for i in range(len(positive_file_names_2023)):
    temp_df = pd.read_csv("Sentiment_Map/Positive_Map/2023/"+positive_file_names_2023[i]+".csv",index_col=0)
    temp_df.reset_index(drop=True, inplace=True)
    year2023_df.append(temp_df)


# In[37]:


student_names_2023 = ['Eury','Sadia','Helen','Xichen','Zhanlan','Katie','Andrea','Ana Maria','Heidi','Mariana','Inara','Kiki']


# In[38]:


# the number shows which category the keyword belongs to
keywords_group = keyword_category.iloc[:, 0].to_numpy()


# In[39]:


category_color = []
for i in keywords_group:
    if i == 1:
        category_color.append('#e3342f')
    if i == 2:
        category_color.append('#f6993f')
    if i == 3:
        category_color.append('#ffed4a')
    if i == 4:
        category_color.append('#38c172')
    if i == 5:
        category_color.append('#4dc0b5')
    if i == 6:
        category_color.append('#3490dc')
    if i == 7:
        category_color.append('#6574cd')
    if i == 8:
        category_color.append('#9561e2')
    if i == 9:
        category_color.append('#f66d9b')


# In[40]:


def class_collective_positive_sensitive_map(class_df, student_names_year):
    nets = []
    for i in range(class_df[0].shape[0]):
        net = Network(notebook=True)
        student_names = []
        occurence = []
        
        for n in range(len(keywords)):
            student_names.append([])
            occurence.append(0)
        for number, student_df in enumerate(class_df):
            for s, value in enumerate(student_df.iloc[i]):
                if value == 1:
                    #student_names[s].append("student"+str(number+1))
                    student_names[s].append(student_names_year[number])
            occurence = [sum(x) for x in zip(occurence, student_df.iloc[i])]
        for student_df in class_df:
            for p, value in enumerate(student_df.iloc[i]):
                if value == 1:
                    net.add_node(p, label=keywords[p], title='unset',size=(int(occurence[p])+1)*3, color=category_color[p])
        
        # add names of student who use the knowledge to corresponding knowledge node's tittle in the map
        for node in net.nodes:
            node['title'] = ', '.join(student_names[int(node['id'])])
            
        net_id = [dic['id'] for dic in net.nodes]
        
        for o in net_id:
            for u in net_id:
                if o != u and keywords_group[o] == keywords_group[u]:
                    net.add_edge(o,u,hidden=True)
        
        net.repulsion(central_gravity=0.9,spring_length=50)
        
        nets.append(net)
    
    return nets


# In[41]:


class_positive_map_2021 = class_collective_positive_sensitive_map(year2021_df,student_names_2021)
class_positive_map_2022 = class_collective_positive_sensitive_map(year2022_df,student_names_2022)
class_positive_map_2023 = class_collective_positive_sensitive_map(year2023_df,student_names_2023)


# In[42]:


class_positive_map_2023[0].show("social_network.html")

for i in range(len(class_positive_map_2023)):
    class_positive_map_2023[i].show(f"assets/class_positive_map_2023_{i+1}.html")
# In[ ]:




