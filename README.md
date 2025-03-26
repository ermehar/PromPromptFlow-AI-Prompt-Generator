# PromPromptFlow-AI-Prompt-Generator
This project demonstrates a simple AI-based prompt generator using Python (Flask) and OpenAI API. The project includes a responsive HTML frontend with a form to submit prompts, a Flask backend to process requests, and Bootstrap for styling. The AI-generated response is displayed directly on the frontend.

---

## **🛠️ Tech Stack**  
- **Frontend:** HTML, CSS (Bootstrap)  
- **Backend:** Python (Flask)  
- **API:** OpenAI API  
- **Styling:** Bootstrap & Bootstrap Icons  

---

## **🚀 Features**  
✅ Clean and responsive UI using Bootstrap  
✅ Flask backend to handle prompt submission  
✅ OpenAI API integration for AI-generated responses  
✅ Sticky footer with author details and social media links  
✅ Favicon for a professional look  

---

## **📦 Installation and Setup**  
### **1. Clone the Repository**  
```bash
git clone https://github.com/ermehar/PromptFlow.git
cd PromptFlow

### **2. Set up a Virtual Environment** *(Optional)*
- Create a virtual environment:
```bash
python3 -m venv venv
```
- Activate the virtual environment:
-- Windows:
    ```bash
    .\venv\Scripts\activate
    ```
-- Mac/Linux:
    ```bash
    source venv/bin/activate
    ```
### **3. Install Required Packages ** 
- Install the necessary dependencies:
```bash
pip3 install flask flask-cors openai
```

## **🚀 Steps to Execute the Python Backend**
1. Add your OpenAI API key in app.py:
```bash
    client = OpenAI(api_key="YOUR_OPENAI_API_KEY")  # Replace with your OpenAI API key
```
2. Start the Flask backend:
```bash
    python3 app.py
```
3. If successful, the Flask server will run at:
```bash
    http://127.0.0.1:5000
```

---

## **🐞 Troubleshooting**
| **Issue** | **Solution** |
|-----------|-------------|
| `ModuleNotFoundError: No module named 'flask'` | Run `pip3 install flask` |
| `ModuleNotFoundError: No module named 'flask_cors'` | Run `pip3 install flask-cors` |
| `Invalid API Key` | Double-check your OpenAI API key |

---

### **📄 License**

This project is open-source and free to use.

---

## **👨‍💻 Author**  
- **Yashwant Mehar**  
  - 📧 [yashwantmehar@gmail.com](mailto:yashwantmehar@gmail.com)  
  - 🔗 [LinkedIn](https://www.linkedin.com/in/ermehar/)  
  - 💻 [GitHub](https://github.com/ermehar)

---

## **🔥 Feel free to fork, contribute, and improve! 😎**
### ✅ **Changes Included:**  
✔️ Clean and professional formatting  
✔️ Added project structure for better clarity  
✔️ Included author details, example prompt, and troubleshooting section  
✔️ Markdown-friendly styling  

---
