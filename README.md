Overview
This system provides a method for protecting Python code by steganographically embedding it within generated texts (such as narrative stories). The actual code is encoded via invisible spaces and tabs at the end of each line to encapsulate the script's functionality in an inconspicuous manner.

Features
Protection Mechanisms
No Plaintext Strings: Avoidance of readable strings in the output code.

Dynamic Key Generation: XOR keys are based on the structural properties of the text.

Environment Checks: Basic verification of the runtime and execution environment.

Integrity Protection: SHA-256 checksum verification against modifications.

Mathematical Obfuscation: Use of opaque predicates for complex control structures.

Import Management: Base64-encoded and protected module imports.

Steganographic Features
Text Embedding: Code is packaged within generated narratives.

Whitespace Encoding: Storage of the data structure in invisible spaces and tabs.

Dynamic Text Generation: Each build process creates entirely new text structures.

Polymorphic Output: Different file signatures for each iteration.

Quick Start
Installation
Bash
# Clone or download the files
git clone https://github.com/Sirenkonett/Python-Stealth-Obfuscator.git
cd stealth-obfuscation

# Install dependencies (if required)
pip install requests pycryptodome
Basic Usage
Bash
# Process and embed the Python code
python builder_v2.py your_script.py output.py

# Execute the processed code
python engine.py output.py
File Structure
Plaintext
stealth-obfuscation/
├── builder_v2.py      # Main program for code embedding
├── engine.py          # Execution environment with integrity checks
├── README.md          # This file
└── your_files/        # Your Python scripts to be processed
How It Works
1. Embedding Process (builder_v2.py)
Read Input: The source Python script is loaded.

Calculate Capacity: Determines the required lines and bits for embedding.

Text Generation: Creates a text with the exact required character capacity.

Dynamic Key: Generates a cryptographic key from the text features.

Encrypt Data: Performs an XOR encryption of the code.

Whitespace Injection: Converts the encrypted bits into spaces and tabs.

Save Output: Saves the generated text with the embedded code.

2. Execution Process (engine.py)
System Checks: Integrity and runtime verification.

Extract Data: Reads the invisible characters and converts them back into bits.

Generate Key: Reconstructs the dynamic key based on the text.

Decrypt Data: Decrypts the embedded code.

Execute Code: Starts the original script in an isolated namespace.

Customization Guide
Modifying the Builder (builder_v2.py)
Change Text Templates
Python
self.story_templates = [
    "Once upon a time, the {character} who {action} in the {location}. {junk_sentence}",
    "In a distant {location} lived the {character}, who {action}. {junk_sentence}",
    # Add your own templates here
]
Add New Variables
Python
self.characters = ["Prince", "King", "Researcher", "Scholar", "YourCharacter"]
self.locations = ["Forest", "Mountain", "Laboratory", "Archive", "YourLocation"]
self.actions = ["searched", "found", "analyzed", "built", "YourAction"]
Modify Encryption
Python
def _xor_encrypt(self, data: bytes, key: bytes) -> bytes:
    # Can be replaced with other encryption algorithms
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])
Modifying the Engine (engine.py)
Adjust System Checks
Python
def _environment_check(self):
    # Adjust thresholds for timing analysis
    self._timing_threshold = 0.05  # 50ms instead of 100ms
    
    # Add new verification methods
    if hasattr(sys, 'gettrace') and sys.gettrace():
        return True
    return False
Modify Key Generation
Python
def _generate_dynamic_key_from_script(self, script_lines: List[str]) -> bytes:
    # Change the method of key generation
    word_count = len(script_lines[1].split())
    total_lines = len([l for l in script_lines if l.strip()])
    key_material = f"{word_count}_{total_lines}_8"
    return hashlib.sha256(key_material.encode('utf-8')).digest()[:32]
Add New Opaque Predicates
Python
# Add mathematical identities that always evaluate to True
x = 5.0
if (x**2 - 25) == 0:  # x² = 25 for x=5
    # Your code here
Advanced Features
Automatic Capacity Adjustment
The system automatically calculates the required text size:

Small scripts: ~50-100 lines

Medium scripts: ~200-400 lines

Large scripts: ~500+ lines

Multiple Output Formats  
Bash
# Generate different text styles
python builder_v2.py script.py output1.py
Batch Processing  
Python
# Process multiple files
import glob
import os
import subprocess

for script in glob.glob("scripts/*.py"):
    output = f"obfuscated/{os.path.basename(script)}"
    subprocess.run(["python", "builder_v2.py", script, output])
Technical Characteristics and Limitations
Code Analysis Properties
Static Analysis: Avoids storing strings in plaintext.

Signature Detection: Generates polymorphic output on every operation.

Runtime Analysis: Utilizes basic checks of the execution environment.

Limitations
Dynamic Analysis: The script's behavior remains analyzable during execution.

Memory Analysis: The code exists in memory during runtime.

Network Traffic: The embedding does not affect network calls of the original script.

Best Practices
Thorough testing of the processed code prior to production use.

Use different keys for each deployment.

Combine with other methods (e.g., standard packers) for enhanced software protection.

Verify compatibility, especially with complex module dependencies.

Troubleshooting
Common Issues
"Data truncated" Error
Bash
# Increase capacity in builder_v2.py
bits_per_line = 64  # Increase from 32
total_lines = needed_lines + 50  # Enlarge safety margin
"Key mismatch" Error
Bash
# Ensure both files use the same key generation
# Check word counting logic
# Verify consistency of line counting
"GUI not appearing"
Bash
# Add required imports to the engine namespace
namespace['tk'] = lib  # For tkinter as tk
namespace['__name__'] = '__main__'  # For if __name__ == '__main__'
Debug Mode
Enable debug output in engine.py:

Python
# Uncomment these lines for error analysis
print(f"Extracted {len(data_bits)} bits, {len(data_bytes)} bytes")
print(f"Full data: {repr(data_str)}")
Examples
Simple GUI Application
Python
# test.py
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Test Window")
    root.geometry("300x200")
    
    label = tk.Label(root, text="Test successfully executed!")
    label.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()
Development Guide
Adding New Features
1. New Encryption Method
Python
class AdvancedBuilder(StealthBuilderV2):
    def _aes_encrypt(self, data: bytes, key: bytes) -> bytes:
        from Crypto.Cipher import AES
        cipher = AES.new(key, AES.MODE_GCM)
        return cipher.encrypt(data)
2. New Text Themes
Python
# Add scientific text templates
self.science_templates = [
    "The {character} conducted the {action} in the {location}. {junk_sentence}",
    "Research indicated that {character} {action} in {location}. {junk_sentence}",
]
3. API Obfuscation  
Python
def _obfuscate_api_calls(self, code: str) -> str:
    # Replace direct calls with indirect imports
    code = code.replace("requests.post", "__import__('requests').post")
    return code
License  
This code is for educational purposes and the research of steganographic concepts only. Users are responsible for complying with applicable laws and regulations.  

Contributing
Fork the repository

Create a feature branch

Add your improvements

Submit a Pull Request

Support
For issues and questions:

Create an issue on GitHub

Check the troubleshooting section

Review the examples

Disclaimer: This tool was developed exclusively for educational and research purposes in the field of software protection and steganography. Users must comply with all applicable local and international laws.
