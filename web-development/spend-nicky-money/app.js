const btnSell = document.querySelector('#btn-sell');
const btnBuy = document.querySelector('#btn-buy');
const itemAmountInput = document.querySelector('#invoice-total');
const totalAmountContainer = document.querySelector('#total-amount');
const totalInvoiceContainer = document.querySelector('#total-invoice');

let invoiceTotal = 0;
let itemAmount = 0;
const startingAmount = 100_000_000_000;
let totalAmount = startingAmount;
let mercedes = 30_000_000_000;


const numberFormatter = (number) => {
    return new Intl.NumberFormat('en-US').format(number);
}

totalAmountContainer.textContent = `Current: ${numberFormatter(totalAmount)} VND`;


btnBuy.addEventListener('click', () => {
    itemAmount++;
    itemAmountInput.value = itemAmount;

    invoiceTotal = itemAmount * mercedes;
    totalInvoiceContainer.textContent = numberFormatter(invoiceTotal);

    totalAmount = startingAmount - invoiceTotal;
    totalAmountContainer.textContent = `Current: ${numberFormatter(totalAmount)} VND`;
});

btnSell.addEventListener('click', () => {
    if (itemAmount > 0) {
        itemAmount--;
        itemAmountInput.value = itemAmount;
    } else {
        btnSell.styledisabled = true;
    }
});
