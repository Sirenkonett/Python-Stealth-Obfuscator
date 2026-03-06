#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enhanced Stealth Obfuscation Builder v2.0
Guaranteed complete payload extraction
"""

import os
import sys
import random
import hashlib
import base64
import secrets
from typing import Dict, List, Tuple, Any

class StealthBuilderV2:
    def __init__(self):
        self.fairy_tale_templates = [
            "Es war einmal {character}, der {action} im {location}. {junk_sentence}",
            "In einem fernen {location} lebte {character}, der {action}. {junk_sentence}",
            "Der {character} {action} durch den {location}. {junk_sentence}",
            "{character} begab sich in den {location}, um zu {action}. {junk_sentence}",
            "Im {location} traf {character} auf eine Herausforderung: {action}. {junk_sentence}"
        ]
        
        self.characters = ["Prinz", "König", "Ritter", "Zauberer", "Bauer", "Händler", "Schmied", "Jäger"]
        self.locations = ["Wald", "Berg", "Tal", "Schloss", "Dorf", "Fluss", "See", "Garten"]
        self.actions = ["suchte", "fand", "verlor", "baute", "zerstörte", "erschuf", "entdeckte", "bewachte"]
        self.events = ["erschien ein Drache", "begann ein Sturm", "fiel ein Fluch", "öffnete sich ein Tor", "verschwand etwas"]
        self.junk_sentences = [
            "Die Vögel sangen ihre schönsten Lieder.",
            "Die Sonne schien hell durch die Blätter.",
            "Ein leichter Wind wehte durch die Bäume.",
            "Die Blüten dufteten wunderbar."
        ]
    
    def _xor_encrypt(self, data: bytes, key: bytes) -> bytes:
        """XOR encryption with key cycling"""
        return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])
    
    def _create_enhanced_fairy_tale(self, payload_code: str) -> str:
        """Create fairy tale with guaranteed payload capacity"""
        # Calculate required capacity
        payload_bytes = payload_code.encode('utf-8')
        payload_bits = len(payload_bytes) * 8
        
        # Calculate needed lines (32 bits per line = 4 bytes per line)
        bits_per_line = 32
        needed_lines = (payload_bits + bits_per_line - 1) // bits_per_line
        
        # Add extra lines for safety margin
        total_lines = needed_lines + 10
        
        print(f"Payload: {len(payload_bytes)} bytes, {payload_bits} bits")
        print(f"Needed lines: {needed_lines}, Total lines: {total_lines}")
        
        # Generate fairy tale
        fairy_script_lines = []
        fairy_script_lines.append("# Märchen-Script mit verborgener Weisheit")
        fairy_script_lines.append("")
        
        # Generate exact number of lines needed
        for i in range(total_lines):
            template = random.choice(self.fairy_tale_templates)
            character = random.choice(self.characters)
            location = random.choice(self.locations)
            action = random.choice(self.actions)
            junk = random.choice(self.junk_sentences)
            
            fairy_line = template.format(
                character=character,
                location=location,
                action=action,
                junk_sentence=junk
            )
            fairy_script_lines.append(fairy_line)
        
        # Generate dynamic key
        dynamic_key = self._generate_dynamic_key(fairy_script_lines)
        
        # Encrypt payload
        encrypted_payload = self._xor_encrypt(payload_bytes, dynamic_key)
        
        # Convert to bits
        payload_bits_str = ''.join(format(byte, '08b') for byte in encrypted_payload)
        
        # Inject payload into ALL lines
        lines_with_payload = []
        bit_index = 0
        
        for line in fairy_script_lines:
            if line.startswith('#') or line.strip() == '':
                lines_with_payload.append(line)
                continue
            
            if bit_index < len(payload_bits_str):
                # Extract bits for this line
                bits_to_inject = min(bits_per_line, len(payload_bits_str) - bit_index)
                current_bits = payload_bits_str[bit_index:bit_index + bits_to_inject]
                
                # Convert to whitespace
                whitespace_payload = self._bits_to_whitespace(current_bits)
                
                # Add line with payload
                lines_with_payload.append(line + whitespace_payload)
                bit_index += bits_to_inject
            else:
                # No more payload bits, add line without payload
                lines_with_payload.append(line)
        
        print(f"Injected {bit_index} bits into {len(lines_with_payload)} lines")
        
        return "\n".join(lines_with_payload)
    
    def _generate_dynamic_key(self, fairy_lines: List[str]) -> bytes:
        """Generate dynamic XOR key from story features"""
        word_count = 0
        line_count = 0
        
        # Count words in first 3 non-comment lines
        for line in fairy_lines:
            if line.startswith('#') or line.strip() == '':
                continue
            if line_count >= 3:
                break
            
            words = line.strip().split()
            word_count += len(words)
            line_count += 1
        
        # Count total non-empty lines
        total_lines = sum(1 for line in fairy_lines if line.strip() and not line.startswith('#'))
        
        # Generate key
        key_material = f"{word_count}_{total_lines}_8"
        key_hash = hashlib.sha256(key_material.encode('utf-8')).digest()
        
        print(f"Key material: {key_material}")
        print(f"Key hash: {key_hash[:8].hex()}")
        
        return key_hash[:32]
    
    def _bits_to_whitespace(self, bits: str) -> str:
        """Convert binary bits to whitespace"""
        whitespace = ""
        for bit in bits:
            if bit == '0':
                whitespace += ' '
            else:
                whitespace += '\t'
        return whitespace
    
    def build_stealth_script(self, original_code: str, output_file: str = "stealth_fairy_tale.py"):
        """Main method to build stealth fairy tale script"""
        # Create enhanced fairy tale script
        fairy_script = self._create_enhanced_fairy_tale(original_code)
        
        # Write the script
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(fairy_script)
        
        print(f"Enhanced stealth script created: {output_file}")
        return output_file

def main():
    if len(sys.argv) < 2:
        print("Usage: python builder_v2.py <python_file_to_obfuscate> [output_file]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "stealth_fairy_tale.py"
    
    if not os.path.exists(input_file):
        print(f"Error: File {input_file} not found")
        sys.exit(1)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        original_code = f.read()
    
    builder = StealthBuilderV2()
    builder.build_stealth_script(original_code, output_file)

if __name__ == "__main__":
    main()
