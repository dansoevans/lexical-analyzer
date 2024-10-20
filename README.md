


### **Project Title:**  
JSON Scanner – Lexical Analyzer

---

### **Description:**  
This project is a **JSON scanner** implemented in Python, designed to perform **lexical analysis** by breaking JSON input into meaningful tokens such as strings, numbers, booleans, braces, and commas. It accepts **JSON input directly from the user** via the console and returns a sequence of tokens representing the input.

---

### **How to Run:**  

1. **Ensure Python 3.x is installed** on your system.
2. Save the code in a file named **`json_scanner.py`**.
3. Open a terminal or command prompt and run the following command:
   ```bash
   python json_scanner_console.py
   ```

4. **When prompted**, enter a valid JSON object.

---

### **Example Run:**

```bash
Enter a JSON object: {"name": "Rockerfeller", "age": 23, "isStudent": false}
```

**Output:**
```
('LBRACE', '{')
('STRING', '"name"')
('COLON', ':')
('STRING', '"Rockerfeller"')
('COMMA', ',')
('STRING', '"age"')
('COLON', ':')
('NUMBER', '23')
('COMMA', ',')
('STRING', '"isStudent"')
('COLON', ':')
('TRUE', 'true')
('RBRACE', '}')
```

---

### **Project Requirements:**  
- **Python 3.x**  
- JSON input must follow the correct syntax to avoid errors.

---

### **Token Types:**
- **STRING**: `"..."` (Text enclosed in double quotes)  
- **NUMBER**: Integers, floats, and numbers in scientific notation  
- **BOOLEAN**: `true` or `false`  
- **NULL**: `null`  
- **BRACES & BRACKETS**: `{`, `}`, `[`, `]`  
- **COMMA & COLON**: `,` and `:`  

---

### **Error Handling:**  
- If the input contains invalid characters or syntax, the program will **raise an error** specifying the position where the issue occurred.

---


### **Credits:**  
Developed by Evans Danso for **CSCI 2115 Final Project 1– Theory of Computer Science**.
