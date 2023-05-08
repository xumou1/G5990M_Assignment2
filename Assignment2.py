# -*- encoding: utf-8 -*-
'''
@File    :   streamlit_ABM.py   
@Contact :   jshmxwc@gmail.com/gy22wx@leeds.ac.uk
@License :   (C)Copyright
 
@Modify Time        @Author     @Version    @Desciption
------------      ----------    --------    -----------
2023/4/4 20:54   Wanchen Xu      1.0         None
'''

import streamlit as st

def intro():
    import streamlit as st
    import openai

    st.write("# Welcome to Assignment2 made by Wanchen Xu(Contains Site suitablity and Slope calculation)!")
    st.sidebar.success("Select a feature above.")

    st.markdown(
        """
        This is a content of GEOG5990M Programming for Geographical Information Analysis: Core Skills (28787) Assignment2, 
        which completes the task of screening suitable sites and calculating slopes in Assignment2 in this code
        
        ### Want to learn more about Site suitablity?
        - Learn about Site suitablity through Arcgis(https://doc.arcgis.com/en/imagery/workflows/resources/site-suitability-analysis.htm)
        - Search Site suitablity in ChatGPT(http://chat.openai.com/chat or Chatbot under)

        ### Want to learn more about Streamlit?

        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        """
    )

    st.markdown("*GPT-3.5 Chatbot(Maybe you can use GPT-3.5 to learn more)*")
    # get API key from user
    test = st.text_input("Your OpenAI API Key:")
    openai.api_key = test

    # Define function to get response from GPT-3.5 model
    def get_response(input):

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=input,
            temperature=0.5,
            max_tokens=100,
            n=1,
            stop=None,
            timeout=10,
        )
        return response.choices[0].text.strip()

    st.markdown("***")
    st.markdown("### Question Area")
    user_input = st.text_input("You: ", "")

    if st.button("Send"):
        bot_response = get_response(user_input)
        st.text_area("Bot: ", value=bot_response, height=200, max_chars=None, key=None)

    st.markdown("Tips: Chatbot only works if you have an API key.")

def Site_suitability():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import io
    import doctest

    geology = None
    transport = None
    population = None

    st.title('Site Suitability')

    st.subheader('Upload the Data')
    # Upload the data of geology, transport, population
    uploaded_file = st.file_uploader("Select geology file(txt)", type="txt")
    if uploaded_file is not None:
        geology = pd.read_csv(uploaded_file, sep=',', header=None)
        # st.write(geology)

    uploaded_file = st.file_uploader("Select transport file(txt)", type="txt")
    if uploaded_file is not None:
        transport = pd.read_csv(uploaded_file, sep=',', header=None)
        # st.write(transport)

    uploaded_file = st.file_uploader("Select population file(txt)", type="txt")
    if uploaded_file is not None:
        population = pd.read_csv(uploaded_file, sep=',', header=None)
        # st.write(population)

    # Check the data and edit
    st.subheader('Check and Edit the Data')
    option = st.selectbox(
        'Which data would you want to check?',
        ('None', 'geology', 'transport', 'population'))
    if option == 'geology':
        checking_data = geology
    elif option == 'transport':
        checking_data = transport
    elif option == 'population':
        checking_data = population
    else:
        checking_data = None

    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv(index=False, header=False, sep=',').encode('utf-8')

    if st.checkbox("Edit Model"):
        if checking_data is not None:
            new_data = st.experimental_data_editor(checking_data)

            txt = convert_df(new_data)

            st.download_button(
                label="Download data as TXT",
                data=txt,
                file_name='new_' + option + '.txt',
                mime='text/plain',
            )
        else:
            st.error("No data uploaded.")
    else:
        if st.checkbox("Show Data by Image"):
            if checking_data is not None:
                plt.axis('off')
                plt.imshow(checking_data)
                title_font = {'fontname': 'Times New Roman', 'fontsize': 15, 'color': 'black'}
                plt.title('Example Title with Custom Font', **title_font, pad=10)
                plt.colorbar()
                st.pyplot()
                plt.close()

                image_buffer = io.BytesIO()
                plt.axis('off')
                plt.imshow(checking_data)
                title_font = {'fontname': 'Times New Roman', 'fontsize': 15, 'color': 'black'}
                plt.title(option.upper() + ' Data', **title_font, pad = 10)
                plt.colorbar()
                plt.savefig(image_buffer, format='PNG', dpi=600, bbox_inches='tight')
                plt.close()

                image_buffer.seek(0)

                st.download_button(
                    label="Download image",
                    data=image_buffer,
                    file_name=option + ".png",
                    mime="image/png",
                )
            else:
                st.error("No data uploaded.")
        else:
            st.write(checking_data)

    # Weight
    st.sidebar.write('Weight')
    if st.sidebar.checkbox("Use Number Input"):
        geology_weight = st.sidebar.number_input("Geology Weight")
        transport_weight = st.sidebar.number_input("Transport Weight")
        population_weight = st.sidebar.number_input("Population Weight")
    else:
        geology_weight = st.sidebar.slider("Geology Weight", 0.0, 100.0, 30.0)
        transport_weight = st.sidebar.slider("Transport Weight", 0.0, 100.0, 30.0)
        population_weight = st.sidebar.slider("Population Weight", 0.0, 100.0, 30.0)
    isrun = st.sidebar.button("Run")

    # Run site suit model
    def Normalize(Dataframe):
        '''
        Test for Normalize function.

        >>> df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
        >>> Normalize(df)
            a    b    c
        0   0.0  0.0  0.0
        1  127.5  127.5  127.5
        2  255.0  255.0  255.0
        '''
        return (Dataframe - Dataframe.min().min()) * (255 - 0) / (Dataframe.max().max() - Dataframe.min().min())

    st.subheader('Test the function')
    st.write(doctest.testmod())

    st.subheader('Run Site Suit Model')
    if geology is not None and transport is not None and population is not None:
        if geology_weight == 0 and transport_weight == 0 and population_weight == 0:
            st.error("Weight can not be 0.")
        else:
            if isrun:
                Result = geology_weight * geology + transport_weight * transport + population_weight * population
                Result_nor = Normalize(Result)
                plt.axis('off')
                plt.imshow(Result_nor)
                title_font = {'fontname': 'Times New Roman', 'fontsize': 15, 'color': 'black'}
                plt.title('Result Map After Considering Factors', **title_font, pad=10)
                plt.colorbar()
                st.pyplot()

                image_buffer = io.BytesIO()
                plt.axis('off')
                plt.imshow(Result_nor)
                title_font = {'fontname': 'Times New Roman', 'fontsize': 15, 'color': 'black'}
                plt.title('Result Map After Considering Factors', **title_font, pad=10)
                plt.colorbar()
                plt.savefig(image_buffer, format='PNG', dpi=600, bbox_inches='tight')
                plt.close()

                image_buffer.seek(0)

                st.download_button(
                    label="Download image",
                    data=image_buffer,
                    file_name="Normalized_Result.png",
                    mime="image/png",
                )

                result_data = convert_df(Result_nor)

                st.download_button(
                    label="Download Result data as TXT",
                    data=result_data,
                    file_name='Result_Data.txt',
                    mime='text/plain',
                )
    else:
        st.error("Need more data uploaded.")

