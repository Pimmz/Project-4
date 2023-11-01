/**
 * @jest-environment jsdom
 */

 const { test, expect } = require("@jest/globals");
 const { function } = require("../script-name");
 
 beforeAll(() => {
     let fs = require("fs");
     let fileContents = fs.readFileSync("base.html", "utf-8");
     document.open();
     document.write(fileContents);
     document.close();
 });

 if (typeof module !== "undefined") module.exports = {
    function,
};
