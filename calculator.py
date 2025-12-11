<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Calculator</title>

  <style>
    body {
      background: #111;
      color: white;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      font-family: Arial, sans-serif;
    }

    .calculator {
      background: #222;
      padding: 20px;
      border-radius: 12px;
      box-shadow: 0 0 15px rgba(255,255,255,0.1);
      width: 260px;
    }

    .display {
      width: 100%;
      height: 60px;
      background: black;
      color: #0f0;
      text-align: right;
      padding: 10px;
      font-size: 28px;
      border-radius: 8px;
      margin-bottom: 15px;
      box-sizing: border-box;
    }

    .buttons {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
    }

    button {
      padding: 15px;
      font-size: 18px;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      background: #333;
      color: white;
      transition: 0.2s;
    }

    button:hover {
      background: #555;
    }

    .equal {
      background: #0a84ff;
      color: white;
    }

    .equal:hover {
      background: #006ad1;
    }
  </style>
</head>

<body>
  <div class="calculator">
    <div class="display" id="display">0</div>

    <div class="buttons">
      <button onclick="clearDisplay()">C</button>
      <button onclick="deleteLast()">DEL</button>
      <button onclick="appendValue('/')">/</button>
      <button onclick="appendValue('*')">*</button>

      <button onclick="appendValue('7')">7</button>
      <button onclick="appendValue('8')">8</button>
      <button onclick="appendValue('9')">9</button>
      <button onclick="appendValue('-')">-</button>

      <button onclick="appendValue('4')">4</button>
      <button onclick="appendValue('5')">5</button>
      <button onclick="appendValue('6')">6</button>
      <button onclick="appendValue('+')">+</button>

      <button onclick="appendValue('1')">1</button>
      <button onclick="appendValue('2')">2</button>
      <button onclick="appendValue('3')">3</button>
      <button onclick="calculate()" class="equal">=</button>

      <button onclick="appendValue('0')" style="grid-column: span 2">0</button>
      <button onclick="appendValue('.')">.</button>
    </div>
  </div>

  <script>
    let display = document.getElementById("display");

    function appendValue(value) {
      if (display.innerText === "0") {
        display.innerText = value;
      } else {
        display.innerText += value;
      }
    }

    function clearDisplay() {
      display.innerText = "0";
    }

    function deleteLast() {
      display.innerText = display.innerText.slice(0, -1);
      if (display.innerText === "") {
        display.innerText = "0";
      }
    }

    function calculate() {
      try {
        display.innerText = eval(display.innerText);
      } catch {
        display.innerText = "Error";
      }
    }

    // Keyboard support
    document.addEventListener("keydown", (event) => {
      if (/[\d+\-*/.]/.test(event.key)) {
        appendValue(event.key);
      } else if (event.key === "Enter") {
        calculate();
      } else if (event.key === "Backspace") {
        deleteLast();
      } else if (event.key === "Escape") {
        clearDisplay();
      }
    });
  </script>
</body>
</html>
