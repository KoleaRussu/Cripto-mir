<!DOCTYPE html>
<html>
<head>
    <title>Calculare L1</title>
</head>
<body>
    <h1>Calculare L1 in algoritmul DES</h1>
    <input type="text" id="inputMessage" placeholder="Introduceți mesajul (8 caractere)">
    <button onclick="calculateL1()">Calculează L1</button>
    <p id="result"></p>

    <script>
        function calculateL1() {
            const inputMessage = document.getElementById("inputMessage").value;

            if (inputMessage.length !== 8) {
                document.getElementById("result").textContent = "Mesajul trebuie să aibă exact 8 caractere.";
                return;
            }
            const L1 = inputMessage.slice(0, 4);            
            document.getElementById("result").textContent = `L1 este: ${L1}`;
        }
    </script>
</body>
</html>