def DEM_processing():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import streamlit as st
    import doctest

    st.title("DEM Processing")

    dem = None

    uploaded_file = st.file_uploader("Select DEM file(txt)", type=["txt", "csv"])
    if uploaded_file is not None:
        dem = pd.read_csv(uploaded_file, sep=' ', header=None)

    if st.checkbox("Check DEM"):
        st.write(dem)

    def calculate_slope(dem, cell_size):
        '''
        Calculate the slope from a given DEM and cell size.

        Args:
            dem (ndarray): 2D array representing the digital elevation model.
            cell_size (float): Size of a cell in the DEM.

        Returns:
            ndarray: 2D array representing the slope.

        Examples:
            >>> dem = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            >>> calculate_slope(dem, 1)
            array([[0.41421356, 0.41421356, 0.41421356],
                [0.41421356, 0.41421356, 0.41421356],
                [0.41421356, 0.41421356, 0.41421356]])
        '''
        pad_dem = np.pad(dem, ((1, 1), (1, 1)), mode='edge')
        slope = np.zeros_like(dem)
        progress_bar = st.sidebar.progress(0)
        frame_text = st.sidebar.empty()
        for i in range(1, pad_dem.shape[0] - 1):
            progress_bar.progress((i + 1) / pad_dem.shape[0])
            frame_text.text("Calculate Progress %d percent" % (int(i/3)))
            for j in range(1, pad_dem.shape[1] - 1):
                dz_dx = ((pad_dem[i - 1, j + 1] + 2 * pad_dem[i, j + 1] + pad_dem[i + 1, j + 1]) -
                         (pad_dem[i - 1, j - 1] + 2 * pad_dem[i, j - 1] + pad_dem[i + 1, j - 1])) / (8 * cell_size)
                dz_dy = ((pad_dem[i + 1, j - 1] + 2 * pad_dem[i + 1, j] + pad_dem[i + 1, j + 1]) -
                         (pad_dem[i - 1, j - 1] + 2 * pad_dem[i - 1, j] + pad_dem[i - 1, j + 1])) / (8 * cell_size)
                slope[i - 1, j - 1] = np.sqrt(dz_dx ** 2 + dz_dy ** 2)

        return slope

    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv(index=False, header=False, sep=',').encode('utf-8')

    if dem is not None:
        st.write("Check calculate funtion work well:")
        st.write(doctest.testmod())

        dem = dem.apply(pd.to_numeric, errors='coerce')

        cell_size = st.sidebar.slider("Cell Size", 1, 50, 1)
        slope = calculate_slope(dem.to_numpy(), cell_size)

        slope_without_nan = np.ma.masked_where(np.isnan(slope), slope)

        max_slope_position = np.unravel_index(np.argmax(slope_without_nan), slope_without_nan.shape)
        min_slope_position = np.unravel_index(np.argmin(slope_without_nan), slope_without_nan.shape)

        plt.imshow(slope)
        plt.colorbar(label='Slope')

        plt.plot(max_slope_position[1], max_slope_position[0], 'rx', label='Max Slope', markersize = 5, markeredgewidth = 2)
        plt.plot(min_slope_position[1], min_slope_position[0], 'ro', label='Min Slope', markersize = 5, markeredgewidth = 2)

        plt.legend()
        plt.title('Slope with Max and Min Positions')
        plt.axis('off')

        st.pyplot()
        st.write("Max Point", max_slope_position, " ", "Min Point", min_slope_position)
        if st.checkbox("Check Slope As Data"):
            st.write(slope)
            slope_df = pd.DataFrame(slope)
            slope_data = convert_df(slope_df)

            st.download_button(
                label="Download Slope as TXT",
                data=slope_data,
                file_name='Slope_Data.txt',
                mime='text/plain',
            )

page_names_to_funcs = {
    "Introduction": intro,
    "Site Suitability": Site_suitability,
    "Slope": DEM_processing
}

demo_name = st.sidebar.selectbox("Choose a feature", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()



