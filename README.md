Abstract
This repository provides an advanced framework for Python code protection utilizing text-based steganography. The system encapsulates functional Python scripts within procedurally generated natural language narratives. The executable payload is encoded via invisible whitespace manipulation (spaces and tabs) at the end of each line, allowing the code to remain fully operational while appearing as standard text files to static analysis tools.

Core Capabilities
Security & Protection Mechanisms
Zero-Plaintext Footprint: Eliminates readable strings in the output source, mitigating basic static analysis and signature detection.

Context-Aware Cryptography: Cryptographic XOR keys are dynamically derived from the structural entropy and linguistic properties of the generated carrier text.

Anti-Analysis Heuristics: Implements runtime environment verification and execution timing checks to detect debugging attempts.

Integrity Verification: Utilizes SHA-256 checksums to prevent tampering and ensure payload integrity prior to execution.

Control Flow Obfuscation: Employs opaque predicates and mathematical identities to complicate control flow graphs.

Protected Imports: Secures module dependencies via base64-encoded, dynamically resolved imports.

Steganographic Architecture
Narrative Embedding: Payloads are steganographically hidden within auto-generated text bodies.

Whitespace Encoding: Translates binary payload data into non-printing characters, preserving the visual structure of the carrier text.

Polymorphic Generation: Each build process yields a unique file signature and text structure, ensuring high variance across deployments.

Getting Started
Prerequisites
Python 3.8 or higher

Required packages: requests, pycryptodome

Installation
Bash
# Clone the repository
git clone https://github.com/Sirenkonett/Python-Stealth-Obfuscator.git
cd stealth-obfuscation

# Install dependencies
pip install requests pycryptodome
Basic Usage
The system consists of two primary components: the builder (encoder) and the engine (decoder/executor).

Bash
# Encode and embed the target Python script
python builder_v2.py source_script.py generated_output.py

# Execute the steganographically embedded script
python engine.py generated_output.py
System Architecture
1. The Encoder (builder_v2.py)
Capacity Allocation: Analyzes the target script to determine the requisite bit capacity and text length.

Carrier Generation: Synthesizes a narrative text meeting the exact structural requirements for the payload.

Key Derivation: Generates a cryptographic key strictly based on the structural metrics of the synthesized text.

Payload Encryption: Applies XOR encryption to the compiled target script.

Steganographic Injection: Translates the encrypted binary sequence into trailing whitespaces and injects them into the carrier text.

2. The Execution Engine (engine.py)
Heuristic Validation: Executes environmental and temporal checks to detect analysis environments.

Payload Extraction: Parses the carrier text, isolating and decoding the steganographic whitespace sequence.

Key Reconstruction: Recalculates the cryptographic key using the same structural metrics as the encoder.

Decryption & Execution: Decrypts the payload and executes it within an isolated, dynamically constructed Python namespace.

API & Extensibility
The framework is designed to be highly modular. Researchers can easily adapt the core components for custom implementations.

Customizing the Carrier Text (builder_v2.py)
You can modify the semantic structure of the generated text by altering the generation dictionaries:

Python
self.story_templates = [
    "The analysis of {subject} demonstrated that {action} occurred in the {environment}. {junk_data}",
    "Initial findings regarding {subject} suggest {action} within the {environment}. {junk_data}",
]

self.subjects = ["Dataset A", "Component B", "Module C", "Subsystem D"]
self.environments = ["runtime environment", "isolated container", "memory space"]
Extending Anti-Analysis Checks (engine.py)
Environmental validation can be customized to include stricter runtime constraints:

Python
def _verify_execution_environment(self) -> bool:
    # Tighten timing analysis constraints (e.g., 50ms variance)
    self._timing_variance_threshold = 0.05 
    
    # Check for active tracing tools
    import sys
    if hasattr(sys, 'gettrace') and sys.gettrace() is not None:
        return False
        
    return True
Implementing Alternative Cryptography
The default XOR encryption can be swapped for industry-standard algorithms:

Python
def _encrypt_payload(self, data: bytes, key: bytes) -> bytes:
    from Crypto.Cipher import AES
    # Note: Requires IV management implementation
    cipher = AES.new(key, AES.MODE_GCM)
    return cipher.encrypt(data)
Threat Model & Technical Limitations
When evaluating this tool for software protection, please note the following architectural limitations:

In-Memory Exposure: The decrypted payload ultimately resides in memory during execution. Advanced memory dumping techniques or dynamic instrumentation (e.g., Frida) can extract the original code.

Network Transparency: This framework obfuscates the script on disk but does not intercept or encrypt network traffic generated by the underlying payload.

Behavioral Signatures: While the static file signature is highly polymorphic, the runtime behavior of the executed script remains unchanged and can be identified by behavioral analysis sandboxes.

Recommendation: For robust software protection, this steganographic layer should be utilized as part of a defense-in-depth strategy, combined with native code compilation (e.g., Cython) and process-hollowing prevention mechanisms.

Troubleshooting
Payload Truncation / Data Loss: If the encoded script is too large for the generated text, increase the bit-per-line capacity in builder_v2.py (e.g., bits_per_line = 64) or increase the structural safety margin.

Cryptographic Key Mismatch: Ensure that the text parsing logic (e.g., line and word counting) is perfectly synchronized between builder_v2.py and engine.py. Any whitespace alteration by an IDE or text editor will corrupt the payload.

GUI Framework Issues: When wrapping GUI applications (like tkinter or PyQt), ensure all necessary top-level modules are explicitly injected into the execution namespace within engine.py.

License & Legal Disclaimer
This repository is licensed under the MIT License.

Disclaimer: This framework is developed and published strictly for academic research, educational purposes, and the study of steganography and software obfuscation techniques. The author(s) assume no liability and are not responsible for any misuse or damage caused by this program. Users must adhere to all applicable local, state, and federal laws when utilizing this software.
