function caesarCipher(text, shift, isDecrypt = false) {
    const shiftAmount = isDecrypt ? 26 - shift : shift;
    return text
      .split('')
      .map((char) => {
        if (/[a-zA-Z]/.test(char)) {
          const isUpperCase = char === char.toUpperCase();
          const charCode = char.charCodeAt(0) - (isUpperCase ? 65 : 97);
          const shiftedCharCode = (charCode + shiftAmount) % 26;
          return String.fromCharCode(shiftedCharCode + (isUpperCase ? 65 : 97));
        }
        return char;
      })
      .join('');
  }

  function generateResults() {
    const plaintext = document.getElementById("plaintext").value;
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = '';

    for (let key = 1; key <= 25; key++) {
      const encryptedText = caesarCipher(plaintext, key);
      const decryptedText = caesarCipher(plaintext, key, true);
      resultsDiv.innerHTML += `<p>Ключ ${key} - Зашифрованный текст: ${encryptedText}, Расшифрованный текст: ${decryptedText}</p>`;
    }
  }

  document.getElementById("plaintext").addEventListener("input", generateResults);
  generateResults();