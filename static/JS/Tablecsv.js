class TableCsv {

    constructor(root) {
        this.root = root;
    }


    update(data, headerColumns = []) {
        this.clear();
        this.setHeader(headerColumns);
        this.setBody(data);
    }


    clear() {
        this.root.innerHTML = "";
    }


    setHeader(headerColumns) {
        this.root.insertAdjacentHTML(
            "afterbegin",
            `
            <thead>
                <tr>
                    ${headerColumns.map((text) => `<th>${text}</th>`).join("")}
                </tr>
            </thead>
        `
        );
    }


    setBody(data) {
        const rowsHtml = data.map((row) => {
            return `
                <tr>
                    ${row.map((text) => `<td>${text}</td>`).join("")}
                </tr>
            `;
        });

        this.root.insertAdjacentHTML(
            "beforeend",
            `
            <tbody>
                ${rowsHtml.join("")}
            </tbody>

        `
        );
    }
}

const tableRoot = document.querySelector("#csvRoot");
const csvFileInput = 'output.csv';
alert(csvFileInput.value);
const tableCsv = new TableCsv(tableRoot);


Papa.parse('output.csv', {
    download: true,
    delimiter: ",",
    skipEmptyLines: true,
    complete: (results) => {
        tableCsv.update(results.data.slice(1), results.data[0]);
    }
});