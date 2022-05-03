#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/healthonrails/annolid/blob/main/docs/tutorials/Annolid_post_processing_distances.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# ## Calculate distances for a pair of instances in the same frame or the same instance across frames

# In[1]:


import pandas as pd
import numpy as np
from google.colab import data_table


# In[ ]:


get_ipython().system('pip install gradio')


# In[ ]:


import gradio as gr


# In[ ]:


data_table.enable_dataframe_formatter()


# In[1]:


CSV_FILE = '/content/mask_rcnn_tracking_results_with_segmenation.csv'


# In[ ]:


df = pd.read_csv(CSV_FILE)


# In[ ]:


df.head()


# ## Calculate the distance of a pair of instances in a given frame
# 
# ---

# In[ ]:


def paired_distance(frame_number,
                    this_instance='Female_98',
                    other_instance='Male_109'):
    df_dis = df[df["frame_number"]==frame_number][['cx','cy','instance_name']]
    df_this = df_dis[df_dis.instance_name == this_instance]
    df_other = df_dis[df_dis.instance_name == other_instance]
    try:
      dist = np.linalg.norm(df_this[['cx','cy']].values-df_other[['cx','cy']].values)
    except:
      dist = None


    return dist


# In[ ]:


paired_distance(0,'Female_98','Male_109')


# In[ ]:


instance_names = list(df.instance_name.unique())


# In[ ]:


iface = gr.Interface(paired_distance,
                     [
                         gr.inputs.Number(),
                         gr.inputs.Dropdown(instance_names),
                         gr.inputs.Dropdown(instance_names),

                     ],
                     [
                         gr.outputs.Label(label="Paired Distance"),
                     ]
                     )
iface.launch()


# ## Calculate the distance of the instance from the previous frame to the current frame

# In[ ]:


def instance_distance_between_frame(frame_number,
                                    instance_name='Female_86'):
    if frame_number < 1:
      return 0
    previous_frame_number = frame_number - 1
    df_dis = df[df["frame_number"]==frame_number][['cx','cy','instance_name']]
    df_dis_prev = df[df["frame_number"]==previous_frame_number][['cx','cy','instance_name']]
    df_dis = df_dis[df_dis.instance_name == instance_name]
    df_dis_prev = df_dis_prev[df_dis_prev.instance_name == instance_name]

    try:
      dist = np.linalg.norm(df_dis[['cx','cy']].values-df_dis_prev[['cx','cy']].values)
    except:
      dist = None
    
    return dist
    


# In[ ]:


df['dist_from_previous_frame_female_86'] = df.frame_number.apply(instance_distance_between_frame,instance_name='Female_86')


# In[ ]:


df['dist_from_previous_frame_female_86'].describe()


# ## The total distance traveled for instance female_86 in in pixels

# In[ ]:


df['dist_from_previous_frame_female_86'].sum()


# In[ ]:


df['dist_from_previous_frame_male_109']= df.frame_number.apply(instance_distance_between_frame, instance_name='Male_109')


# In[ ]:


df['dist_from_previous_frame_male_109'].sum()


# In[ ]:


df['dist_from_previous_frame_female_98']= df.frame_number.apply(instance_distance_between_frame, instance_name='Female_98')


# In[ ]:


df['dist_from_previous_frame_female_98'].sum()


# In[ ]:


import plotly.express as px
import plotly.graph_objects as go


# In[ ]:



fig = px.line(x=df.frame_number, y=df.dist_from_previous_frame_female_86, labels={'x':'frame_number', 'y':'dist from previous frame female_86'})
fig.show()


# ## Distance between two instances e.g. female_98 and male_109 in pixels

# In[ ]:


df['dist_frog__female_98_male_109'] = df.frame_number.apply(paired_distance)


# In[ ]:



fig = px.line(x=df.frame_number, y=df.dist_frog__female_98_male_109, labels={'x':'frame_number', 'y':'distance between frog male in tank 2 to frog female in tank 2'})
fig.show()

