# MOST: Modern Open Scientific / Standard Templates

By: **Morteza Zakeri**†

† Ph.D., Iran University of Science and Technology, Tehran, Iran (m-zakeri@live.com).

Version 0.2.0 (11 April 2023)


**Abstract—** 
Welcome to __Modern Open Scientific / Standard Templates (MOST)__ repository. By submitting my MSc thesis in 2018, I introduced a new latex template to perform writing and publishing Persian thesis in a standard and pretty style. 
Today this repository consists of additional latex and Microsoft office template including templates for technical reports, homework, and presentations. We decided to publish all of these templates on GitHub. 
Please send me your feedback and comments if you are using (Z)MOST templates.  
  
**Index Terms:** LaTex-template, Office template, Persian pretty typesetting


## 1 Packages in MOST

### 1.1 latex
Contains the Tex templates for writing theses, reports, homework, technical reports, and presentations.

#### 1.1.1 IUST Thesis template
The main package in MOST is the IUST-Thesis template. It supports different types of theses, including the Ph.D. dissertation, M.Sc. thesis, and B.Sc. project.

##### How to compile?
Use the following command to create the PDF file for your thesis.

1. `git clone https://github.com/m-zakeri/ZMOST.git`
2. `xelatex.exe -synctex=1 -interaction=nonstopmode "maintext.tex"`
3. `xindy -L persian-variant1 -C utf8 -I xindy -M "maintext".xdy -t "maintext".glg -o "maintext".gls "maintext".glo`
4. `xelatex.exe -synctex=1 -interaction=nonstopmode "maintext".tex`

#### 1.1.2 Example thesis
Some sample theses using the IUST Thesis template are as follows:

* [https://github.com/m-zakeri/MSc](https://github.com/m-zakeri/MSc)


### 1.2 word
Contains Microsoft Word templates for writing theses, reports, and seminars.


### 1.3 powerpoint
Contains Microsoft PowerPoint templates for academic presentations.



## 2 FAQ
For any question please contact `m-zakeri@live.com`

