function onesComplement(bits) {
  return [...bits].map((b) => (b === "0" ? "1" : "0")).join("");
}

function binaryAdd(a, b) {
  const width = Math.max(a.length, b.length);
  const sum = parseInt(a, 2) + parseInt(b, 2);
  const carry = sum >> width;
  let result = sum & ((1 << width) - 1);
  if (carry) result = (result + carry) & ((1 << width) - 1);
  return result.toString(2).padStart(width, "0");
}

function checksum(blocks) {
  let running = blocks[0];
  for (let i = 1; i < blocks.length; i += 1) {
    running = binaryAdd(running, blocks[i]);
  }
  return onesComplement(running);
}

document.getElementById("checksum-btn").addEventListener("click", () => {
  const value = document.getElementById("checksum-input").value.trim();
  const blocks = value.split(/\s+/);
  const output = document.getElementById("checksum-output");
  if (!blocks.length || blocks.some((b) => !/^[01]+$/.test(b))) {
    output.textContent = "Invalid input. Use bitstrings like: 1010 0101 1111";
    return;
  }
  const width = blocks[0].length;
  if (blocks.some((b) => b.length !== width)) {
    output.textContent = "All blocks must be equal length.";
    return;
  }
  output.textContent = `Checksum: ${checksum(blocks)}`;
});

document.getElementById("parity-btn").addEventListener("click", () => {
  const value = document.getElementById("parity-input").value.trim();
  const output = document.getElementById("parity-output");
  if (!/^[01]+$/.test(value)) {
    output.textContent = "Invalid bitstring.";
    return;
  }
  const even = [...value].filter((ch) => ch === "1").length % 2 === 0;
  output.textContent = even ? "Even parity check passed." : "Even parity check failed.";
});
