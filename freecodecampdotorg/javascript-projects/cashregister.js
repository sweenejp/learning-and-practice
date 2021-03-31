var denom = [
    { name: "ONE HUNDRED", val: 100.0 },
    { name: "TWENTY", val: 20.0 },
    { name: "TEN", val: 10.0 },
    { name: "FIVE", val: 5.0 },
    { name: "ONE", val: 1.0 },
    { name: "QUARTER", val: 0.25 },
    { name: "DIME", val: 0.1 },
    { name: "NICKEL", val: 0.05 },
    { name: "PENNY", val: 0.01 }
];

function checkCashRegister(price, cash, cid) {
    let difference = cash - price;
    let output = {
        status: "CLOSED",
        change: []
    };

    console.log(difference);

    //convert cid array into a object which includes a "total" key value pair

    let register = cid.reduce( (acc, curr) => {
        acc.total += curr[1];
        acc[curr[0]] = curr[1];
        return acc;
    },
    { total: 0 })

    register.total = Math.round(register.total * 100) / 100;

    console.log(register)

    // handle insufficient funds
    if (difference > register.total) {
        output.status = "INSUFFICIENT_FUNDS";
        return output;
    }

    // handle exact change
    if (difference == register.total) {
        output.change = cid;
        return output;
    }

    // Loop through the denomination array
    let change_arr = denom.reduce( (acc, curr) => {
        let value = 0;
        // While there is still money of this type in the drawer
        // And while the difference is larger than the demonination
        while (register[curr.name] > 0 && difference >= curr.val) {
            difference -= curr.val;
            register[curr.name] -= curr.val;
            value += curr.val;
        }
        
        difference = Math.round(difference * 100) / 100;

        if (value > 0 ) {
            acc.push([curr.name, value]);
        }

        return acc; // Return the current change_arr
    }, []); // Initial value of empty array for reduce

    // at this point there should be no difference left. If there is difference left that we means we could not provide the correct amount of change. Or if change_arr has no elements...
    console.log(difference);
    console.log(change_arr);
    console.log(register)
    if (change_arr.length < 1 || difference > 0) {
        output.status = "INSUFFICIENT_FUNDS"
        return output;
    };

    output.status = "OPEN";
    output.change = change_arr;
    return output;


};

console.log(checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]));
