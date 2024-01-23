// Easy base64 encode/decode in node.js
const decodeBase64 = (str) => {
  return Buffer.from(str, "base64").toString("utf-8");
};

const encodeBase64 = (str) => {
  return Buffer.from(str).toString("base64");
};

// Get sys args
const args = process.argv.slice(2);
const [action, value] = args;

// Run
switch (action) {
  case "-e":
    console.log(encodeBase64(value));
    break;
  case "-d":
    console.log(decodeBase64(value));
    break;
  default:
    console.log("Invalid action, use `-e` or `-d`.");
}
