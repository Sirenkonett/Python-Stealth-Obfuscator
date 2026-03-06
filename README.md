# Python-Stealth-Obfuscator[README.md](https://github.com/user-attachments/files/25792698/README.md)
# 🕵️‍♂️ Stealth Python Obfuscation System

**High-Security Python Code Obfuscation with Fairy Tale Camouflage**

## 📋 Overview

This system provides military-grade code obfuscation by hiding malicious Python code inside seemingly innocent fairy tale stories. The code is encoded in invisible whitespace characters (spaces and tabs) at the end of each line, making it completely undetectable by static analysis tools.

## 🎯 Features

### 🛡️ Security Features
- **Zero-String Policy**: No plaintext strings in the obfuscated code
- **Dynamic Key Generation**: XOR keys generated from story features
- **Anti-Debugger Protection**: Timing and tracer detection
- **Anti-Tamper Protection**: SHA-256 checksum verification
- **Opaque Predicates**: Mathematical identities for obfuscation
- **Library Hiding**: Hidden imports with base64 encoding

### 🎭 Stealth Features
- **Fairy Tale Camouflage**: Code hidden in innocent-looking stories
- **Whitespace Encoding**: Payload stored in invisible spaces/tabs
- **Dynamic Story Generation**: Each build creates unique stories
- **Polymorphic Output**: Different obfuscation each time

## 🚀 Quick Start

### Installation
```bash
# Clone or download the files
git clone <repository-url>
cd stealth-obfuscation

# Install dependencies (if needed)
pip install requests pycryptodome
```

### Basic Usage
```bash
# Obfuscate your Python code
python builder_v2.py your_script.py output.py

# Execute the obfuscated code
python engine.py output.py
```

## 📁 File Structure

```
stealth-obfuscation/
├── builder_v2.py      # Enhanced obfuscation builder
├── engine.py          # Execution engine with security checks
├── README.md          # This file
└── your_files/       # Your Python scripts to obfuscate
```

## 🔧 How It Works

### 1. Obfuscation Process (`builder_v2.py`)
1. **Read Input**: Your Python script is loaded
2. **Calculate Capacity**: Determines required lines and bits
3. **Generate Story**: Creates unique fairy tale with exact capacity
4. **Dynamic Key**: Generates XOR key from story features
5. **Encrypt Payload**: XOR-encrypts your code with the key
6. **Whitespace Injection**: Converts encrypted bits to spaces/tabs
7. **Write Output**: Saves fairy tale with hidden payload

### 2. Execution Process (`engine.py`)
1. **Security Checks**: Anti-debugger and anti-tamper verification
2. **Extract Payload**: Reads whitespaces and converts to bits
3. **Generate Key**: Recreates the same dynamic key
4. **Decrypt Payload**: XOR-decrypts the hidden code
5. **Execute Code**: Runs your original Python in isolated namespace

## 🛠️ Customization Guide

### Modifying the Builder (`builder_v2.py`)

#### Change Story Templates
```python
self.fairy_tale_templates = [
    "Es war einmal {character}, der {action} im {location}. {junk_sentence}",
    "In einem fernen {location} lebte {character}, der {action}. {junk_sentence}",
    # Add your own templates here
]
```

#### Add New Characters/Locations
```python
self.characters = ["Prinz", "König", "Ritter", "Zauberer", "YourCharacter"]
self.locations = ["Wald", "Berg", "Tal", "Schloss", "YourLocation"]
self.actions = ["suchte", "fand", "verlor", "baute", "YourAction"]
```

#### Modify Encryption
```python
def _xor_encrypt(self, data: bytes, key: bytes) -> bytes:
    # Replace with your own encryption algorithm
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])
```

### Modifying the Engine (`engine.py`)

#### Change Security Checks
```python
def _anti_debugger_check(self):
    # Modify timing threshold
    self._debug_threshold = 0.05  # 50ms instead of 100ms
    
    # Add new detection methods
    if hasattr(sys, 'gettrace') and sys.gettrace():
        return True
    return False
```

