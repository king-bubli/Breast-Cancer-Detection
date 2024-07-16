"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Breast Cancer Predictor")

    # Add image to the home page
    st.image("C:\\Users\\kingd\\Downloads\\Breast-Cancer-Detector-master\\images\\home.png")

    # Add brief describtion of your web app
    st.markdown(
    """## Table of Contents
- [About](#about-the-project)
- [Decision Tree](#decision-tree)
- [Why have I used decision tree in this project?](#why-have-I-used-decision-tree-in-this-project?)
- [Dataset](#dataset)
- [Working of the Model](#working-of-the-model)
- [Libraries Used](#libraries-used)

## About the Project
I have developed a Breast cancer Prediction System using Decision Tree. I am using Decision Tree to classify and predict breast cancer.

## Decision Tree
A decision tree is a type of supervised machine learning model used for categorization or making predictions based on a set of questions and their answers. Imagine it as a flowchart-like structure where each node represents a decision or test on specific attributes, branches represent the outcomes of those decisions, and leaf nodes hold the final predictions or classifications
<br>

## Why have I used decision tree in this project?
<ol>
<li>
<p><strong>Interpretability:</strong></p>
<ul>
<li>Decision trees are easy to understand and visualize. You can literally draw them out like flowcharts.</li>
<li>Each decision rule corresponds to a real-world condition, making it interpretable even for non-technical users.</li>
</ul>
</li>
<li>
<p><strong>Versatility:</strong></p>
<ul>
<li>Decision trees can handle both classification (categorical outcomes) and regression (continuous outcomes) tasks.</li>
<li>They serve as the foundation for more complex ensemble methods like Random Forests and Boosted Decision Trees.</li>
</ul>
</li>
<li>
<p><strong>Applications:</strong></p>
<ul>
<li>Decision trees find applications in various domains:
<ul>
<li>Medical diagnosis (e.g., predicting disease outcomes based on symptoms)</li>
<li>Customer churn prediction</li>
<li>Credit risk assessment</li>
<li>Recommender systems</li>
<li>And much more!</li>
</ul>
</li>
</ul>
</li>
</ol>

## Dataset
The breast cancer dataset is a classic and very easy binary classification dataset.

    =================   ==============
    Classes                          2
    Samples per class*   212(M),357(B)
    Samples total                  569
    Dimensionality                   9
    Features            real, positive
    =================   ==============

### ***Data Set Information***

Features are computed from a digitized image of a **Fine Needle Aspirate (FNA)** of a breast mass. They describe characteristics of the cell nuclei present in the image.

### ***Attribute Information:***

1) Diagnosis (1 = malignant, 0 = benign)
2) Ten real-valued features are computed for each cell nucleus:
    - radius (mean of distances from center to points on the perimeter)
    - texture (standard deviation of gray-scale values)
    - perimeter
    - area
    - smoothness (local variation in radius lengths)
    - compactness (perimeter^2 / area - 1.0)
    - concavity (severity of concave portions of the contour)
    - concave points (number of concave portions of the contour)
    - symmetry
    - fractal dimension (coastline approximation - 1)

## Working of the Model
<p>The dataset is loaded and then the data and targets are separated out. The data consists of 569 instances and 9 features.</p>
<p>Then from the mean it was observed that the distribution of the data was not even. So the data was stratified. Now the data was equally distributed among the two targets Malignant[1] and Benign[0].</p>
<table>
<tr><th width="50%">Benign [0]</th><th width="50%">Malignant [1]</th>
</tr>
<tr><td width="50%">Benign refers to a condition, tumor, or growth that is not cancerous. This means that it does not spread to other parts of the body. It does not invade nearby tissue. Sometimes, a condition is called benign to suggest it is not dangerous or serious. In general, a benign tumor grows slowly and is not harmful.</td><td width="50%">Malignancy is the tendency of a medical condition to become progressively worse. Malignancy is most familiar as a characterization of cancer.</td>
</tr>
</table>
<p align="center"><img src="https://www.verywellhealth.com/thmb/V4VdxdpWe0V1KY871SPrfw6kRqo=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/514240-article-img-malignant-vs-benign-tumor2111891f-54cc-47aa-8967-4cd5411fdb2f-5a2848f122fa3a0037c544be.png" width="100%"></p>

*For more information about Benign and Malignant Tumor, you can refer from  <a href="https://www.verywellhealth.com/what-does-malignant-and-benign-mean-514240">VeryWellHealth</a> page related to this.*

Further the *DecisionTreeClassifier* model is loaded and the training data is fitted in the variable where the model is loaded. Then the model is evaluated and the prediction on the training data is made.

## Libraries Used
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png" alt="Scikit Learn" width="30%">

Scikit Learn is a Python module integrating classical machine
learning algorithms in the tightly-knit world of scientific Python
packages (numpy, scipy, matplotlib).

It aims to provide simple and efficient solutions to learning problems
that are accessible to everybody and reusable in various contexts:
machine-learning as a versatile tool for science and engineering.</p>
<hr>
<p align="center">
<img src="https://miro.medium.com/v2/resize:fit:481/1*n_ms1q5YoHAQXXUIfeADKQ.png" alt="Pandas" width="30%">

Pandas is a Python package providing fast, flexible, and expressive data
structures designed to make working with "relational" or "labeled" data both
easy and intuitive. It aims to be the fundamental high-level building block for
doing practical, **real world** data analysis in Python. Additionally, it has
the broader goal of becoming **the most powerful and flexible open source data
analysis / manipulation tool available in any language**. It is already well on
its way toward this goal.
</p>
<hr>
<p align="center">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKIP8E5fz_gnfgCKDQRmhOGyzHNsbBgzsU8w&s" alt="NumPy" width="30%">

NumPy provides
  - An array object of arbitrary homogeneous items
  - Fast mathematical operations over arrays
  - Linear Algebra, Fourier Transforms, Random Number Generation
</p>
    """, unsafe_allow_html=True)