# Automated Personal Loan Document Processing 
This is a OCR based application which Automates the process of entering the loan applicant's information into the loan application system
## To run the Project
   ### Install all dependencies listed in requirements.txt file by running the command from the project directory
   ```bash
   pip install -r requirements.txt
   ```
   ### Then from the project directory run the command
   ```bash
   streamlit run app/ui.py
   ```
## Working Flow
1. The streamlit provides an easy UI for uploading the documents of loan applicants in jpg, jpeg, png, pdf format
2. OpenCV & numpy library are used to preprocess the uploaded image and it returns the processed image
3. Then this processed image is passed to extract_text_from_image() function & here [pytesseract](https://pypi.org/project/pytesseract/) & [re](https://docs.python.org/3/library/re.html) are used to extract text from image
4. Then these extracted text are passed to extract_fields(ocr_text) function to retrive only required text and this function returns required text in (Key : Value) pair in a list format
5. Now this list is displayed on screen and for review and editing purpose
6. After that this list is sent to the actual Loan Application System
