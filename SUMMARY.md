Development Summary 

Overview
For this final project, I created an AI-powered Personal Knowledge Management System (PKMS) designed to help users organize notes and manage tasks using a terminal-based interface. The system also integrates artificial intelligence to summarize notes and generate task suggestions. The entire project was developed in Python and uses JSON files for data storage, ensuring that it remains portable and functional across Windows, macOS, and Linux systems. The goal was not only to build a working application, but also to demonstrate the effective use of AI-coding assistance throughout the development process.

Throughout the project, I relied on AI as a support tool to help with planning, problem-solving, and code refinement. This allowed me to make consistent progress while also improving my understanding of system design and debugging strategies. The process felt like a balance between human decision-making and AI-guided direction, which helped shape the final result into a structured and functional system.

---

Development Process

Planning and Initial Setup
The development process began by carefully reviewing the assignment requirements and breaking them into manageable sections. I identified the core components: note management, task management, persistent storage, AI interaction, and a command-line interface. From there, I created a clear folder structure that separated each responsibility, making the codebase easier to understand and maintain. This allowed me to approach development in smaller, logical steps rather than attempting everything at once.

I focused on keeping the structure organized and readable, with each file serving a specific purpose. This made it easier to locate problems and implement improvements as the project evolved. Having a clear starting plan helped reduce confusion and created a stable foundation for future additions.

---

How I Used AI-Coding Assistants

ChatGPT was my assistant of choice due to how simple and accessable it was and played a major role in building this project. I primarily used it in a conversational way, treating it like a development assistant that could help explain concepts, generate starter code, and troubleshoot errors. This collaboration made the development process more efficient and less intimidating.

ChatGPT helped with planning the architecture, suggesting folder structures, and recommending how different components should interact. It also provided initial versions of key functions for managing notes, tasks, and JSON storage. I used these as a base and then modified them to better fit my intended design and system behavior. This ensured that I remained in control while still benefiting from AI-generated ideas.

When issues arose, such as error messages or unexpected behavior, ChatGPT helped interpret tracebacks and explain what was happening behind the scenes. This made debugging more educational rather than frustrating and helped build an understanding due to keeping its fixes easy to udnerstand.

---

What Worked Well

Several aspects of the project worked smoothly and contributed to its success. Separating the system into individual modules made debugging much easier and improved overall clarity. JSON storage proved reliable and easy to work with, allowing data to persist between sessions without complications. The terminal interface was intuitive and allowed for clear communication with the system. Using Git throughout the project helped track changes and ensured safe experimentation.

One of the most effective parts of the development was the integration of AI functionality. Once the environment variables and API configuration were correctly set up, the AI features worked consistently. Being able to summarize notes and generate task ideas added meaningful value and demonstrated the practical use of artificial intelligence in the system.

---

Challenges and What Didn’t Work

There were several obstacles encountered throughout development, which required troubleshooting and adjustment. One major challenge involved Python environment conflicts. Having multiple versions of Python installed caused confusion when installing and running required packages, especially for OpenAI and dotenv. This required careful verification of interpreter paths and environment settings.

Import errors were another common problem early on. Incorrect file paths and missing initialization files caused repeated failures. These issues were resolved by reorganizing the project structure and ensuring all directories were properly recognized by Python. API configuration also caused issues at first, as the system struggled to read environment variables correctly. Through trial and error, the configuration was fixed and stabilized.

Some command-handling features initially failed due to incorrect parsing and method calls. These were corrected through careful testing and logic adjustments. While frustrating at times, these issues strengthened my understanding of how different system components work together.

---

Testing Process

Testing was performed through repeated interaction with the terminal interface. I created notes, added tasks, marked them as complete, and searched for specific entries to ensure correct functionality. I also tested how the system handled invalid inputs and empty lists to verify stability and error handling.

The AI features were tested by running summarization and task suggestion commands on various notes. This confirmed that AI responses were being generated correctly and consistently. Each testing phase helped fine-tune the system and improve its overall reliability.

---

Overall Reflection

This project provided a valuable learning experience by demonstrating how AI can assist without replacing critical thinking. While AI helped accelerate development, I still needed to analyze the code, understand errors, and make informed decisions. This balance reinforced the importance of both technical knowledge and adaptability.

The process helped improve my skills in debugging, planning, and system organization. It also gave me greater confidence in working with larger projects that involve multiple interacting components and real-world constraints.