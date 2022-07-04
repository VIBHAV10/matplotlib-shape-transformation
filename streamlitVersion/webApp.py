from requests import session
import streamlit as st 
import  streamlitVersion.shape as shape
import streamlitVersion.func as func
import matplotlib.pyplot as plt

#Title of the Project
st.title("Geometrical Transformations")

#starting the application
shapeType=func.chooseShape() #function to call the main menu to select between polygon and circle

global query

if 'l1' not in st.session_state:
    st.session_state['l1']=[]
if 'query' not in st.session_state:
    st.session_state['query']=[]

def val():
    global query
    query=[st.session_state.query[0],st.session_state.query[1],st.session_state.query[2]]
#print session state variables
if shapeType=="Circle":
    l1=func.circleForm() #function to call the form to enter the parameters of the circle 
    st.session_state['l1']=l1
    if(st.session_state.l1):
        cir=shape.Circle(l1[0],l1[1],l1[2])
        output = cir.scale(float(1))
        cir.plot()
        # circle1 = plt.Circle(( cir.center_x , cir.center_y ), cir.rad) 
        # figure, axes = plt.subplots()
        # axes.add_patch(circle1)       
        # axes.set_aspect( 1)
        # plt.title( 'Circle' )
        # st.pyplot(figure)

        
        if(l1[3]=="Rotate"):
            query=func.circle_rotation()
            st.session_state['query']=query
            if(st.session_state.query):
                output = cir.rotate(float(query[0]), float(query[1]), float(query[2]))
                cir.plot()

        if(l1[3]=="Translate"):
            query=func.circle_translate()
            st.session_state['query']=query
            if(st.session_state.query):
                output = cir.translate(float(query[1]), float(query[2]))
                cir.plot()

        if(l1[3]=="Scale"):
            query=func.circle_scale()
            st.session_state['query']=query
            if(st.session_state.query):
                output = cir.scale(float(query[0]))
                cir.plot()
                    