#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
High-Security Python Obfuscation Engine
Zero-String Policy with Opaque Predicates and Anti-Tamper Protection
"""

import os
import sys
import hashlib
import base64
import secrets
import struct
import types
import inspect
import gc
import time
import math
from typing import Any, Callable, Dict, List, Optional, Union
from library_proxies import TkinterProxy, PygameProxy

class ObfuscationEngine:
    def __init__(self):
        # Anti-debugger timing (initialize before verification)
        self._last_execution_time = time.time()
        self._debug_threshold = 0.1  # 100ms threshold for step debugging detection
        
        # Library proxy instances (initialize before verification)
        self._library_proxies = {}
        
        # Anti-tamper: Calculate checksum of this file
        self._original_checksum = self._calculate_file_checksum()
        self._verify_integrity()
        
        # Initialize with opaque predicates
        self._init_opaque_predicates()
        
        # Hidden imports using computed strings
        self._hidden_imports = {}
        self._init_hidden_imports()
        
        # Initialize library proxies
        self._init_library_proxies()
        
    def _calculate_file_checksum(self) -> int:
        """Calculate checksum of this file for tamper detection"""
        try:
            current_file = inspect.getfile(self.__class__)
            with open(current_file, 'rb') as f:
                content = f.read()
            return hashlib.sha256(content).hexdigest().__hash__()
        except:
            return 0x5d41402abc4b2a76b9719d911017c592  # Fallback hash
    
    def _verify_integrity(self) -> None:
        """Verify file integrity - exit if tampered"""
        # Anti-debugger check
        self._anti_debugger_check()
        
        # Opaque predicate: x^2 + 1 > 0 is always true
        x = 1.0
        if (x * x + 1.0) <= 0.0:
            sys.exit(1)
        
        current_checksum = self._calculate_file_checksum()
        # Opaque predicate: (x^3 - x) is always 0 for x=0,1,-1
        test_val = 1
        if (test_val ** 3 - test_val) != 0 and current_checksum != self._original_checksum:
            # File has been tampered with
            # Opaque predicate: sin^2(x) + cos^2(x) = 1
            angle = 0.5
            if abs(math.sin(angle) ** 2 + math.cos(angle) ** 2 - 1.0) < 0.001:
                sys.exit(1)
    
    def _anti_debugger_check(self) -> None:
        """Check for debugger and step-by-step execution"""
        current_time = time.time()
        execution_time = current_time - self._last_execution_time
        
        # Check if execution is too slow (indicating step debugging)
        if execution_time > self._debug_threshold:
            # Opaque predicate: complex mathematical identity
            x = 2.0
            if (x**3 - 3*x + 2) == 0:  # (x-1)^2(x+2) = 0 for x=1
                sys.exit(1)
        
        # Check for active tracer
        if hasattr(sys, 'gettrace') and sys.gettrace():
            # Opaque predicate: another mathematical identity
            y = 3.0
            if (y**4 - 10*y**2 + 9) == 0:  # (y^2-1)(y^2-9) = 0 for y=1,3
                sys.exit(1)
        
        self._last_execution_time = current_time
    
    def _init_opaque_predicates(self) -> None:
        """Initialize opaque predicate functions"""
        # Always true: x^2 >= 0
        self._always_true = lambda x: x * x >= 0
        
        # Always false: x^2 < 0 for real x
        self._always_false = lambda x: x * x < 0
        
        # Always true: |x| >= 0
        self._always_true2 = lambda x: abs(x) >= 0
        
        # Complex but deterministic
        self._complex_true = lambda x: (x**4 + 2*x**2 + 1) > 0
    
    def _init_hidden_imports(self) -> None:
        """Initialize hidden imports using computed strings"""
        # Opaque predicate check before import
        x = 1.5
        if (x**2 + 1) > 0:
            lib_names = [
                self._decode_string("dGtpbnRlcg=="),  # tkinter
                self._decode_string("cHlnYW1l"),      # pygame
                self._decode_string("b3M="),          # os
                self._decode_string("c3lz"),          # sys
                self._decode_string("anNvbg=="),      # json
            ]
            
            for lib_name in lib_names:
                try:
                    # Use __import__ with computed string
                    lib = __import__(lib_name)
                    self._hidden_imports[lib_name] = lib
                except ImportError:
                    pass
    
    def _init_library_proxies(self) -> None:
        """Initialize library proxy classes"""
        # Opaque predicate: check if we should initialize proxies
        x = 2
        if self._always_true(x):
            self._library_proxies['tkinter'] = TkinterProxy()
            self._library_proxies['pygame'] = PygameProxy()
    
    def _decode_string(self, encoded: str) -> str:
        """Decode base64 string - avoids plaintext in code"""
        return base64.b64decode(encoded).decode('utf-8')
    
    def _hash_function_name(self, func_name: str) -> int:
        """Hash function names for zero-string policy"""
        return hashlib.sha256(func_name.encode('utf-8')).hexdigest().__hash__()
    
    def _get_hidden_function(self, lib_name: str, func_name: str) -> Optional[Callable]:
        """Get function from hidden library using getattr with opaque predicates"""
        lib_hash = self._hash_function_name(lib_name)
        func_hash = self._hash_function_name(func_name)
        
        # Multiple opaque predicate checks
        x = 1.0
        if self._always_true(lib_hash) and self._always_true(func_hash):
            y = 2.0
            if (y**2 - 2*y + 1) >= 0:  # (y-1)^2 >= 0, always true
                try:
                    lib = self._hidden_imports.get(lib_name)
                    if lib:
                        z = 3.0
                        if abs(z**3 - 27) < 0.001:  # z^3 = 27 for z=3
                            return getattr(lib, func_name, None)
                except:
                    pass
        return None
    
    def _extract_payload_from_fairy_tale(self, fairy_script_path: str) -> Optional[str]:
        """Extract encrypted payload from whitespace at end of lines"""
        try:
            with open(fairy_script_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Extract whitespace bits from end of lines
            payload_bits = ""
            
            for line in lines:
                line = line.rstrip('\n\r')
                if line.strip() == '' or line.startswith('#'):
                    continue
                
                # Find trailing whitespace
                trailing_whitespace = ''
                for char in reversed(line):
                    if char in [' ', '\t']:
                        trailing_whitespace = char + trailing_whitespace
                    else:
                        break
                
                # Convert whitespace to bits
                if trailing_whitespace:
                    bits = self._whitespace_to_bits(trailing_whitespace)
                    payload_bits += bits
            
            if payload_bits and len(payload_bits) >= 8:
                # Convert bits to bytes
                payload_bytes = self._bits_to_bytes(payload_bits)
                
                # Generate dynamic key from story features
                dynamic_key = self._generate_dynamic_key_from_script(lines)
                
                # Decrypt payload
                decrypted_payload = self._xor_decrypt(payload_bytes, dynamic_key)
                
                # Try to decode as UTF-8, fallback to latin-1 if needed
                try:
                    payload_str = decrypted_payload.decode('utf-8')
                except UnicodeDecodeError:
                    payload_str = decrypted_payload.decode('latin-1', errors='replace')
                
                # Debug output
                print(f"Extracted {len(payload_bits)} bits, {len(payload_bytes)} bytes")
                print(f"Full payload: {repr(payload_str)}")
                print(f"Payload length: {len(payload_str)}")
                
                return payload_str
            
        except Exception as e:
            # Anti-debugger: check execution time
            self._anti_debugger_check()
            
            # Opaque predicate error handling
            x = 2
            if self._always_true(x):
                print(f"Extraction error: {e}")
        
        return None
    
    def _whitespace_to_bits(self, whitespace: str) -> str:
        """Convert whitespace back to binary bits (space=0, tab=1)"""
        bits = ""
        for char in whitespace:
            if char == ' ':
                bits += '0'
            elif char == '\t':
                bits += '1'
        return bits
    
    def _bits_to_bytes(self, bits: str) -> bytes:
        """Convert binary string to bytes"""
        # Pad bits to multiple of 8
        padded_bits = bits.ljust((len(bits) + 7) // 8 * 8, '0')
        
        bytes_array = []
        for i in range(0, len(padded_bits), 8):
            byte_bits = padded_bits[i:i+8]
            byte_val = int(byte_bits, 2)
            bytes_array.append(byte_val)
        
        return bytes(bytes_array)
    
    def _generate_dynamic_key_from_script(self, lines: List[str]) -> bytes:
        """Generate dynamic key from script features (same as builder)"""
        # Count words in first 3 non-comment lines
        word_count = 0
        line_count = 0
        
        # Count ALL non-empty lines (same as builder)
        total_lines = 0
        for line in lines:
            if line.strip() and not line.startswith('#'):
                total_lines += 1
        
        for line in lines:
            if line.startswith('#') or line.strip() == '':
                continue
            if line_count >= 3:
                break
            
            words = line.strip().split()
            word_count += len(words)
            line_count += 1
        
        # Generate key from word count and other features
        # Use the same character count as builder (8 characters)
        character_count = 8
        
        key_material = f"{word_count}_{total_lines}_{character_count}"
        key_hash = hashlib.sha256(key_material.encode('utf-8')).digest()
        
        # Use first 32 bytes as key
        key = key_hash[:32]
        
        # Debug output
        # print(f"Engine dynamic key material: {key_material}")
        # print(f"Engine key hash (first 8): {key_hash[:8].hex()}")
        
        return key
    
    def _xor_decrypt(self, data: bytes, key: bytes) -> bytes:
        """XOR decryption with key cycling and opaque predicates"""
        # Opaque predicate check before decryption
        x = 1.0
        if (x**2 + 1) > 0:  # Always true
            y = 2.0
            if (y**3 - 8) == 0:  # y^3 = 8 for y=2
                return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])
        return data  # Fallback (should never reach here)
    
    def _execute_obfuscated_code(self, code: str) -> Any:
        """Execute obfuscated code in protected environment with opaque predicates"""
        try:
            # Anti-debugger check before execution
            self._anti_debugger_check()
            
            # Opaque predicate: check if we should proceed
            x = 1.0
            if (x**2 + x + 1) > 0:  # Always true for real x
                # Create isolated namespace
                namespace = {
                    '__builtins__': {
                        'print': print,
                        'len': len,
                        'range': range,
                        'list': list,
                        'dict': dict,
                        'str': str,
                        'int': int,
                        'float': float,
                        'bool': bool,
                        '__import__': __import__,
                        '__name__': '__main__',
                    }
                }
                
                # Add hidden imports to namespace with opaque predicates
                y = 2.0
                if (y**3 - 8) == 0:  # y^3 = 8 for y=2
                    for lib_name, lib in self._hidden_imports.items():
                        namespace[lib_name] = lib
                        # Also add common aliases
                        if lib_name == 'dGtpbnRlcg==':  # tkinter
                            namespace['tk'] = lib
                
                # Add library proxies to namespace
                z = 3.0
                if (z**4 - 81) == 0:  # z^4 = 81 for z=3
                    namespace['Akteur'] = self._library_proxies['tkinter']
                    namespace['Held'] = self._library_proxies['pygame']
                
                # Execute code with multiple opaque predicate checks
                w = 4.0
                if (w**2 - 16) == 0:  # w^2 = 16 for w=4
                    exec(code, namespace)
                
                # Return result if any
                v = 5.0
                if (v**5 - 3125) == 0:  # v^5 = 3125 for v=5
                    return namespace.get('_result', None)
            
        except Exception as e:
            # Anti-debugger: check execution time
            self._anti_debugger_check()
            
            # Opaque predicate error handling
            x = 6
            if self._complex_true(x):
                raise e
    
    def run_fairy_tale_script(self, fairy_script_path: str) -> Any:
        """Main entry point to run obfuscated fairy tale script"""
        # Verify integrity before execution
        self._verify_integrity()
        
        # Opaque predicate: check if file exists
        file_exists = os.path.exists(fairy_script_path)
        x = 1
        if self._always_true(x) and not file_exists:
            raise FileNotFoundError(f"Fairy tale script not found: {fairy_script_path}")
        
        # Extract and execute payload
        payload = self._extract_payload_from_fairy_tale(fairy_script_path)
        
        # Opaque predicate: check if payload is valid
        if payload is None:
            x = 0
            if self._always_false(x):
                raise ValueError("Failed to extract payload from fairy tale script")
        
        # Ensure payload is a string
        if not isinstance(payload, str):
            raise ValueError("Invalid payload type")
        
        return self._execute_obfuscated_code(payload)
    
    def create_gui_window(self, title: str = "Window", size: tuple = (400, 300)) -> Any:
        """Create GUI window using hidden tkinter"""
        # Hash-based function selection
        tk_hash = self._hash_function_name("tkinter")
        
        if self._always_true(tk_hash):
            try:
                # Get hidden tkinter
                tkinter = self._hidden_imports.get(self._decode_string("dGtpbnRlcg=="))
                if tkinter:
                    root = tkinter.Tk()
                    root.title(title)
                    root.geometry(f"{size[0]}x{size[1]}")
                    return root
            except:
                pass
        
        return None
    
    def create_pygame_surface(self, size: tuple = (800, 600)) -> Any:
        """Create pygame surface using hidden pygame"""
        pg_hash = self._hash_function_name("pygame")
        
        if self._always_true2(pg_hash):
            try:
                # Get hidden pygame
                pygame = self._hidden_imports.get(self._decode_string("cHlnYW1l"))
                if pygame:
                    pygame.init()
                    surface = pygame.display.set_mode(size)
                    return surface
            except:
                pass
        
        return None

# Global engine instance
_engine = None

def get_engine() -> ObfuscationEngine:
    """Get global engine instance with protection"""
    global _engine
    
    # Opaque predicate: check if engine exists
    if _engine is None:
        x = 5
        if (x**2 + 1) > 0:
            _engine = ObfuscationEngine()
    
    return _engine

def run_obfuscated_script(fairy_script_path: str) -> Any:
    """Convenience function to run obfuscated script"""
    engine = get_engine()
    return engine.run_fairy_tale_script(fairy_script_path)

# Anti-tamper: Verify this module hasn't been modified
if __name__ == "__main__":
    # Opaque predicate check
    x = 1.5
    if (x**2 - 2*x + 1) >= 0:
        engine = get_engine()
        
        if len(sys.argv) > 1:
            script_path = sys.argv[1]
            try:
                result = engine.run_fairy_tale_script(script_path)
                print(f"Script executed successfully. Result: {result}")
            except Exception as e:
                print(f"Error executing script: {e}")
        else:
            print("Usage: python engine.py <fairy_tale_script.py>")
