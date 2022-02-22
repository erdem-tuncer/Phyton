from matplotlib import pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import datetime
from PIL import Image

st.title("My Good and Big Title")
st.title("maybe second title")

st.text("this is written with the ext function")

st.markdown("`import numpy as np`") # this is like a code
st.markdown("## Subheader")

st.header("Header function")  #if you want to access with url
st.subheader("This is  a subheader with subheader function")

st.success("success")
st.info('be careful')
st.error("oops!")

st.help(print)

st.write("this is a text written with `write` function.") #it understands the object type and it parses it
st.write(pd.DataFrame({
    'first column':[1,2,3,4],
'second column':[10,20,30,40]}))

img = Image.open('cat.jpg')
st.image(img, caption='very very cute kitty', use_column_width=True)

#video = open("videoname.mp4","rb")
#st.video(video)

st.video("https://www.youtube.com/watch?v=EtIelTF7As8")

#result = st.checkbox("my boring checkbox")
#st.write(result)

if  st.checkbox("my boring checkbox"):
    st.success("congrats you can click chackbox")
else:
    st.error("why?!!")


result = st.radio("How many cats do you want",(0,1,2,3,4,5))

st.write(result)


result1 = st.radio("How many cats do you want",('a','b', len))
st.write(result1)


check0 = st.button("Click me")
st.write(check0)

result2 = st.selectbox('Select a number', [0,1,2,3,4,5])
st.write(result2)

result3 = st.multiselect("Select one or more values", [0,1,2,3,4,5]) #it always returns list type
st.write(result3)

if len(result3) > 0:
    st.write(f'Here are {result3} cats for you!')
else:
    st.write("No cats for you -.-")

'------------------------'

x = st.slider("Select a value please", 10,50,15,10) #default starts from 0 to 100 # starts from 15 

if x != 10:
    st.write(x)
'------------------------'
#st.text_input("Please type smthng!", "Default text")

text = st.text_input("Please type smthng!", placeholder = 'Type right here...')
'------------------------'
st.text_area("Text area")

'------------------------'
#result6 = st.date_input("title")

result7 = st.date_input("title",datetime.datetime.now())
'------------------------'
st.time_input("Time :", datetime.time(12,0))


'------------------------'
st.code("""import numpy as np
import pandas as pd
import matplotlib as plt""")

'------------------------'
with st.echo():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    df = pd.DataFrame({'a':[1,2,3,4,5], 'b':[6,7,8,9,10]}) 
    df #dynamic 
'103------------------------'
st.sidebar.write("ON a slider") # at the left side

st.sidebar.code("""import numpy as np
import pandas as pd
import matplotlib as plt""")

y=st.sidebar.slider("Select bro smthg", 0.0,1.0,0.5,0.01)

'------------------------'
df=pd.read_csv("Mall_Customers.csv")

st.write(df) #dynamic
with st.echo(): #dynamic
    df


'static------------------------'
st.write("Table")
st.table(df) #statically
st.dataframe(df.head())


'----------------------126------------------------'
x=st.slider("select index")
st.line_chart(df['Age'][:x])  #interactive, You can zoom in or zoom out


'----------------------126------------------------'












