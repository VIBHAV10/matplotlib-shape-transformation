import streamlit as st
def chooseShape():
    shape_type = st.selectbox("Choose a shape", ["Circle", "Polygon"])
    return shape_type

def chooseTransformation():
    transformation_type = st.selectbox("Choose a transformation", ["Translate","Rotate", "Scale"])
    return transformation_type

def circleForm():
    form = st.form(key="Circle")

    with form:
        col1,col2,col3= st.columns(3)
        with col1:
            r = st.number_input("Radius", value=1)
        with col2:
            x = st.number_input("X coordinate", value=0)
        with col3:
            y = st.number_input("Y coordinate", value=0)


        with col1:
            translate=st.checkbox("Translate")
        with col2:
            rotate=st.checkbox("Rotate")
        with col3:
            scale=st.checkbox("Scale")
  


        st.write("Enter the angle and coordinates for the point of rotation")
        with col1:
            angle=st.number_input("Angle", value=0)            
        with col2:
            Rx=st.number_input("X coordinate", value=0)
        with col3:
            Ry=st.number_input("Y coordinate", value=0)

        st.write("Enter the coordinates for the translation")
        with col1:
            Tx=st.number_input("X coordinate", value=0)
        with col2:
            Ty=st.number_input("Y coordinate", value=0)
        st.write("Enter the scaling factor")
        scale=st.number_input("New Radius", value=1)


        submitted = st.form_submit_button(label="Submit")
    if submitted:
        l=[x,y,r,[translate,rotate,scale],]
        return l
#cache this function
    

def circle_rotation():
    form = st.form(key="circle_rotate")
    with form:
        col1, col2,col3= st.columns(3)
        st.write("Enter the angle and coordinates for the point of rotation")
        with col1:
            angle=st.number_input("Angle", value=0)            
        with col2:
            x=st.number_input("X coordinate", value=0)
        with col3:
            y=st.number_input("Y coordinate", value=0)
        submitted = st.form_submit_button(label="Submit")
    if submitted:
        l=[x,y,angle]
        return l

def circle_translate():
    form = st.form(key="circle_translate")
    with form:
        st.write("Enter the coordinates for the translation")
        col1, col2= st.columns(2)
        with col1:
            x=st.number_input("X coordinate", value=0)
        with col2:
            y=st.number_input("Y coordinate", value=x)
        submitted = st.form_submit_button(label="Submit")
    if submitted:
        l=[x,y]
        return l

def circle_scale():
    form = st.form(key="circle_scale")
    with form:
        st.write("Enter the scaling factor")
        scale=st.number_input("New Radius", value=1)
        submitted = st.form_submit_button(label="Submit")
    if submitted:
        l=[scale]
        return l
        