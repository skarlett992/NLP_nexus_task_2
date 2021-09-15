# Nexus AI Challenges

## TASK 1: ID Card Detection.
Problem: We want to solve a problem that occurs at buildings/companies’ receptions. Currently, a receptionist needs to input all the information manually and it takes a long time. Visitors need to wait for a long time and sometimes it creates a long queue in front of the reception.
We want to build a visitor sign-in system (visitor sign-in system) for company receptions. This system takes a photo of the Visitor's Photo ID card by a tablet placed on the reception and extracts the following information to identify the visitor.
- Face Photo
- Name
- ID Number
- Any other information as much as possible
And we cannot predict what type of ID card the visitor provides, it can be ...
- Passport of any countries
- The national ID card of any countries - something else
So, we need to support un-predictable formats. And also, the data extraction may happen on demand, so we need to complete the process within a reasonable duration.
### Input & Output
- Input
- ID Card Image taken by Tablet
- Output
- data (name, id, ... ) and image of face photo.

## Install: 
0. Configure venv ([link to manual](https://docs.python.org/3/tutorial/venv.html))  
1. Install project requirements `pip install -r /path/to/requirements.txt`
2. Put the image that you need to recognize into input directory
3. Open cli-console and run command: `python main.py --input input/work_card.png`
4. See result into output directory

## Requirements
Python 3.7.7
```buildoutcfg
asgiref==3.4.1
click==8.0.1
cycler==0.10.0
Django==3.2.7
image==1.5.33
imageio==2.9.0
importlib-metadata==4.8.1
joblib==1.0.1
kiwisolver==1.3.2
langid==1.1.6
matplotlib==3.4.3
nameparser==1.0.6
networkx==2.6.3
nltk==3.6.2
numpy==1.21.2
opencv-python==4.5.3.56
pandas==1.3.3
pdf2image==1.16.0
Pillow==8.3.2
pycountry==20.7.3
pyparsing==2.4.7
pytesseract==0.3.8
python-dateutil==2.8.2
pytz==2021.1
PyWavelets==1.1.1
regex==2021.8.28
scikit-image==0.18.3
scipy==1.7.1
six==1.16.0
sqlparse==0.4.2
tifffile==2021.8.30
tqdm==4.62.2
typing-extensions==3.10.0.2
zipp==3.5.0
```

## Annotaion / Questions:

1. A detailed solution which describes "How you would solve the problem", include URLs of web pages, articles, code repositories you will use.

A program has been developed based on the OCR library and the NTLK post-moderation algorithm. At the design stage of the implementation, I used the official documentation of the library pytesseract:
https://tesseract-ocr.github.io/tessdoc/
and a link to scientific articles describing the approach of NTLK:
https://openaccess.thecvf.com/content/CVPR2021/papers/Dai_Progressive_Contour_Regression_for_Arbitrary-Shape_Scene_Text_Detection_CVPR_2021_paper.pdf
https://www.nltk.org/


2. What kind of data and how much data you would require from the client and provide guidelines on how to make the data & how to annotate data.

Further development of the program will require additional training. A large increase in accuracy can be provided by the introduction of document types for their classification and marking of areas under the full name, document numbers, as well as binding to the data entry language.

3. Some results which you got with your strategy testing
The result of my work is a program that can:
1) find a photograph of a person's face in a document,
2) recognize text in a document
3) select the person's full name from the recognized text

This solution allows you to automatically recognize the language of the text. The program implements work through the I / O console of the operating system.

4. And How much data you required for training (If your solution requires it)

Prepared training ocr-models were used tessdata:
https://github.com/tesseract-ocr/tessdata

5. Describe how to build training/testing data (e.g. tools for annotation )
6. If you use any of the pre-trained models, use the model with the data sample ( you need to find something on the web ) and provide the result.

Prepared training ocr-models were used tessdata:
https://github.com/tesseract-ocr/tessdata

For testing, we used piece data sets to write scripts for saving the result.

7. Provide a timeline if you work on it only by yourself. (How many days/months you need, what kind of results you can promise to deliver

Employment schedule: part-time. The term of independent implementation (taking into account the current information provided in the condition of the problem statement): 1 year

8. Provide sample code you use ( code repository or jupyter notebook file )

https://github.com/skarlett992/nexus_task_2.git