#### Modify Key Generation
```python
def _generate_dynamic_key_from_script(self, script_lines: List[str]) -> bytes:
    # Change how keys are generated
    word_count = len(script_lines[1].split())  # Different calculation
    total_lines = len([l for l in script_lines if l.strip()])
    key_material = f"{word_count}_{total_lines}_8"
    return hashlib.sha256(key_material.encode('utf-8')).digest()[:32]
```

#### Add New Opaque Predicates
```python
# Add mathematical identities that always evaluate to True
x = 5.0
if (x**2 - 25) == 0:  # x² = 25 for x=5
    # Your code here
```

## 🔍 Advanced Features

### Custom Payload Capacity
The system automatically calculates required capacity:
- **Small scripts**: ~50-100 lines
- **Medium scripts**: ~200-400 lines  
- **Large scripts**: ~500+ lines

### Multiple Output Formats
```bash
# Generate different fairy tale styles
python builder_v2.py script.py output1.py  # German fairy tales
# Modify builder for English, French, etc.
```

### Batch Processing
```python
# Process multiple files
import glob
for script in glob.glob("scripts/*.py"):
    output = f"obfuscated/{os.path.basename(script)}"
    subprocess.run(["python", "builder_v2.py", script, output])
```

## ⚠️ Security Considerations

### What This System Evades
- **Static Analysis**: No suspicious strings in plain text
- **Signature Detection**: Polymorphic output each time
- **Pattern Recognition**: Hidden in innocent-looking content
- **Basic Debugging**: Anti-debugger protections

### Limitations
- **Dynamic Analysis**: Can be detected during execution
- **Memory Analysis**: Payload exists in memory when running
- **Network Traffic**: Obfuscation doesn't hide network calls

### Best Practices
1. **Always test** obfuscated code before deployment
2. **Use different keys** for each deployment
3. **Combine with other techniques** (packers, runtime encryption)
4. **Monitor detection** of your specific use case

## 🐛 Troubleshooting

### Common Issues

#### "Payload truncated" Error
```bash
# Increase capacity in builder_v2.py
bits_per_line = 64  # Increase from 32
total_lines = needed_lines + 50  # Add more safety margin
```

#### "Key mismatch" Error
```bash
# Ensure both files use same key generation
# Check word counting logic in both files
# Verify line counting consistency
```

#### "GUI not appearing" 
```bash
# Add required imports to engine.py namespace
namespace['tk'] = lib  # For tkinter as tk
namespace['__name__'] = '__main__'  # For if __name__ == '__main__'
```

### Debug Mode
Enable debug output in `engine.py`:
```python
# Uncomment these lines for debugging
print(f"Extracted {len(payload_bits)} bits, {len(payload_bytes)} bytes")
print(f"Full payload: {repr(payload_str)}")
```

## 📚 Examples

### Simple GUI Application
```python
# test.py
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Test Window")
    root.geometry("300x200")
    
    label = tk.Label(root, text="Stealth Test Successful!")
    label.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()
```


## 🔧 Development Guide

### Adding New Features

#### 1. New Encryption Method
```python
class AdvancedBuilder(StealthBuilderV2):
    def _aes_encrypt(self, data: bytes, key: bytes) -> bytes:
        from Crypto.Cipher import AES
        cipher = AES.new(key, AES.MODE_GCM)
        return cipher.encrypt(data)
```

#### 2. New Story Themes
```python
# Add different camouflage themes
self.science_templates = [
    "The {character} conducted {action} in the {location}. {junk_sentence}",
    "Research showed {character} {action} at {location}. {junk_sentence}",
]
```

#### 3. Network Obfuscation
```python
def _obfuscate_network_calls(self, code: str) -> str:
    # Replace direct network calls with obfuscated versions
    code = code.replace("requests.post", "__import__('requests').post")
    return code
```

## 📄 License

This code is for educational purposes only. Users are responsible for complying with local laws and regulations.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Submit a pull request

## 📞 Support

For issues and questions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review the examples

---

**⚠️ Disclaimer**: This tool is designed for educational and research purposes only. Users must comply with applicable laws and regulations.
