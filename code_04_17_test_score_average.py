# code_04_17_test_score_average.py
# This program average test score. It asks the user for the number of students and the number of the score per student
import streamlit as st 
# Streamlit app setup  
st.title('Exam Score Average Calculator')  
# Get the number of students
num_stu = int(st.number_input('Enter the number of student', min_value=1))
# Get the number of test score per students
num_exam_score = int(st.number_input('Enter the number of exam', min_value=1)) 

total_average = 0.0
# Repeat task for students. Determine each students' average test score
for student in range(num_stu): 
    # Initialize an accumulator for test score
    total = 0.0
    # Repeat caculation for exam
    st.header(f'student number {student + 1}')
    for exam in range(num_exam_score):
        # Get a student's test score
        while True:  
            try:  
                score = float(st.text_input(f'Please enter {exam + 1}exam score (0-100)'))  
                if 0 <= score <= 100:  
                    break  
                else:  
                    st.error('Exam score must be between 0 and 100, please re-enter')  
            except ValueError:  
                st.error('Please enter a valid number as your exam score') 
        # Caculate the average test score for this students
        total += score  
        average = total / (exam + 1)  # Calculate the running average for this student  
        st.write(f'The{exam + 1}exam score has been entered')  
        st.write(f'The current average score of this student is：{average}')  
    # Display the average
    st.write(f'student number {student + 1}, the average is：{average}')  
    total_average += average  
# Calculate and display the overall average for all students  
st.header('Average grades of all students')  
st.write(f'The average score of all students is：{total_average / num_stu}')
#! Add a print line for which number of exam you are
#! Add input validation for exam score. each exam score should be in range of >=0 to <=100
    # Add caculation of average of all students
    # Add keep going machanism
    # BAsed on the code, make a streamlit app
    # Upload the code to the github and deploy your app using streamlit.io
    # At the top of the script, add the streamlit link
