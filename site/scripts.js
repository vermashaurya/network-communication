function setOutputState(element, message, isError = false) {
  element.textContent = message;
  element.classList.toggle("is-error", isError);
  element.classList.toggle("is-success", !isError && Boolean(message));
}

function onesComplement(bits) {
  return [...bits].map((bit) => (bit === "0" ? "1" : "0")).join("");
}

function binaryAdd(a, b) {
  const width = Math.max(a.length, b.length);
  const sum = parseInt(a, 2) + parseInt(b, 2);
  const carry = sum >> width;
  let result = sum & ((1 << width) - 1);
  if (carry) {
    result = (result + carry) & ((1 << width) - 1);
  }
  return result.toString(2).padStart(width, "0");
}

function checksum(blocks) {
  let running = blocks[0];
  for (let index = 1; index < blocks.length; index += 1) {
    running = binaryAdd(running, blocks[index]);
  }
  return onesComplement(running);
}

const checksumButton = document.getElementById("checksum-btn");
if (checksumButton) {
  checksumButton.addEventListener("click", () => {
    const value = document.getElementById("checksum-input").value.trim();
    const blocks = value ? value.split(/\s+/) : [];
    const output = document.getElementById("checksum-output");

    if (!blocks.length || blocks.some((block) => !/^[01]+$/.test(block))) {
      setOutputState(output, "Use space-separated binary blocks such as 1010 0101 1111.", true);
      return;
    }

    const width = blocks[0].length;
    if (blocks.some((block) => block.length !== width)) {
      setOutputState(output, "Every block must have the same width.", true);
      return;
    }

    setOutputState(output, `Checksum result: ${checksum(blocks)}`);
  });
}

const parityButton = document.getElementById("parity-btn");
if (parityButton) {
  parityButton.addEventListener("click", () => {
    const value = document.getElementById("parity-input").value.trim();
    const output = document.getElementById("parity-output");

    if (!/^[01]+$/.test(value)) {
      setOutputState(output, "Use only 0s and 1s in the bitstring.", true);
      return;
    }

    const onesCount = [...value].filter((digit) => digit === "1").length;
    const isEven = onesCount % 2 === 0;
    setOutputState(
      output,
      isEven
        ? `Valid even parity. Ones count: ${onesCount}.`
        : `Parity check failed. Ones count: ${onesCount}.`,
      !isEven,
    );
  });
}
