from fastapi import FastAPI
import uvicorn
import random
import os
import src.decryptia as decryptia


app = FastAPI()


@app.get("/{encryption}/{action}/{text}")
async def main(encryption: str, action: str, text: str, key: str = "Decryptia"):
    final_return = {}
    match encryption.lower():
        case "base64":
            match action.lower():
                case "encode":
                        base_result = decryptia.Base64().Encode(text)
                        final_return = {
                            "encoded": base_result,
                            "type": "Base64",
                            "input_text": text
                        }
                case "decode":
                        base_result = decryptia.Base64().Decode(text)
                        final_return = {
                            "decoded": base_result,
                            "type": "Base64",
                            "input_text": text
                        }
        case "morsecode":
            match action.lower():
                case "encode":
                        morse_result = decryptia.MorseCode().Encode(text)
                        final_return = {
                            "encoded": morse_result,
                            "type": "MorseCode",
                            "input_text": text
                        }
                case "decode":
                        morse_result = decryptia.MorseCode().Decode(text)
                        final_return = {
                            "decoded": morse_result,
                            "type": "MorseCode",
                            "input_text": text
                        }
        case "binarycode":
            match action.lower():
                case "encode":
                        binary_result = decryptia.BinaryCode().Encode(text)
                        final_return = {
                            "encoded": binary_result,
                            "type": "BinaryCode",
                            "input_text": text
                        }
                case "decode":
                        binary_result = decryptia.BinaryCode().Decode(text)
                        final_return = {
                            "decoded": binary_result,
                            "type": "BinaryCode",
                            "input_text": text
                        }
        case "vigenerecipher":
            match action.lower():
                case "encrypt":
                        vigenere_result = decryptia.VinegereCipher().Encrypt(text, key)
                        final_return = {
                            "encrypted": vigenere_result,
                            "type": "VigenereCipher",
                            "input_text": text,
                            "key": key
                        }
                case "decrypt":
                        vigenere_result = decryptia.VinegereCipher().Decrypt(text, key)
                        final_return = {
                            "decrypted": vigenere_result,
                            "type": "VigenereCipher",
                            "input_text": text,
                            "key": key
                        }
    return final_return


@app.get("/vigenerecipher/{action}/{text}/{key}")
async def mainV(action: str, text: str, key: str = "Decryptia"):
    final_return = {}
    match action.lower():
        case "encrypt":
                vigenere_result = decryptia.VinegereCipher().Encrypt(text, key)
                final_return = {
                    "encrypted": vigenere_result,
                    "type": "VigenereCipher",
                    "input_text": text,
                    "key": key
                }
        case "decrypt":
                vigenere_result = decryptia.VinegereCipher().Decrypt(text, key)
                final_return = {
                    "decrypted": vigenere_result,
                    "type": "VigenereCipher",
                    "input_text": text,
                    "key": key
                }
    return final_return


uvicorn.run(app, port=3000, host="0.0.0.0")
