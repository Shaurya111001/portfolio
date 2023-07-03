import streamlit as st

def main():
    # Set page title and layout
    st.set_page_config(page_title='Portfolio Website', layout='wide')

    # Create sidebar navigation
    st.sidebar.title("Navigation")
    menu_options = ['About Me', 'Education', 'Work Experience', 'Projects', 'Awards', 'Skills']
    choice = st.sidebar.radio("Go to", menu_options)

    # Render different pages based on user choice
    if choice == 'About Me':
        render_about_me()
    elif choice == 'Education':
        render_education()
    elif choice == 'Work Experience':
        render_work_experience()
    elif choice == 'Projects':
        render_projects()
    elif choice == 'Awards':
        render_awards()
    elif choice == 'Skills':
        render_skills()

def render_about_me():
    st.title("About Me")
    st.write("Hello, I'm Shaurya Aditya Singh.")
    st.write("I am a passionate developer with experience in various technologies.")
    st.write("Feel free to explore my work and contact me for any collaboration opportunities.")
    st.write("GitHub: [github.com/Shaurya111001](https://github.com/Shaurya111001)")
    st.write("Email: adityasingh111001@gmail.com")
    st.write("Devfolio: [devfolio.co/@Shaurya11](https://devfolio.co/@Shaurya11)")

def render_education():
    st.title("Education")
    st.write("Bachelor of Technology in Computer Science")
    st.write("Jaypee University of Engineering and Technology, Guna, India")
    st.write("Expected Graduation: 2023")
    st.write("GPA: 8.8/10")
    st.write("Coursework: Data Structure and Algorithms, Operating Systems, Database Management, Machine learning, Artificial Intelligence, Information Security, and Cryptography.")
    st.write("---")
    st.write("Intermediate (Science with Mathematics)")
    st.write("Kendriya Vidyalaya (C.B.S.E.), Varanasi-2019")
    st.write("Percentage: 88/100")
    st.write("Secured 4th Position in School")
    st.write("1st in Mathematics (95/100)")

def render_work_experience():
    st.title("Work Experience")
    st.write("Software Engineer Intern")
    st.write("Incture Technologies, Bengaluru, India")
    st.write("February 2023 - June 2023")
    st.write("- Worked on various AWS services like IoT Core and QLDB using Python SDK.")
    st.write("- Developed solutions for clients by utilizing knowledge of different tools and creating secure data communication channels between them.")
    st.write("---")
    st.write("Software Development Intern")
    st.write("Qurinom Solutions, Remote")
    st.write("April 2022 - November 2022")
    st.write("- Spearheaded a project, Showcase, a video-sharing-based E-commerce website using MERN Stack.")
    st.write("- Developed object-oriented code in Node.js in accordance with industry and company standards using the Express framework with 2 models and more than 15 APIs.")
    st.write("- Led the transition from Ejs template to React, providing proficient Data Binding and Reusable Components. Integrated it with the server using Axios and JWT.")

def render_projects():
    st.title("Projects")
    st.write("Here are some of the projects I've worked on:")
    st.write("1. BlockChain Based Donation System")
    st.write("- Built a portal where people can donate Ethereum tokens to NGOs and organizations.")
    st.write("- Created the smart contract using Solidity for token transfer. [View Code](https://github.com/your-github-repo/blockchain-based-donation)")
    st.write("- Designed UI in React.JS and integrated it with Flask and Web3 Smart Contract.")
    st.write("---")
    st.write("2. TechX - A Portal to Bring Business Online")
    st.write("- Built a web portal where any business owner can register and access all employees, assign tasks assigned to the employees, and schedule meetings.")
    st.write("- Worked on the server using NodeJS with 2 schema models and over 6 controller APIs. [View Code](https://github.com/your-github-repo/techx-portal)")
    st.write("- Designed UI using React-Three-Fiber for 3D animations.")
    st.write("---")
    st.write("3. Plant Disease Detection App using React-Native and FastApi")
    st.write("- Created a Plant disease detection model using the Plant Village dataset to classify over 38 classes.")
    st.write("- Used React-Native in the front end and connected it with the weights of the model as a server using FastApi. [View Code](https://github.com/your-github-repo/plant-disease-detection-app)")

def render_awards():
    st.title("Awards and Achievements")
    st.write("Winner at Startup Saga - A Bug in a Startup Hackathon by AIT Pune (Devfolio) - Nov 2021")
    st.write("Microsoft Technology Associate in Python by Microsoft - Sep 2020, Scored Above 85")
    st.write("Deep Learning.AI TensorFlow Developer Professional Certificate")
    st.write("JP Morgan Virtual Internship Program – Displayed visual data using React and Learned Perspective software.")

def render_skills():
    st.title("Skills & Interests")
    st.write("Languages: Python, JavaScript, Java, HTML/CSS, C++")
    st.write("Platforms: Django, Flask, React, TensorFlow, Scikit-Learn, Git, SmartPy, Taquito, Web3, Spring Boot, Docker")

if __name__ == '__main__':
    main()
