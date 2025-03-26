# **ChatGPT API Project (Python + HTML)**

This project demonstrates how to create a simple web-based UI to interact with the ChatGPT API using a Python Flask backend. The user can enter a prompt through the frontend, send it to the backend, and receive a generated response in HTML format.

---

## **🛠️ Requirements**
- Python 3.8 or later  
- OpenAI API Key  

---

## **📦 Installation**
### **1. Install Python**
- Download and install Python from the official website: [https://www.python.org](https://www.python.org)  

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

## **🌐 Steps to Open and Use the HTML File**
1. Open index.html in your browser.
2. Enter a prompt in the text area.
3. Click Submit to send the prompt to the backend.
4. The generated response will be displayed below the text area.


## **🧪 Example Prompt**

```text
    Write a blog about the benefits of AI in healthcare.
```
### **✅ Example Output**
    - AI improves diagnosis accuracy.
    - AI automates administrative tasks.
    - AI helps with personalized treatment plans.

## **🐞 Troubleshooting**
| **Issue** | **Solution** |
|-----------|-------------|
| `ModuleNotFoundError: No module named 'flask'` | Run `pip3 install flask` |
| `ModuleNotFoundError: No module named 'flask_cors'` | Run `pip3 install flask-cors` |
| `Invalid API Key` | Double-check your OpenAI API key |


### **📄 License**

This project is open-source and free to use.