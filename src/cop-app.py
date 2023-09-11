import streamlit as st
from pathlib import Path
import base64

# set page config
st.set_page_config(
    page_title='Gen AI Demos',
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    make_sidebar()
    make_body()

    return None


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


def make_sidebar():
    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=100 height=60>](https://streamlit.io/)'''.format(
        img_to_bytes("goreply.png")), unsafe_allow_html=True)
    st.sidebar.header('Apps show down here')

    st.sidebar.markdown('__Bigg text??__')

    return None


def make_body():
    chossing_app = st.selectbox('Which App would you like to test today? :eyes:',
                                ('App 1', 'App 2', 'App 3'))

    big_boy = st.container()

    with big_boy:
        col1, col2, col3 = st.columns(3)
        with col1:
            col1.subheader('App 1')
        with col2:
            col2.subheader('App 2')
        with col3:
            col3.subheader('App 3')


if __name__ == '__main__':
    main()
