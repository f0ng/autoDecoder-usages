import express from "express";
import axios from "axios";
import puppeteer from "puppeteer-core";

const app = express();
app.use(
  express.urlencoded({
    extended: true,
    limit: "50mb",
    parameterLimit: 5000,
  })
);
app.use(express.json({ limit: "50mb" }));

// 加密
app.post("/encode", async (req, res) => {
  let body = req.body.dataBody;

  let encResult = "";
  if (typeof req.body.requestorresponse == "undefined") {
    encResult = await bothEncode(body);
  } else if (req.body.requestorresponse == "request") {
    encResult = await requestEncode(body);
  } else {
    encResult = await responseEncode(body);
  }

  console.log("发送加密报文：%O\r\n", encResult);
  res.send(encResult);
});

async function bothEncode(body) {
  console.log("-".repeat(15) + " [Both Encode] " + "-".repeat(15) + "\n");
  console.log("Body: " + body + "\r\n");

  // let result = await consoleRun(`encryptBody(\`${data}\`)`);
  // console.log("result:" + result + "\r\n");
  return result;
}

async function requestEncode(body) {
  console.log("-".repeat(15) + " [Request Encode] " + "-".repeat(15) + "\n");
}

async function responseEncode(body) {
  console.log("-".repeat(15) + " [Response Encode] " + "-".repeat(15) + "\n");
}

// 解密
app.post("/decode", async (req, res) => {
  let body = req.body.dataBody;
  let decResult = "";
  if (typeof req.body.requestorresponse == "undefined") {
    decResult = await bothDecode(body);
  } else if (req.body.requestorresponse == "request") {
    decResult = await requestDecode(body);
  } else {
    decResult = await responseDecode(body);
  }

  console.log("接收加密明文：%O\r\n", decResult);
  res.header("Content-Type", "application/json;charset=utf-8");
  res.send(decResult);
});

async function bothDecode(body) {
  console.log("-".repeat(15) + " [Both Decode] " + "-".repeat(15) + "\n");
  body = body.trim();

  // return await consoleRun(`decryptKey('${body}')`);
}

async function requestDecode(body) {
  console.log("-".repeat(15) + " [Request Decode] " + "-".repeat(15) + "\n");
}

async function responseDecode(body) {
  console.log("-".repeat(15) + " [Response Decode] " + "-".repeat(15) + "\n");
}

// Hook 调试
app.post("/debug", async (req, res) => {
  console.log("-".repeat(15) + " [Console Debug] " + "-".repeat(15) + "\n");
  let command = Object.keys(req.body)[0];
  let result = await consoleRun(command);

  console.log(`Command：${command} \r\nResult: ${result}\r\n`);
  res.header("Content-Type", "text/plain;charset=utf-8");
  res.send(result);
});

// 在 Chrome Console 控制台执行命令
async function consoleRun(command) {
  const wsKey = await axios.get("http://127.0.0.1:9222/json/version");
  const browser = await puppeteer.connect({
    browserWSEndpoint: wsKey.data.webSocketDebuggerUrl,
    defaultViewport: null,
  });

  const pages = await browser.pages();
  const page = pages[0];
  console.log(`\r\n[+] Console run: ${command}\r\n`);
  const res = await page.evaluate(command);
  await browser.disconnect();

  return res;
}

const server = app.listen(8888, function () {
  const host = server.address().address;
  const port = server.address().port;

  console.log("应用实例，访问地址为 http://%s:%s\n", host, port);
});
