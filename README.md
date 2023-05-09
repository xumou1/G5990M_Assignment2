# <span style="font-family: Times New Roman, sans-serif;">G5990M Programming for Geographical Information Analysis: Core Skills (28787) Assignment2</span>
*<span style="font-family: Times New Roman, sans-serif;">
  Author:Wanchen Xu<br>
  &nbsp;&nbsp;&nbsp;&nbsp;<br>
  Project Github Address: https://github.com/xumou1/G5990M_Assignment2<br>
  Streamlit Share Address: https://xumou1-g5990m-assignment2-assignment2-p4cr3f.streamlit.app/<br>
  &nbsp;&nbsp;&nbsp;&nbsp;<br>
</span>*

- [<span style="font-family: Times New Roman, sans-serif;">G5990M Programming for Geographical Information Analysis: Core Skills (28787) Assignment2</span>](#-span-style--font-family--times-new-roman--sans-serif---g5990m-programming-for-geographical-information-analysis--core-skills--28787--assignment2--span-)
  * [<span style="font-family: Times New Roman, sans-serif;">1 Introduction</span>](#-span-style--font-family--times-new-roman--sans-serif---1-introduction--span-)
    + [<span style="font-family: Times New Roman, sans-serif;">1.1 Project Background</span>](#-span-style--font-family--times-new-roman--sans-serif---11-project-background--span-)
    + [<span style="font-family: Times New Roman, sans-serif;">1.2 Project Requirements</span>](#-span-style--font-family--times-new-roman--sans-serif---12-project-requirements--span-)
      - [<span style="font-family: Times New Roman, sans-serif;">1.2.1 Site Suitability Requirements</span>](#-span-style--font-family--times-new-roman--sans-serif---121-site-suitability-requirements--span-)
      - [<span style="font-family: Times New Roman, sans-serif;">1.2.2 DEM Processing Requirements</span>](#-span-style--font-family--times-new-roman--sans-serif---122-dem-processing-requirements--span-)
  * [<span style="font-family: Times New Roman, sans-serif;">2 Code Details</span>](#-span-style--font-family--times-new-roman--sans-serif---2-code-details--span-)
    + [<span style="font-family: Times New Roman, sans-serif;">2.1 Function Implementation Logic And Code</span>](#-span-style--font-family--times-new-roman--sans-serif---21-function-implementation-logic-and-code--span-)
      - [<span style="font-family: Times New Roman, sans-serif;">2.1.1 Site Suitability Logic And Code</span>](#-span-style--font-family--times-new-roman--sans-serif---211-site-suitability-logic-and-code--span-)
      - [<span style="font-family: Times New Roman, sans-serif;">2.1.2 DEM Processing Logic And Code</span>](#-span-style--font-family--times-new-roman--sans-serif---212-dem-processing-logic-and-code--span-)
  * [<span style="font-family: Times New Roman, sans-serif;">3 Question And Solving Method</span>](#-span-style--font-family--times-new-roman--sans-serif---3-question-and-solving-method--span-)

## <span style="font-family: Times New Roman, sans-serif;">1 Introduction</span>

### <span style="font-family: Times New Roman, sans-serif;">1.1 Project Background</span>
<span style="font-family: Times New Roman, sans-serif;">&nbsp;&nbsp;&nbsp;&nbsp;Two different scenarios exist in Assignment 2. One is that a company producing stone has provided three essential indicators that influence the location of its plant in the UK and wants to obtain software that can manually adjust the weighting parameters. A certain amount of code was required to accomplish this goal. Secondly, an extreme sports holiday company wanted to find suitable locations for their activities and therefore needed you to find a suitable location by calculating the slope.  
  &nbsp;&nbsp;&nbsp;&nbsp;In this scenario, we needed to complete the tasks given in the scenario, and in this case, we chose Python as the primary language according to the course requirements.Here's a brief introduction to python and streamlit  
  &nbsp;&nbsp;&nbsp;&nbsp;Python is a high-level, interpreted, and general-purpose programming language created by Guido van Rossum and first released in 1991. It has a simple and easy-to-read syntax, making it a popular choice for beginners and experienced programmers. Python is known for its versatility. It can be used for various applications, including web development, data analysis, artificial intelligence, machine learning, scientific computing, automation, and more.
Python has an extensive standard library, which provides a wealth of built-in modules and functions to handle everyday tasks. Additionally, Python has a vast ecosystem of third-party packages available through the Python Package Index (PyPI), further extending its capabilities.&nbsp;&nbsp;[Link to Python](https://www.python.org/)  
  &nbsp;&nbsp;&nbsp;&nbsp;Streamlit is a Python library for building interactive web applications for data science and machine learning. It was created in 2018 by Adrien Treuille, Amanda Kelly and Thiago Teixeira.Streamlit aims to enable data scientists and developers to quickly and easily create engaging data visualization applications without spending much time writing front-end code.
Streamlit provides a clean, easy-to-use API that lets us focus on working with data and creating visualizations without worrying about complex UI logic. It integrates with standard Python data science libraries such as NumPy, Pandas, Matplotlib and Plotly. In addition, Streamlit supports hot reloading, which means that when we update our code, the application responds and updates in real-time, making iterative development much more accessible.&nbsp;&nbsp;[Link to Streamlit](https://streamlit.io/)
</span>
><span style="font-family: Times New Roman, sans-serif;">**_Life is short, use Python.&nbsp;&nbsp;_** _--Guido van Rossum_</span>

### <span style="font-family: Times New Roman, sans-serif;">1.2 Project Requirements</span>
<span style="font-family: Times New Roman, sans-serif;">
  &nbsp;&nbsp;&nbsp;&nbsp;In this section we will focus on analysing the project requirements in both scenarios and combine them with the requirements outlined in Assignment 2 to arrive at a more complete and mature project requirements contentM<br>
  &nbsp;&nbsp;&nbsp;&nbsp;<br>
</span>

#### <span style="font-family: Times New Roman, sans-serif;">1.2.1 Site Suitability Requirements</span>
<span style="font-family: Times New Roman, sans-serif;">
  &nbsp;&nbsp;&nbsp;&nbsp;First of all we can see in the pdf of the brief description of the project that there are four basic requirements for this project.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;1. Reads the raster data and displays them.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;2. Multiplies each raster by a factor, adds the weighted rasters together and rescales the resulting raster to have values in the range [0, 255].<br>
  &nbsp;&nbsp;&nbsp;&nbsp;3. Displays the result raster and writes this to a file.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;4. Provides a GUI that allows the user to choose the weights by means of ‘sliders’ and that displays the result.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;This is a program that requires the development of a graphical user interface (GUI) whose primary function is to read one or more raster data and perform a weighted multiplication operation, add the results and rescale them to values in the range [0, 255] and display the resulting raster data in the GUI. The program also provides sliders for users to select weights and save the results to a file. The requirement is primarily for geospatial data analysis. It is intended to provide the user with a simple and practical tool to adjust the weights and visualise the results for spatial analysis using the sliders.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;We can see that in the pdf of the brief project, the primary four requirements for this project are briefly the four steps of the experiment and the visualisation of reading data, processing data, producing results and exporting results. The requirement is that the final results be regularised to between 0 and 255, as well as allowing the user to control the processing of the data steps (and adjusting the weights), again based on our requirements. We added the ability to query and edit the original data and download the updated data. We found that it was not easy to find a range of problems with the data when querying the table for complete UK data, so we added the ability to image the data.
</span>

#### <span style="font-family: Times New Roman, sans-serif;">1.2.2 DEM Processing Requirements</span>
<span style="font-family: Times New Roman, sans-serif;">
  &nbsp;&nbsp;&nbsp;&nbsp;The requirements for this project are similar to those of the previous one, and the documentation briefly mentions four requirements for it.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;1. Reads the raster data and displays it.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;2. Calculates the maximum slope for each row and column (pixel) of the raster by considering all the slopes between the pixel and the 8 nearest pixels. (Think about what to do at the map edges.)<br>
  &nbsp;&nbsp;&nbsp;&nbsp;3. Saves the maximum slopes to a file in the same format as the provided raster data.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;4. Provides a GUI that allows the user to choose the raster data file to load and that displays the result and on top of this the most extreme locations in terms of maximum slope.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;Both requirements require the development of a GUI program and involve the reading, processing and display of the raster data and the saving of the results to a file. However, their primary function is different, as the main function of this project requirement is to calculate the maximum slope of the raster data and display the result in the GUI. In contrast, the primary function of the first requirement is to perform a weighted multiplication operation on the raster data and add the results, then rescale the result and display it in the GUI. In addition, the first requirement requires the provision of a slider for the user to select the weights. The focus of this project requirement was to calculate the maximum slope of the raster data and display the result in the GUI. This required complex calculations and processing of the raster data, including consideration of map edges and the use of progress bars to track the progress of the calculations. The main objective of this requirement is to provide a practical tool for geospatial analysis that can help users better understand terrain features and landscape structure.
</span>

## <span style="font-family: Times New Roman, sans-serif;">2 Code Details</span>

### <span style="font-family: Times New Roman, sans-serif;">2.1 Function Implementation Logic And Code</span>
<span style="font-family: Times New Roman, sans-serif;">
  &nbsp;&nbsp;&nbsp;&nbsp;This section describes the software functionality and the functional implementation logic of the project requirements mentioned above.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;<br>
</span>

#### <span style="font-family: Times New Roman, sans-serif;">2.1.1 Site Suitability Logic And Code</span>
<span style="font-family: Times New Roman, sans-serif;">
  &nbsp;&nbsp;&nbsp;&nbsp;The function of this code is to add a file upload control to the Streamlit application that allows the user to select a text file and read that file as a Pandas DataFrame. This particular file upload control is used to select the geology data file. If the user uploads a file, it is read as a Pandas DataFrame, stored in the variable geology and can then be used in subsequent code. It follows the steps below:<br>
1. Call the st.file_uploader() method to create a file upload control, displaying the text "Select geology file(txt)" and restricting the file type to "txt".<br>
2. Check if the uploaded file is empty, and if not, read the contents of the file using Pandas' read_csv() method, specifying the file separator as a comma (sep=',') and no header line (header=None).<br>
3. Store the read data in the variable geology for subsequent use.<br>
As shown in code fragment 1 below<br>
</span>

```python
# CODE FRAGMENTS 1
# Upload the data of geology, transport, population
uploaded_file = st.file_uploader("Select geology file(txt)", type="txt")
if uploaded_file is not None:
   geology = pd.read_csv(uploaded_file, sep=',', header=None)
```

<span style="font-family: Times New Roman, sans-serif;">
  &nbsp;&nbsp;&nbsp;&nbsp;In code fragment 2, the data frame is implemented by calling st.experimental_data_editor() to edit the data frame and convert it to new CSV data. First, the data is read from the file uploaded by the user and stored in the checking_data variable. Then, if the user has selected edit mode, the st.experimental_data_editor() function will be called to open an editable form screen, allowing the user to make changes to the form directly. Once the user has finished editing, the convert_df() function will be used to convert the modified DataFrame to CSV format and the st.download_button() function will be used to create a download button allow the user to download the modified data file.<br>
</span>

```python
# CODE FRAGMENTS 2
new_data = st.experimental_data_editor(checking_data)

txt = convert_df(new_data)

st.download_button(
    label="Download data as TXT",
    data=txt,
    file_name='new_' + option + '.txt',
    mime='text/plain',
)
```

<span style="font-family: Times New Roman, sans-serif;">
  &nbsp;&nbsp;&nbsp;&nbsp;The primary function of code frament 3 is to display the raster data in the GUI and provide a download button to download the corresponding image file. The logic of the implementation is as follows: the overall step is divided into two parts: to display the data and to download the data. In the show data step, the imshow function in the matplotlib library displays the raster data on the canvas and sets the title and colour bar. Show the image and use the savefig function to save the image to the image_buffer. Call the seek(0) function to move the file pointer to the beginning of the file. Use the st.download_button function to create a download button to allow the user to download the image file. This function takes four arguments: the tag, the data (i.e. which binary cache data image_buffer was used previously), the file name and the MIME type.<br>
</span>

```python
# CODE FRAGMENTS 3
plt.axis('off')
plt.imshow(checking_data)
title_font = {'fontname': 'Times New Roman', 'fontsize': 15, 'color': 'black'}
plt.title(option.upper() + ' DATA', **title_font, pad=10)
plt.colorbar()
st.pyplot()
plt.close()

image_buffer = io.BytesIO()
plt.axis('off')
plt.imshow(checking_data)
title_font = {'fontname': 'Times New Roman', 'fontsize': 15, 'color': 'black'}
plt.title(option.upper() + ' DATA', **title_font, pad = 10)
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
```

<span style="font-family: Times New Roman, sans-serif;">
  &nbsp;&nbsp;&nbsp;&nbsp;The primary function of code snippet 4 is to create a sidebar containing three sliders for selecting the values of the weights to achieve the required user control of the weights. These sliders pass the user-selected values for geological, traffic and population weights through the slider component, which are stored in variables and used in the weighted raster calculation. For each slider, three initial settings are included, i.e. minimum, maximum and default values, which are adjusted according to the user input values.<br>
</span>

```python
# CODE FRAGMENTS 4
geology_weight = st.sidebar.slider("Geology Weight", 0.0, 100.0, 30.0)
transport_weight = st.sidebar.slider("Transport Weight", 0.0, 100.0, 30.0)
population_weight = st.sidebar.slider("Population Weight", 0.0, 100.0, 30.0)
```

<span style="font-family: Times New Roman, sans-serif;">
  &nbsp;&nbsp;&nbsp;&nbsp;This code defines a normalisation function to normalise the value of the final result after the weighting has been completed so that it maps the pixel values in the range of 0-255 for the final visual presentation.
The input to the function is a variable in DataFrame format. The minimum and maximum values of all rows of the DataFrame are obtained and used to normalise the data, and then the final normalised result is mapped to the range 0 to 255 by multiplying by 255. The function returns the DataFrame with the range limits completed.
The function also contains a doctest test module to check that the function is implemented correctly. The test module gives a test DataFrame containing integers from 1 to 9. The function is used to normalise this test DataFrame and compare the result with the expected result to ensure the function has been implemented correctly.<br>
</span>

```python
# CODE FRAGMENTS 5
def Normalize(Dataframe):
    '''
    Test for Normalize function.

    >>> df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    >>> Normalize(df)
        a    b    c
    0   0.0  31.875  63.75
    1  95.625  127.5  159.375
    2  191.25  223.125  255.0
    '''
    return (Dataframe - Dataframe.min().min()) * (255 - 0) / (Dataframe.max().max() - Dataframe.min().min())
```

#### <span style="font-family: Times New Roman, sans-serif;">2.1.2 DEM Processing Logic And Code</span>
<span style="font-family: Times New Roman, sans-serif;">
  &nbsp;&nbsp;&nbsp;&nbsp;This function calculates the slope of a Digital Elevation Model (DEM), which takes a 2D array of the form DEM and the cell size as input parameters. As it is necessary to use the D8 algorithm often used in calculating slope to facilitate the calculation of the position of the edge section, the function first fills the DEM by raising its length and width by one pixel in size, i.e. adding the top and bottom rows and the left and rightmost columns to the array, and then carries out the operation of calculating the slope for each cell, finally returning a two-dimensional array representing the slope. The calculation process is long and therefore requires a progress bar to check the progress of the function. Inside the function, a progress bar is initialised to show the calculation progress in the sidebar. The function also contains a text box to display text information about the progress of the calculation. In the implementation, the slope is calculated by solving for the slope using a trigonometric function and calculating the slope by differencing.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;The code uses the D8 algorithm, which calculates the slope of each pixel of the DEM and returns an array of the same size as the DEM:
Extend the DEM by 1 unit in both rows and columns, using "edge extrapolation", where the elevation of a grid point on the edge is the elevation of its neighbouring interior point; Iterate through the interior of the DEM one by one and calculate the difference in height between the eight surrounding points and the point as dx (for distance in the x-direction) and dy (for distance in the y-direction) respectively; The dx and dy are used to calculate the slope values using the Pythagorean theorem, and the resultant array is returned with the same size as the original DEM array. The D8 algorithm gets its name from the fact that it uses a 3 x 3 neighbourhood, as shown in the following figure:<br>
  
![Figure1 D8 Algorithms Image](https://github.com/xumou1/G5990M_Assignment2/blob/main/image/D8.jpg)

Where p is the currently calculated pixel point and 1-8 are the eight adjacent pixel points, numbered sequentially. In the D8 algorithm, each pixel point can only flow out in one of the eight adjacent directions, i.e. to the lowest adjacent pixel point. If multiple adjacent pixel points of the same height exist, one direction is chosen at random. This method is often used in slope calculations.<br>
</span>

```python
# CODE FRAGMENTS 1
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
```

<span style="font-family: Times New Roman, sans-serif;">
  &nbsp;&nbsp;&nbsp;&nbsp;The primary function of code snippet 2 is to obtain the slope image with the NaN values removed, as the presence of an image with NAN values affects the location of the maximum value. After the data cleaning in the previous step, the next step is to find the location of the maximum and minimum slope values using the numpy library function unravel_index() and then label the location with markers on the original DEM image ( The markers used here are the red x's and circles). The max_slope_position and min_slope_position are the tuples obtained by the method in np mentioned above and represent the row and column coordinates of the location of the maximum and minimum slope values.<br>
</span>

```python
# CODE FRAGMENTS 2
slope_without_nan = np.ma.masked_where(np.isnan(slope), slope)

max_slope_position = np.unravel_index(np.argmax(slope_without_nan), slope_without_nan.shape)
min_slope_position = np.unravel_index(np.argmin(slope_without_nan), slope_without_nan.shape)

plt.plot(max_slope_position[1], max_slope_position[0], 'rx', label='Max Slope', markersize = 5, markeredgewidth = 2)
plt.plot(min_slope_position[1], min_slope_position[0], 'ro', label='Min Slope', markersize = 5, markeredgewidth = 2)
```

## <span style="font-family: Times New Roman, sans-serif;">3 Question And Solving Method</span>


